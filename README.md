Инструкция по git
=================
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
Для слияния необходимо, чтобы версии веток были последними, если это не так нужно сделать pull изменений. Если много людей работают с одной веткой, то это также необходимо.
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
