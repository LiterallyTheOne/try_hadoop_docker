FROM bde2020/hadoop-namenode

WORKDIR /app

RUN rm /etc/apt/sources.list

RUN echo "deb http://archive.debian.org/debian-security stretch/updates main" >> /etc/apt/sources.list.d/stretch.list

RUN echo "deb http://archive.debian.org/debian stretch main" >> /etc/apt/sources.list.d/stretch.list

RUN apt update -y
RUN apt install python -y

COPY . .

CMD ["/run.sh"]
