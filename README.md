# How to run project
1.create venv (python -m venv .venv)
2.pip install -r requirements.txt
3.you need to change db credentials your admin name/password in /alembic.ini and /settings.py for postgress
4.To up your docker you need to install choco make (maybe you will need to install it with admin privileges) and write "make up" in terminal
5.for set up migrations (alembic upgrade head) 
