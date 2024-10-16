# 2daw-abp-p1-s2-example

Exemple de suport per l'sprint 2 del projecte 1 de 2n de DAW.

## Setup

### Python Virtual Environment

#### Linux

Crea l'entorn:

    python3 -m venv .venv

L'activa:

    source .venv/bin/activate

Instal·la el requisits:

    pip install -r requirements.txt

Per a generar el fitxer de requiriments:

    pip freeze > requirements.txt

Per desactivar l'entorn:

    deactivate

#### Windows

Crea l'entorn:

    python -m venv .venv

L'activa:

    .venv\Scripts\activate

Instal·la el requisits:

    pip install -r requirements.txt

Per a generar el fitxer de requiriments:

    pip freeze > requirements.txt

Per desactivar l'entorn:

    deactivate

### Base de dades

#### SQLite

La base de dades SQLite és dins de la carpeta [sqlite](./sqlite) s'ha de dir `database.db`, tot i que es pot configurar un nom diferent al fitxer de configuració. S'ha creat amb l'script [database.sql](./sqlite/database.sql). Aquest script conté dos usuaris de prova:

* `ed@test.cat` amb la contrasenya `patata` i el rol **editor**.
* `vi@test.cat` amb la contrasenya `patata` i el rol **viewer**.

#### PostgreSQL o MySQL remot

S'ha de configurar la variable d'entorn `SQLALCHEMY_DATABASE_URI` al fitxer `.env`. Ha de tenir aquesta sintaxis:

    #postgresql
    SQLALCHEMY_DATABASE_URI="postgresql://usuari:password@host:port/base-de-dades"
    #mysql
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://usuari:password@host:port/base-de-dades"

La base de dades ha de tenir les taules creades. Aquí pots trobar l'script per crear les taules a [PostgreSQL](./docker/databases/postgres/database.sql) i per [MySQL](./docker/databases/mysql/database.sql).

#### PostgreSQL o MySQL dockeritzat

Dins de la carpeta [docker](./docker/) crea un fitxer `.env` fent servir com a base el [.env.exemple](./docker/.env.exemple) i inicia el docker compose de MySQL o PostgreSQL. Desprès, afegeix com el punt anterior la variable `SQLALCHEMY_DATABASE_URI` al fitxer `.env` de l'arrel.

### Fitxer de configuració

Crea un fitxer `.env` amb els paràmetres de configuració. Pots fer servir com a base el fitxer [.env.exemple](./.env.exemple).

## Run

Executa:

    flask run --debug

I obre un navegador a l'adreça: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Debug amb Visual Code

Des de l'opció de `Run and Debug`, crea un fitxer anomenat `launch.json` amb el contingut següent:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "MY APP",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```
