# базовый образ на основе Ubuntu 20.04
FROM ubuntu:20.04

# отключение интерактивного режима, для принятия решений по умолчанию
# например для установки таймзоны для пакета tzdata, т.к. он просит ввести её с консоли
ENV DEBIAN_FRONTEND=noninteractive

# установка пакетов системы
RUN apt-get update  &&  \
    apt-get install -y python3 python3-pip

# установка и настройка MySQL
RUN apt-get install -y mysql-server mysql-client && \
    service mysql start && \
    mysql -e "CREATE DATABASE testdb;" && \
    mysql -e "CREATE USER 'admin'@'localhost' IDENTIFIED BY 'P@ssw0rd';" && \
    mysql -e "GRANT ALL PRIVILEGES ON testdb.* TO 'admin'@'localhost';" && \
    mysql -e "FLUSH PRIVILEGES;" && \
    mysql -e "USE testdb; CREATE TABLE users (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), last_name VARCHAR(255), PRIMARY KEY (id));" && \
    service mysql stop

# установка Flask и зависимостей для работы с MySQL
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

COPY entrypoint.sh /

# копирование приложения Flask
COPY app app/

# открытие порта 443
EXPOSE 443

# делаем entrypoint.sh исполняемым
RUN chmod +x /entrypoint.sh

# запуск скрипта entrypoint.sh при запуске контейнера
ENTRYPOINT ["/entrypoint.sh"]