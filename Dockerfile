FROM python:3.7.1-alpine3.8 as base

# FROM base as builder
# RUN mkdir /install
# WORKDIR /install

# COPY requirements.txt /requirements.txt
# RUN pip install --install-option="--prefix=/install" -r /requirements.txt


# FROM base
# COPY --from=builder /install /usr/local

# COPY . /app
# WORKDIR /app
# EXPOSE 5000

#4 worker threads, listening on 5000
#CMD ["gunicorn","app:app" "-b", ":8000", "-w 4"]

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

CMD ["python", "app.py"]