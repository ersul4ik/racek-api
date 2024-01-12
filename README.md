# racek-api
The product helps users to manage hiking tours 


## Roadmap

- [x] Find a way of using charts and put it into the codebase
- [x] Describe the actors (type of users) ([more](docs/actors/doc.md))
- .... ([read more](docs/roadmap.md))

## Development

- Python (3.11)
- Fast-API

### Getting Started

```bash
pyenv install 3.11
pyenv virtualenv 3.11 racek-api
pyenv activate racek-api
```

Update `pip` & `setuptools`, install `pip-tools`:

```bash
pip install -U pip pip-tools setuptools
```

### Installation

```bash

pip install -r requirements.txt
```

### How to Run

```bash
cd src

uvicorn main:app --reload (--port <port>)
```


### How to use

[Swagger] - <host_name>/docs