FROM python:3.9.6
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install transformers==4.25.1
RUN python -m pip install torch===1.9.0 
RUN python -m pip install torchvision===0.10.0 
RUN python -m pip install torchaudio===0.9.0
RUN python -m pip install fugashi==1.2.1
RUN python -m pip install ipadic==1.0.0
RUN python -m pip install matplotlib==3.6.2

