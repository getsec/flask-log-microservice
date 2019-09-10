# This is wayyyy smaller that wsgi one or alpine linux
FROM python:3.7-alpine

# Copy everything into an app folder
COPY . /app    

# Switch to the app directory
WORKDIR /app

# Install the requiremnets
RUN pip install -r requirements.txt

# Periodically run a health check and ensure the endpoint responds
HEALTHCHECK --interval=12s --timeout=12s --start-period=30s \  
 CMD curl localhost:8001

# Launch python with app.py
ENTRYPOINT ["python"]

CMD ["app.py"]