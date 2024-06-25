
# Dockerized Flask/FastAPI Application

This repository contains a Dockerized Flask/FastAPI application with a MongoDB database, managed using Docker Compose.

## Prerequisites
- Virtual machine on Microsoft Azure
- Docker installed on that machine
- Docker Compose installed on that machine

## Repository Structure

```
.
├── template/                    
│  └── index.html             
├── .gitignore             
├── app.py              
├── config.py
├── models.py      
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md            
```

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Build the Docker Image

Navigate to the root directory of the cloned repository and build the Docker image using the Dockerfile.

```bash
docker build -t <your-dockerhub-username>/<your-image-name> .
```

### 3. Run the Docker Container

To run the Docker container and ensure the application works correctly inside the container, use the following command:

```bash
docker run -p 8000:8000 <your-dockerhub-username>/<your-image-name>
```

You should now be able to access the application at `http://localhost:8000`.

### 4. Using Docker Compose

To use Docker Compose for managing multiple services (application and MongoDB database), follow these steps:

#### 4.1 Create a `docker-compose.yml` file

The `docker-compose.yml` file should look something like this:

```yml
version: '3.8'

services:
  mongo:
    image: mongo:latest
    container_name: mongo
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db

  web:
    build: .
    container_name: flask-app
    command: flask run --host=0.0.0.0
    volumes:
      - .:/app
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - MONGO_URI=mongodb://mongo:27017/flaskdb
    depends_on:
      - mongo

volumes:
  mongo-data:

```

#### 4.2 Start the services

Run the following command to start the services defined in the `docker-compose.yml` file:

```bash
docker-compose up --build
```

The application will be accessible at `http://localhost:8000`, and the MongoDB database will be running in the background.

### 5. Push the Docker Image to Docker Hub

Tag the Docker image and push it to Docker Hub.

```bash
docker tag <your-dockerhub-username>/<your-image-name>:latest <your-dockerhub-username>/<your-image-name>:v1.0
docker push <your-dockerhub-username>/<your-image-name>:v1.0
```

## Conclusion

You have successfully containerized a Flask/FastAPI application using Docker and Docker Compose. You can now build, run, and manage the application and its dependencies efficiently using Docker.

For any issues or contributions, please open an issue or submit a pull request.

---

Replace `<repository-url>`, `<repository-directory>`, `<your-dockerhub-username>`, and `<your-image-name>` with the appropriate values specific to your repository and Docker Hub account.
