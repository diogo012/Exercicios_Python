FROM python:3.12.2-slim

WORKDIR /app

# install nodemon
RUN apt update
RUN apt install curl -y
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash
RUN apt install nodejs -y
RUN npm install -g npm@9.2.0
RUN npm install -g nodemon

# upgrade pip
RUN python -m pip install --upgrade pip

# dependencies from requirements.txt
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py