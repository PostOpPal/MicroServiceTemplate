sudo apt-get install libmysqlclient-dev
mysql -u root -p < ./schema.sql
sqlacodegen mysql://root:root@localhost/templatedatabase > ./models.py