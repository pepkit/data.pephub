FROM databio/pephub:latest
COPY . /app
ENTRYPOINT [ "pephub", "serve", "-c", "config.yaml" ]