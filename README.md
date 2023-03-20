# KTPMonitor, Linux

## Установка git

Установка git, создание ключа

    sudo apt install git
    ssh-keygen -t ed25519 -C "your_email@example.com"

После этого надо вставить ключ в своем аккаунте на git

    git clone git@github.com:khuaigul/KTPMonitor.git

## Установка python

    sudo apt-get update
    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.9
    sudo apt install python3-pip
    
## Установка mysql

Важно: пароль надо либо сделать как в проекте, либо переписать проект

    sudo apt update
    sudo apt install mysql-server
    sudo mysql_secure_installation

Если вылезет такая ошибка:

    Error: SET PASSWORD has no significance for user 'root'@'localhost' as the authentication method used doesn't store authentication data in the MySQL server. Please consider using ALTER USER instead if you want to change authentication parameters.
    
В терминале нужно сделать:
1. Завершите mysql_secure_installation из другого терминала с помощью команды killall:
sudo killall -9 mysql_secure_installation 
2. Запустите клиент mysql:
sudo mysql 
3. Выполните следующий SQL-запрос:
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'SetRootPasswordHere';
exit
4. Затем выполните следующую команду:
sudo mysql_secure_installation 
5. Как пароль используйте установленный выше


## Установка библиотек Python

    pip install mysql-connector-python
    pip install django
    pip install djangorestframework
    pip install markdown       # Markdown support for the browsable API.
    pip install django-filter


# Запуск
## Один раз надо:

    sudo mysql
    create database KTP_Monitor;

Далее скриптом создаем таблицы

    python3 add_new_tables.py

Теперь можно запускать 

    python manage.py runserver

--------------

# KTPMonitor, windows 

