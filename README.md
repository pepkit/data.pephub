# pephub.databio.org
This is the publically available instance of [PEPhub](https://github.com/pepkit/pephub) provided by the Sheffield lab. You can view the deployed instance at https://pephub.databio.org

## Development
### Build the container
```
docker build -t pephub.databio.org .
```

### Launch
PEPhub requires many parameters to run. You can read more about those [here](https://github.com/pepkit/pephub/blob/master/docs/server-settings.md). These must be injected as environment variables. You can manually do this and inject one-by-one. There is an example script in this repo called [launch_docker.sh](launch_docker.sh).

 ```
 launch_docker.sh
 ```
