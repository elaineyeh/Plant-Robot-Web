FROM python:3.7

RUN apt-get update && apt-get install -y \
  gcc \
  musl \
  default-libmysqlclient-dev


WORKDIR /app

# Install required package
RUN pip3 install -U --no-cache-dir gunicorn pip setuptools

# Install pip 
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Set port
EXPOSE 80

COPY . .

# Run
CMD ["gunicorn", "--workers", "2", "--bind", ":80", "--log-level", "INFO", \
     "core.wsgi:application"]