FROM python:3.7-alpine3.7
LABEL version="1.0.0"
LABEL author="Vinícius"
ENV ACCESS_COUNTER_PORT 8080
ENV ACCESS_COUNTER_DEBUG False
ENV ACCESS_COUNTER_LOG_FILE /var/log/access_log
ENV ACCESS_COUNTER_COUNT_FILE /etc/access_counter/count
EXPOSE $ACCESS_COUNTER_PORT
VOLUME /var/log
COPY . /access_counter
WORKDIR /access_counter
RUN pip install -r requirements.txt &&\
    mkdir /etc/access_counter
ENTRYPOINT ["gunicorn"]
CMD ["--chdir", "src", "app:app", "-b", ":8080"]
