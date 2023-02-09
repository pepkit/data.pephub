FROM databio/pephub:latest
COPY peps/ /app/peps/
COPY config.yaml /app
COPY schemas.yaml /app
RUN mkdir /app/uploads
ENTRYPOINT [ "pephub", "serve", "--port", "80" ]
