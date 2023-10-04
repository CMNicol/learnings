Code adapted from [AWS-CDK-in-Practice](https://github.com/PacktPublishing/AWS-CDK-in-Practice/tree/main).  
Book [here](https://www.packtpub.com/product/aws-cdk-in-practice/9781801812399).  

# Full Stack App
* ECS/Fargate, S3, DynamoDB  
* Flask BE served through ALB, ECS Task  
* React FE served through S3  


# Set Up Python Virtual Environment
Starting point: inside `full_stack/`.  
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r infrastructure/requirements.txt
pip install -r server/requirements.txt
```  

# Building Frontend App
Starting point: inside `full_stack/`.  
```sh
cd web
yarn
yarn build
```  
Will need to replace the `backend_url` with the ALB endpoint.  

# Deploying Infra
Starting point: inside `full_stack/`.  
```sh
cd infrastructure
cdk synth
cdk deploy --profile <profile>
```  

## How is the task run? 
What handles "kicking off" the app? How does container get run?  

## Destroying Infra
```sh
cdk destroy
```  
