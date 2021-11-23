FROM databio/pephub:latest
COPY peps/ /app/data/
ENTRYPOINT [ "pephub", "serve", "-c", "config.yaml" ]