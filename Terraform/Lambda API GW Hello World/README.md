https://developer.hashicorp.com/terraform/tutorials/aws/lambda-api-gateway

```sh
aws s3 ls $(terraform output -raw lambda_bucket_name)
```

```sh
aws lambda invoke --region=eu-west-1 --function-name=$(terraform output -raw function_name) response.json
```

```sh
curl "$(terraform output -raw base_url)/hello"
```

```sh
curl "$(terraform output -raw base_url)/hello?Name=Terraform"
```