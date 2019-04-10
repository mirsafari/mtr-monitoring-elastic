FROM alpine
RUN apk add --no-cache mtr python3 netcat-openbsd
COPY ./scripts /scripts
RUN chmod 700 /scripts/*
CMD ["/scripts/mtr-agent.sh"]
