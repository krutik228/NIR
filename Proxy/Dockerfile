# базовый образ на основе Ubuntu 20.04
FROM ubuntu:20.04

# отключение интерактивного режима, для принятия решений по умолчанию
# например для установки таймзоны для пакета tzdata, т.к. он просит ввести её с консоли
ENV DEBIAN_FRONTEND=noninteractive

# установка pip
RUN apt-get update && apt-get install -y python3 python3-pip

# установка Flask и зависимостей
RUN pip3 install Flask

# установка и настройка WordPress
RUN apt-get install -y wordpress

# копирование конфигурационных файлов
COPY entrypoint.sh /

# открытие порта 80
EXPOSE 80

# делаем entrypoint.sh исполняемым
RUN chmod +x /entrypoint.sh

# запуск скрипта entrypoint.sh при запуске контейнера
ENTRYPOINT ["/entrypoint.sh"]
