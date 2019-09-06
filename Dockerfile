FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

HEALTHCHECK --interval=12s --timeout=12s --start-period=30s \  
 CMD python healthcheck.py

ENTRYPOINT ["python"]

CMD ["app.py"]