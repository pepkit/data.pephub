FROM databio/pephub:latest
COPY . /app/data
ENTRYPOINT [ "pephub", "serve", "-c", "config.yaml" ]