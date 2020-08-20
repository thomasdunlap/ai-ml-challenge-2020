FROM ubuntu:18.04

ARG USERNAME=imagemagick

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

RUN apt-get update -y
RUN apt-get install -y python3.7 python3-pip build-essential && \
    apt-get install python3-venv -y

RUN python3 -m venv /venv
RUN which python3.7


RUN apt-get update -yqq && \
apt-get install -yqq \
apt-utils ca-certificates

RUN apt-get install -yqq locales && locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN apt-get install -yqq imagemagick
ADD fixpolicy.sh /
RUN /fixpolicy.sh && rm /fixpolicy.sh

RUN apt-get clean && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt /requirements.txt

RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install numpy==1.18.5
RUN /venv/bin/pip install -r requirements.txt


RUN mkdir -p /workdir && \
chmod -R a+rwX /workdir


RUN useradd -ms /bin/bash ${USERNAME}
USER ${USERNAME}



WORKDIR /workdir



COPY UI_Upgrade_V1 /workdir

VOLUME ["/workdir"]

ENTRYPOINT ["python3"]

CMD ["run.py"]
