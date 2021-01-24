
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

### Quick Start
```
1. sudo docker run -d -it -p 3306:3306 -e MYSQL_ROOT_PASSWORD=1234 --name root {CONTAINER_ID} /bin/bash

2. mysql -u root -p

3. CREATE USER 'root'@'%' IDENTIFIED BY '1234';

4. GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';

5. flush privileges;
```

### Support Link
 - Basic
   - https://eunice513.tistory.com/108
