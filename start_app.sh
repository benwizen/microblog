#/bin/sh
docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY='#' \
    -e MAIL_SERVER='#' -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME='#' -e MAIL_PASSWORD='#' \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://microblog:<password>@dbserver/microblog \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    microblog:latest
