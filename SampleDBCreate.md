# Sample DataBase Create
```
@ DataBase : Postgresql
@ target OS : ubuntu 20.04

@ Sample Data Link : https://sp.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip
@ Usage : wget {SAMPLE_DATA_LINK}
```

## Install Postgresql
```
sudo apt-get install postgresql postgresql-contrib
```

## Switch User
```
sudo -i -u postgres
```

## Create DataBase
```
create database dvdrental;
```

## Restore DataBase
```
pg_restore -h localhost -U postgres -C -d dvdrental -F t dvdrental.tar
```
