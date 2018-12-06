# personal issue automation stuff

but maybe you'll find it useful too

## setup

  git clone git@github.com:vilmibm/issuer.git
  cd issuer
  cp issuer/example.config.py issuer/config.py
  nano issuer/config.py # add your personal github token
  python3 -mvenv issuer.venv
  source issuer.venv/bin/activate
  pip install -e .

## generate tracking issue checklists

    issuer tracking-checklist --owner vilmibm --repo prosaic --repo tildemush --label bug

 output is like:

     - [ ] [do some stuff with things](https://github.com/vilmibm/prosaic/issues/123)
     - [x] [fix the thing](https://github.com/vilmibm/tildemush/issues/456)
    
