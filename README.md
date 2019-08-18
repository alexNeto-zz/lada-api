# Lada API


[![Build Status](https://travis-ci.org/alexNeto/lada-api.svg?branch=master)](https://travis-ci.org/alexNeto/lada-api)
[![Coverage Status](https://coveralls.io/repos/github/alexNeto/lada-api/badge.svg?branch=master)](https://coveralls.io/github/alexNeto/lada-api?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/29914403de1fdead5141/maintainability)](https://codeclimate.com/github/alexNeto/lada-api/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/99156cf8d9f74c7faaefaaed6c343d4f)](https://www.codacy.com/app/alexNeto/lada-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alexNeto/lada-api&amp;utm_campaign=Badge_Grade)

Api para consulta e comparação de previsão do tempo.
Related To [lada-app](https://github.com/alexNeto/lada-app)

- [Lada API](#lada-api)
  - [Setup](#setup)
    - [Create a _venv_ in the project folder](#create-a-venv-in-the-project-folder)
    - [Activate the _venv_](#activate-the-venv)
    - [Export Variables](#export-variables)
    - [Install the dependencies](#install-the-dependencies)
    - [Run it](#run-it)

## Setup

### Create a _venv_ in the project folder

```bash
python3 -m venv ./venv
```

### Activate the _venv_
  
- For Linux or Mac:

```bash
source venv/bin/activate
```

- For Windows:

```bash
\venv\Scripts\activate.bat
```

### Export Variables

> this step is only if you want live reload.

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
```

### Install the dependencies

```bash
pip install -r requirements.txt
```

### Run it

```bash
python -m flask run
```
