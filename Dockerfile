FROM databio/pephub:latest
COPY peps/ /app/peps/
COPY config.yaml /app
COPY schemas.yaml /app

ENTRYPOINT [ "pephub", "serve", "-c", "config.yaml" ]