# Monitoraggio Elezioni
[![Build status](https://travis-ci.org/Cesaaar/mon_elezioni.svg?branch=master)](https://travis-ci.org/Cesaaar)


http://www.monitoraggioelezioni.it

Monitoraggio dei principali partecipanti alle elezioni politiche italiane del 2018.


### Per lanciare il servizio in locale ###

```
git clone https://github.com/Cesaaar/mon_elezioni.git

docker build -t app .

docker-compose up -d
```

### config.py ###
Il file config.py contiene le diverse configurazioni, in particolare la struttura del database corrisponde a quella realizzata nel repository od_elezioni.

### Tecnologie ###
- python
- flask
- html
- javascript
- css

### Database ###

- od_elezioni
