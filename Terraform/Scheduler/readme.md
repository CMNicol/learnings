1. Deploy Infrastructure  
2. Upload Docker image to repository  
3. Run ECS Task  


# Run the script locally
```sh
chmod +x processA.sh
./processA.sh
```  

# Build Docker image locally
Create image named `jobs-image`.  
Run this image with a command which will run the script.  
```sh
docker build . -t jobs-image
docker run --name jobs-container jobs-image /script/processA.sh
```
Cleanup
```sh
docker rm jobs-container
docker rmi jobs-image
```

https://aws.amazon.com/blogs/containers/migrate-cron-jobs-to-event-driven-architectures-using-amazon-elastic-container-service-and-amazon-eventbridge/  

https://dev.to/erozedguy/ci-cd-pipeline-for-amazon-ecs-fargate-with-terraform-33na  

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html  

https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html