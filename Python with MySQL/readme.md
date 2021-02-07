PYTHON WITH MYSQL

steps taken:
1. pipenv shell // only done first time
    // create virtual env in C:\Users\krunal\.virtualenvs as Python_with_MySQL-9tEszp2Q

// activate venv everytime you want to run the script
2. source C:\Users\krunal\.virtualenvs\Python_with_MySQL-9tEszp2Q\Scripts\activate
    activate virtual env
3. pip install mysql-connector-python --skip-lock
4. pipenv lock
5. select correct python intepretor
   ctrl+shift+p -> python intepretor-> select venv intepretor (here Python With MySQL pipenv)


if pipenv locking gets stuck somewhere

do
- pipenv install <packagename> --skip-lock
- pipenv lock
