FROM nikolaik/python-nodejs:python3.6-nodejs14-stretch

RUN cd /home/ && \
    git clone -b feature/level_predict https://github.com/magic929/starlightrelive.git

ENV HOME=/home/starlightrelive
COPY ./starlightRe.db $HOME/

RUN cd $HOME/ && pip3 install -r requirements.txt && \
    cd $HOME/frontend/ && \ 
    npm install && \
    npm run build && \
    cd $HOME/backend/ && python main.py