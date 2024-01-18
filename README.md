# TGR

<br>

## Para inicializar a aplicação

<br>

### Criando ambiente virtual

```
\TGR> python -m venv <name venv>
```

### Instalando dependências

```
\TGR> pip install -r requirements.txt
```
<br>

---

<br>

## Iniciando ambiente virtual

<br>

#### Linux

```
\TGR> source venv/bin/activate
```

#### Windows

```
\TGR> .\venv\Scripts\activate
```

<br>

## Desativando ambiente virtual

<br>

```
\TGR> deactivate
```

---

<br>

## Criando usuário

```
\TGR\tgr> python manage.py createsuperuser
\TGR\tgr> python manage.py migrate
```

## Aplicando as migrações

```
\TGR\tgr> python manage.py makemigrations
\TGR\tgr> python manage.py migrate
```

## Criando os objetos no banco de dados

- Há um comando para criar os objetos no banco de dados, que deve ser executado após as migrações:

```
\TGR\tgr> python manage.py init
```

## Iniciar o projeto (porta opcional, padrão 8000)


```
\TGR\tgr> python manage.py runserver <port>
```

## Exportando dados

- Exportando dados dos modelos principais (recomendado, por enquanto)
```
\TGR\tgr> python -Xutf8 .\manage.py dumpdata main --output=data-models.json
```

- Exportando todos os dados (dá erros de importação, não recomendado)
```
\TGR\tgr> python -Xutf8 .\manage.py dumpdata --output=data.json
```

#### <b>OBS:</b> Os dados estão sendo exportados com o charset adaptado para o Brasil, mas caso queria fazer alguma mudança, retire o argumento -Xutf8.

<br>

## Importando dados

```
\TGR\tgr> python manage.py loaddata data.json
```

## Importante
- Acredito que você pode ter alguns problemas ao instalar algumas dependências, caso dê algum problema, instale manualmente as extensões com problema, já adianto alguns comandos que você pode executar abaixo:

    ```
    \TGR\tgr> python -m pip install --upgrade pip
    \TGR\tgr> pip install django
    \TGR\tgr> pip install django-bootstrap-form
    \TGR\tgr> pip install mysqlclient

    ```
- Crie, pelo MySQL Workbench ou Shell uma base de dados previamente, com o nome 'tgr'.
- Lembre se de trocar o seu usuário no [settings.py](/tgr/tgr/settings.py)
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'tgr',
            'USER': 'seuUsuario', # Altere para seu usuário
            'PASSWORD': 'suaSenha', # Altere para sua senha
            'HOST': 'localhost',
            'PORT': '3306',
            'OPTIONS': {
                'charset': 'utf8mb4',
            }
        }
    }
    ```
