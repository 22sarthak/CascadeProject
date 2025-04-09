# Flask DevOps Demo

A simple Flask REST API with Docker containerization and automated deployments.

## Features

- Health check endpoint (`/health`)
- Hello world endpoint (`/api/v1/hello`)
- Version info endpoint (`/api/v1/version`)
- Rotating log files
- Docker containerization
- Automated builds via GitHub Actions

## Local Development

1. Build the Docker image:
```bash
docker build -t sarthak273a/flask-app .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 --name flask-app sarthak273a/flask-app
```

3. Test the endpoints:
```bash
curl http://localhost:5000/health
curl http://localhost:5000/api/v1/hello
curl http://localhost:5000/api/v1/version
```

## CI/CD Pipeline

The application uses GitHub Actions for continuous integration and deployment:

1. On push to main branch:
   - Builds Docker image
   - Pushes to Docker Hub
   - Tags with both latest and commit SHA

## Docker Hub

The Docker image is available at: `sarthak273a/flask-app`

To pull the latest version:
```bash
docker pull sarthak273a/flask-app:latest
```

## Environment Variables

- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Docker Hub access token (for CI/CD)
