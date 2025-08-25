# Sistema de Fichas - Flask (Python)

## Requisitos
- Python 3.10+
- Pipenv ou pip
- SQLite (embutido)

## Instalação
```bash
cd site_py_full_v3
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

A aplicação subirá em http://127.0.0.1:5000

## Usuário inicial
Ao iniciar pela primeira vez, um usuário admin é criado:
- email: admin@example.com
- senha: admin123

## Estrutura
- Autenticação (login/logout)
- Gestão de Fichas (wizard em 2 etapas com endereço, celular, forma de pagamento, nota fiscal)
- Gestão de Usuários (listar, criar/editar, ativar/bloquear)
- Financeiro (fechamento mensal, exportar CSV)

## Observações
- Se você já rodou versão anterior, apague `instance/app.db` para recriar com as novas colunas.
