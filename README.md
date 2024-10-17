# flask lab

https://flask.palletsprojects.com/en/3.0.x/quickstart/

### Per lanciare:

Crea un ambiente virtuale python:
```shell
python -m venv .venv
```

Se la console ti segnala un errore di permessi, lancia su power shell come amministratore:
```shell
Set-ExecutionPolicy Unrestricted -Force
```

Installa le dipendenze scritte sul file requirements.txt
```shell
pip install -r requirements.txt
```

lancia il server di prova con 
```shell
flask run --debug
```
per uscire dal web server ctrl+c
