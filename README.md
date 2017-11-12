# Monitoraggio Elezioni
[![Build status](https://travis-ci.org/Cesaaar/travis-lab.svg?master)](https://travis-ci.org/Cesaaar)

Monitoraggio dei principali partecipanti alle elezioni politiche italiane del 2018.


### Per lanciare il servizio in locale ###

```
git clone https://github.com/Cesaaar/mon_elezioni.git

source venv/bin/activate
export SETTINGS=~/Documents/opendata/config.py
python runserver.py

```

### Tecnologie ###
- python
- flask
- html
- javascript
- css

### config.py ###
Il file config.py contiene le diverse configurazioni, in particolare la struttura del database corrisponde a quella realizzata nel repository od_elezioni.

### Database ###

- od_elezioni
