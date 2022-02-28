FROM python

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py

EXPOSE 80

CMD python app.py