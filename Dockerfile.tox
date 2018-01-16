FROM ubuntu:16.04

ENV PYENV_REQUIRED_PYTHON_BASENAME python_versions.txt
ENV PYENV_REQUIRED_PYTHON /pyenv/$PYENV_REQUIRED_PYTHON_BASENAME

ENV PYENV_ROOT /pyenv/
ENV PATH /pyenv/shims:/pyenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN apt-get update -q -y
RUN apt-get install --no-install-recommends --fix-missing -y \
    build-essential \
    libssl-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    curl \
    git \
    make \
    locales \
    python-pip \
    && apt-get autoremove -y \
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install --upgrade tox tox-pyenv

RUN curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

COPY $PYENV_REQUIRED_PYTHON_BASENAME $PYENV_REQUIRED_PYTHON

RUN while read line; do \
    pyenv install $line || exit 1 ;\
    done < $PYENV_REQUIRED_PYTHON


RUN pyenv global system `cat $PYENV_REQUIRED_PYTHON | tr '\n' ' '`
RUN pyenv local `cat $PYENV_REQUIRED_PYTHON | tr '\n' ' '`

WORKDIR /app

COPY . /app/

CMD ["tox"]
