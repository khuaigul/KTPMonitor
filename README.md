# KTPMonitor4

sudo apt install git
ssh-keygen -t ed25519 -C "your_email@example.com"
git clone git@github.com:khuaigul/KTPMonitor4.git

-------------------------------------------
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update

python3

----------------

sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation

Error: SET PASSWORD has no significance for user 'root'@'localhost' as the authentication method used doesn't store authentication data in the MySQL server. Please consider using ALTER USER instead if you want to change authentication parameters.

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
--------------------------------------------------

visual studio code
-------------------------------------------------
sudo apt install python3-pip
pip install mysql-connector-python
pip install django

--------------------------------------------
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter
------------------
python manage.py migrate


--------------
CREATE DATABASE KTP_Monitor;