## Установка git и репозитория
1. [Скачать](https://git-scm.com/download/win)
2. Добавить в PATH
3. Развернуть репозиторий по инструкции [ниже](https://github.com/khuaigul/KTPMonitor/blob/develop/README.md#%D1%80%D0%B0%D0%B7%D0%B2%D0%B5%D1%80%D1%82%D1%8B%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D1%8F)
## Установка и настройка локальной базы данных

1. Для загрузки и установки MySQL Server следуйте инструкциям по [ссылке](https://wiki.merionet.ru/servernye-resheniya/12/ustanovka-mysql-servera-na-windows-10/?ysclid=lee4gqyolw814370891)
2. При установке MySQL Server на этапе установки нужно поставить пароль ```DB_for_tppo123```
3. Необходимо открыть MySQL Workbench и прописать команды (можно через консоль)
    1. ```create database KTP_Monitor```
4. После этого в консоли необходимо выполнить скрипт ```KTP/taskmanager/main/server/create_tables.py``` (возможно там нужно раскомментить вызов функции)
5. Необходимо установить компилятор для языка Python по [ссылке](https://www.python.org/downloads/)
## Установка и настройка сервера
1. Для установки необходимых компонентов и библиотек выполните в консоли следующие команды
    1. ```pip install mysql-connector-python```
    2. ```pip install django```
## Запуск 
  1. Чтобы запустить сервер необходимо перейти в каталог ```KTP\taskmanager```
  2. В текущем каталоге выполнить команду: 
      1. ```.\manage.py runserver```
      
  При успешных установке и запуске всех необходимых компонентов в консоли появится ссылка на Local-host, при переходе откроется разработанное приложение.
  ```
  March 20, 2023 - 11:04:20
Django version 4.1.7, using settings 'taskmanager.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## Superuser(администратор)
  1. Чтобы создать Superuser
      1. Необходимо перейти в каталог ```KTP\taskmanager```
      2. Выполнить команду ```python manage.py createsuperuser```
      3. Ввести нужные данные : 
  
        ```Username (leave blank to use 'admin'): admin
        Email address: admin@xyz.com
        Password: ********
        Password (again): ********
        Superuser created successfully.```
  2. Пользование 
      1. Зайти по ссылке ```http://127.0.0.1:8000/admin/```
## Вход
  1. Чтобы войти надо создать  Superuser
  2. Зайти по ссылке ```http://127.0.0.1:8000```
  3. По логину и паролю который вводили в Superuser зайти на сайт
 
# Инструкция по git
-----------------
### Развертывание репозитория
Сделайте папку, где вы хотите создать локальный репозиторий.
Выполните там команды в следующем порядке:
```sh
git init # Инициализировать локальный репозиторий в папке
# Скопировать репозиторий
git clone https://github.com/khuaigul/KTPMonitor.git 
# Указать, что вы будете работать с заданным удаленным репозиторием
git remote add origin https://github.com/khuaigul/KTPMonitor.git 
git fetch origin # Обновить информацию про ветки
```
Теперь у вас локально есть копия заданного репозитория под именем origin.
### Аутентификация
Когда вы попробуйте отправить какие то изменения в удаленный репозиторий, то будет предложено залогиниться через браузер.
Так же необходимо указать некоторую информацию о себе:
```sh
git config user.email "someemail@mail"
git config user.name "PussyDestroyer69"
```
### Работа с ветками
Ветка содержит в себе файлы проекта и историю коммитов(изменений). Работая в одной ветке можно не боятся повредить остальные.

 Для создания незавесимого рабочего пространства, можно создать новую ветку, которая изначально будет копией ветки, от которой создается. Дальнейшие ее изменения (коммиты) не влияют на изначальную ветку, но в какой то момент их можно слить, объеденив содержимое.
 
Ветки бывают **удаленными** и **локальными**.
Удаленные находятся в удаленном репозитории, если на них переключиться появляются их локальные копии.
Локальные ветки - это ветки, которые редактируются на устройстве, их потом можно коммитить и сливать с удаленными.
Чтобы обновить список удаленных веток выполните:
```sh
git fetch origin
```
Чтобы посмотреть список веток используйте следующие команды:
```sh
git branch -r # удаленные ветки
git branch # локальные ветки
git branch -a # все ветки
```
Рабочую ветку и информацию о ней можно посмотреть в:
```sh
git status
```
Для переключения (изменения рабочей ветки) используйте checkout:
```sh
git checkout some_branch
git checkout some_branch -- # Если есть файл с названием как у ветки
```
Создание новой ветки (туда копируется текущая):
```sh
git branch new_branch_name # Новая ветка создается от текущей
git push origin new_branch_name # Залить ее в удаленный репозиторий
```
Удаление ветки:
```sh
git branch -d branch_name # Удалить локальную ветку
git branch -D branch_name # Удалилить локальную ветку, даже если запрещает
git push origin --delete branch_name # Удалить удаленную ветку
```
### Коммиты
Коммит - это пакет изменений, который был внесен в ветку. Без объединения изменений в коммит они никак не учитываются.
После того как вы изменяли файлы, их необходимо добавить в коммит:
```sh
git add file_name # Добавить отдельный файл
git add directory_name # Добавить файлы в каталоге
git add . # Добавить все файлы в этом каталоге
git rm file_name # Удалить отдельный файл
```
Создание коммита:
```sh
git commit -m "Название коммита"
```
Отправить коммит в удаленный репозиторий:
```sh
git push origin branch_name
git push # Если установлена ветка по умолчанию
git push --set-upstream origin branch_name # Установка ветки по умолчанию 
```
### Загрузка из удаленного репозитория
Загрузить содержимое из репозитория:
```sh
git pull origin branch_name
git pull # Если установлена ветка по умолчанию
git push --set-upstream origin branch_name # Установка ветки по умолчанию 
```
Если вы хотите слить две ветки (текущую и branch2), то используйте:
```sh
git merge branch2
```
Для слияния необходимо, чтобы версии веток были последними, если это не так, нужно сделать pull изменений. Если много людей работают с одной веткой, то это также необходимо.

Могут возникнуть конфликты, их необходимо решить мануально, отредактировав файлы (там описываются все изменения). Потом сделайте add и commit.

Можно последовательно перенести коммиты из одной ветки в другую, начиная от ближайшего к их общему предку. Каждый перенесенный коммит становится новым коммитом в ветке, в которую выполняется перенос. Эта операция выполняется с помощью:
```sh
git rebase branch_2 # Переносим коммиты из текущей ветки в branch_2
```
На каждом перенесенном коммите могут возникнуть конфликты.
### Откат изменений
Чтобы посмотреть историю коммитов, используйте:
```sh
git log --oneline
```
На экран будут выведены список из кодов коммитов и их описание.
Можно переключиться на старую версию с помощью checkout на код коммита:
```sh
git checkout a1e8fb5
git checkout some_branch # на последнюю версию
```
Оттуда можно создать новую ветку. Изменения в новой ветке не учитываются, если вы работаете не в последней версии.
Если необходимо полностью откатиться к предыдущей версии:
```sh
git revert HEAD # Отменяет последний коммит
git revert a1e8fb5 # Отменяет коммит по его коду
```
Можно откатиться к версии по коду коммита, но работает только если все коммиты локальные:
```sh
git reset --hard a1e8fb5 
```

### Игнорирование файлов
Вы можете создать файл .gitignore и прописать там список файлов, которые не требуется коммитить. Они будут игнорироваться при попытки их добавить.
