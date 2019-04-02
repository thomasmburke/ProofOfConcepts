FROM python:3-alpine
RUN python3 -m pip install --upgrade pip
COPY ./ /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]
