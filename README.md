
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


---
---

# Jenkins Freestyle Job for Dockerized Flask/FastAPI Application

This repository contains the instructions to set up a Jenkins freestyle job to pull the Dockerized Flask/FastAPI application from a Git repository and launch it on port 5003.

## Prerequisites

- Jenkins installed and running on an Azure Linux virtual machine
- Access to the Git repository containing the Dockerized application
- Docker installed on the Jenkins machine

## Steps

### 1. Jenkins Setup

#### 1.1 Install Jenkins

If Jenkins is not already installed, follow these steps to install it:

```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

#### 1.2 Configure Jenkins

1. Access Jenkins at `http://<jenkins-vm-ip>:8080` and complete the setup wizard.
2. Install necessary plugins:
   - Git plugin
   - Docker plugin

#### 1.3 Connect Jenkins to Git Repository

1. Go to `Manage Jenkins` > `Manage Credentials` and add your Git credentials.
2. Go to `Manage Jenkins` > `Global Tool Configuration` and configure Git by specifying the path to the Git executable.

### 2. Create Freestyle Job

1. **Create a New Job**:
   - Go to Jenkins dashboard.
   - Click on `New Item`.
   - Enter an item name (e.g., `DockerizedAppPullAndRun`).
   - Select `Freestyle project` and click `OK`.

2. **Build Triggers**:
   - Configure build triggers as needed, such as `Poll SCM` to periodically check for changes in the Git repository.

3. **Build Steps**:
   - Add a build step to execute shell commands:
     ```sh
     # Pull the latest changes
     git pull <repository-url>

     # Build the Docker image
     docker build -t <your-dockerhub-username>/<your-image-name> .

     # Stop and remove any running container of the same name
     docker stop my_docker_app || true && docker rm my_docker_app || true

     # Run the Docker container on port 5003
     docker run -d -p 5003:5000 --name my_docker_app <your-dockerhub-username>/<your-image-name>
     ```

4. **Save and Run the Job**:
   - Click `Save`.
   - Build the job manually to ensure everything is set up correctly.

### 3. Verify the Setup

1. Make changes to the Git repository to update the application (e.g., modify a route or template).
2. Push the changes to the repository.
3. Trigger the Jenkins job manually or wait for the automated trigger.
4. Access the application at `http://<jenkins-vm-ip>:5003` to ensure the changes are reflected.

## Conclusion

You have successfully set up a Jenkins freestyle job to pull the Dockerized Flask/FastAPI application from a Git repository and launch it on port 5003. This setup ensures that any changes made to the repository are automatically deployed via Jenkins.

For any issues or contributions, please open an issue or submit a pull request.

---

Replace `<jenkins-vm-ip>`, `<your-dockerhub-username>`, and `<your-image-name>` with the appropriate values specific to your Jenkins VM, Docker Hub username, and Docker image name.
