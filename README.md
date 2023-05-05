# Meetup PodCodar - FastAPI

[Página oficial do framework](https://fastapi.tiangolo.com/)

## Criação do repositório usando GitHub CLI

- `gh repo create`

## Criação do ambiente virtual

- `python3 -m venv .venv`
- `source .venv/bin/activate`

## Instalação das dependências

- `pip install flake8 black pytest "fastapi[all]"`

## Criação do arquivo `main/app.py`

- Rota GET "/"

## Execução com `uvicorn`

- `python -m uvicorn app.main:app --reload`

## Ativação do `ngrok`

- `ngrok http 8000`

## Implementação do teste

- `TestClient`
- `assert status_code`
- `assert json()`

## [Início do TDD] Teste: GET "/members"

## Implementação: GET "/members"

`MEMBER_DB = []` (nunca faça isso na vida real!)

## Teste: POST "/members"

- POST + asserts
- GET + asserts

## Implementação: POST "/members"

- Parâmetro do Body
- `MEMBER_DB.append(member)`
- `status_code` padrão

## (Se der tempo) GitHub Action
