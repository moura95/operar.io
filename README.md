 
### Pré-requisitos
* [ ] Python 3.x 
* [ ] Virtualenv

### Criando Virtualenv
```
python3-m virtualenv venv
```
### Ativando Virtualenv
```
sourcer venv/bin/activate
```

### Instalando as bibliotecas

```
pip install -r requirements.txt
```

### Executando o projeto

```
python manage.py migrate

python manage.py runserver

```

### Populate database Script

```
Com o servidor rodando 127.0.0.1:8000
execute python3 scripts/populate.py
```


### Executando Tests Unitarios

```
pytest -v
```

### Caso de Error
```
"no Such Table core.enderecos" 
execute python manage.py migrate --run-syncdb
```
