https://developer.hashicorp.com/terraform/tutorials/modules/module-create

```sh
aws s3 cp modules/aws-s3-static-website-bucket/www/ s3://$(terraform output -raw website_bucket_name)/ --recursive
```

```sh
aws s3 rm s3://$(terraform output -raw website_bucket_name)/ --recursive
```