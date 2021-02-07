
# MySQL Note

### TEST ENV
```
OS : Ubuntu 20.04
```

### Quick Start Support Link
 - 1.Docker && Docker MySQL Install 
   - http://jmlim.github.io/docker/2019/07/30/docker-mysql-setup/

 - 2.Sample SQL File
   - https://www.mysqltutorial.org/mysql-sample-database.aspx/

 - 3.SQL IMPORT
   - https://kssong.tistory.com/2

### Installation
```
$ apt update

$ apt install wget

$ apt install unzip
```

### MYSQL USER:PASSWORD SETTING
```
sudo docker run -d -it -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 --name {HOSTNAME} {IMAGE_ID} /bin/bash
```

### EXTERNAL ACCESS SETTING
```
1. mysql -u root -p

2. CREATE USER 'root'@'%' IDENTIFIED BY '1234';

3. GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';

4. flush privileges;
```

### Support Link
 - Basic
   - https://eunice513.tistory.com/108
