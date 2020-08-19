FROM ubuntu:18.04

ARG USERNAME=imagemagick

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

RUN apt-get update -y
RUN apt-get install -y python3.7 python3-pip python3-venv build-essential

RUN apt-get update -yqq && \
apt-get install -yqq \
apt-utils ca-certificates

RUN apt-get install -yqq locales && locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN apt-get install -yqq imagemagick
ADD fixpolicy.sh /
RUN /fixpolicy.sh && rm /fixpolicy.sh

RUN apt-get clean && rm -rf /var/lib/apt/lists/*


RUN mkdir -p /workdir && \
chmod -R a+rwX /workdir


RUN useradd -ms /bin/bash ${USERNAME}
USER ${USERNAME}



WORKDIR /workdir

COPY ./requirements.txt /workdir/requirements.txt

RUN python3.7 -m venv env
RUN source env/bin/activate
RUN pip install --upgrade pip
RUN pip install numpy==1.18.5
RUN pip install -r requirements.txt


COPY UI_Upgrade_V1 /workdir

VOLUME ["/workdir"]

ENTRYPOINT ["python3"]

CMD ["run.py"]
