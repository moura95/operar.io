# Desafio Framework_digital

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
### Caso de Error
```
"no Such Table core.enderecos" 
execute python manage.py migrate --run-syncdb
