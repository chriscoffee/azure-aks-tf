# azure-dk-tf

This is a terraform module that creates an AKS cluster on Azure and controls its deployment through Terraform.

### main.tf

The file contains the components for creating the cluster
- The resource group
- One kubernetes cluster hosted on AKS

### outputs.tf

Outputs we can take from the module

### variables.tf

Input data mostly in map format as I have a weird preference to this.

### tests/aks_test.py

Code for testing module

## Depdendencies

- drone
- terraform
- python

## How to run tests and deploy

`drone exec` will run the tests

`terraform plan` and `terraform apply` will deploy the cluster
