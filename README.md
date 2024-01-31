# TGR

<br>

## Para preparar a inicialização da aplicação

<br>

### Criando ambiente virtual

```
\TGR> python -m venv <name venv>
```

<br>

## Iniciando ambiente virtual

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

### Instalando dependências
- Instale na venv preferencialmente

```
(venv) \TGR> pip install -r requirements.txt
```
<br>

---

<br>


## Aplicando as migrações

```
\TGR\tgr> python manage.py makemigrations // Provavelmente não será necessário, porque deixarei um arquivo com a migração inicial
\TGR\tgr> python manage.py migrate
```

<br>

## Criando super usuário

```
\TGR\tgr> python manage.py createsuperuser
```

<br>

## Criando os objetos no banco de dados

- Há um comando para criar os objetos no banco de dados, que deve ser executado após as migrações:

```
\TGR\tgr> python manage.py init
```

<br>

## Iniciar o projeto (porta opcional, padrão 8000)


```
\TGR\tgr> python manage.py runserver <port>
```

<br>

## Importante
- Acredito que você pode ter alguns problemas ao instalar algumas dependências, caso dê algum problema, instale manualmente as extensões com problema, já adianto alguns comandos que você pode executar abaixo:

    ```
    \TGR\tgr> python -m pip install --upgrade pip
    \TGR\tgr> pip install django
    \TGR\tgr> pip install django-bootstrap-form
    \TGR\tgr> pip install mysqlclient

    ```
- Crie, pelo MySQL Workbench ou Shell uma base de dados previamente, com o nome 'tgr'.
- Lembre se de deixar configurado o [settings_local.py](/tgr/tgr/settings_local.py). As configurações feitas nesse arquivo serão importadas no [settings.py](/tgr/tgr/settings.py).
    ```
    DATABASE_USER = 'root' # Troque por seu usuário na base de dados
    DATABASE_PASSWORD = 'SUA_SENHA_AQUI' # Troque por sua senha na base de dados
    DATABASE_HOST = 'localhost' # Caso esteja utilizando um servidor remoto, troque para o endereço do servidor
    DATABASE_PORT = '3306' # Troque para a porta utilizada pelo servidor de banco de dados
    ```
- Como é um arquivo que contém informações potencialmente confidenciais, eu apenas deixarei um template e minhas reais configurações não estarão disponíveis.

<br>

## Exportando dados

- Exportando dados dos modelos principais (recomendado, por enquanto)
```
\TGR\tgr> python -Xutf8 .\manage.py dumpdata main --output=data-models.json
```

- Exportando todos os dados (dá erros de importação, não recomendado)
```
\TGR\tgr> python -Xutf8 .\manage.py dumpdata --output=data.json
```

<br>

#### <b>OBS:</b> Os dados estão sendo exportados com o charset adaptado para o Brasil, mas caso queria fazer alguma mudança, retire o argumento -Xutf8.

<br>

## Importando dados

```
\TGR\tgr> python manage.py loaddata data.json
```
