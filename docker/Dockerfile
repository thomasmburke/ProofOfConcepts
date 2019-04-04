FROM python:3-alpine
RUN python -m pip install --upgrade pip
COPY ./ /
RUN pip install -r requirements.txt
WORKDIR /
ENTRYPOINT [ "python3" ]
CMD [ "facebook_scraper.py" ]
