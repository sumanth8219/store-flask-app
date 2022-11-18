### Developer guide

[Setting up docker on WSL2](https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9)

#### Start docker on wsl2 Ubuntu
```dotnetcli
sudo dockerd
```
#### Build Docker image
```bash
docker build -t rest-apis-flask-python .
```

#### Start a docker for local development
```bash
docker run -d --network host -w /app -v "$(pwd):/app" rest-apis-flask-python
```