import json
import sys

import click
import requests

from .config import GH_TOKEN, GH_URL

def query(q_text, variables=None):
  q_json = {
      'query': q_text,
  }
  if variables is not None:
    q_json['variables'] = variables
  resp = requests.post(
      GH_URL, 
      data=json.dumps(q_json), 
      headers={'Authorization': f'bearer {GH_TOKEN}'})

  resp.raise_for_status()

  return json.loads(resp.content)

@click.group()
def cli():
  pass

@cli.command()
@click.option('--owner', required=True, help='user or org among whose repos to search.')
@click.option('--repo', required=True, multiple=True, help='repo to search in. can be specified multiple times.')
@click.option('--label', required=True, multiple=True, help='label to use. can be specified multiple times.')
def tracking_checklist(owner, repo, label):
  repo_ids = []
  for r in repo:
    result = query( '''
        query($name: String!, $owner: String!) {
          repository(owner: $owner, name: $name) { id }
        }
        ''', variables={"name": r, "owner": owner})
    if result.get('errors'):
      raise ValueError(result['errors'])
    repo_ids.append(result['data']['repository']['id'])
  result = query('''
    query($repo_ids: [ID!]!, $labels: [String!]!) {
      nodes(ids: $repo_ids) {
        ... on Repository {
          nameWithOwner
          issues(first: 100, labels: $labels) {
            edges {
              node {
                ... on Issue {
                  title
                  state
                  url
                }
              }
            }
          }
        }
      }
    }
  ''', variables={"repo_ids":repo_ids, "labels":label})
  if result.get('errors'):
    raise ValueError(result['errors'])
  for repo in result['data']['nodes']:
    for issue in (i['node'] for i in repo['issues']['edges']):
      title = issue['title']
      url = issue['url']
      link = f' [{title}]({url}) '
      state = '- [ ] ' if issue['state'] == 'OPEN' else '- [x] '
      print(f'{state} {link}')

def main():
  cli()
