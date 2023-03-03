# KTPMonitor4, Linux

## Установка git

Установка git, создание ключа

    sudo apt install git
    ssh-keygen -t ed25519 -C "your_email@example.com"

после этого надо вставить ключ в своем аккаунте на git

    git clone git@github.com:khuaigul/KTPMonitor4.git

## Установка python

    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.9
    sudo apt install python3-pip
    
## Установка mysql

ВАЖНО: пароль надо либо сделать как в проекте, либо переписать проект

    sudo apt update
    sudo apt install mysql-server
    sudo mysql_secure_installation

если вылезет такая ошибка:

    Error: SET PASSWORD has no significance for user 'root'@'localhost' as the authentication method used doesn't store authentication data in the MySQL server. Please consider using ALTER USER instead if you want to change authentication parameters.
    
то надо сделать вот так:
Open the terminal application. 
1. Terminate the mysql_secure_installation from another terminal using the killall command:
sudo killall -9 mysql_secure_installation 
2. Start the mysql client:
sudo mysql 
3. Run the following SQL query: 
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'SetRootPasswordHere';
exit
5. Then run the following command to secure it:
sudo mysql_secure_installation 
6. When promoted for the password enter the SetRootPasswordHere (or whatever you set when you ran the above SQL query) 
7. That is all. 

## установка Visual studio code



## Установка библиотек Python

    pip install mysql-connector-python
    pip install django
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter


# Запуск
## один раз надо:

    sudo mysql
    create database KTP_Monitor;

далее скриптом создаем таблицы

    python3 add_new_tables.py

далее мигрируем
  
    python manage.py migrate


теперь можно запускать 

    python manage.py runserver

--------------
CREATE DATABASE KTP_Monitor;
