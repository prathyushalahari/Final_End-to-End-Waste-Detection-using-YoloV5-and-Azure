#End-to-End-Waste-Detection-using-YoloV5-and-Azure

Author : M Prathyusha Lahari


This is end to end azure waste object detection deployment

## Workflows- files to be worked
1. constant
1. constant
2. entity
3. components
4. pipelines
5. app.py

# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+XXXXXX


## Run from terminal:

docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 
