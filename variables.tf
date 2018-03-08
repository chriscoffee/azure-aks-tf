variable "resource_group" {
  description = "Specifies the resource group where the resource exists. Changing this forces a new resource to be created."
  type        = "map"
}

variable "location" {
  description = "The location where the AKS Managed Cluster instance should be created. Changing this forces a new resource to be created."
}

variable "kubernetes_cluster" {
  description = "The map for the configuration of the kubernetes cluster"
  type        = "map"
  /*
    default = {
      name = ""
      version = "" # Version of Kubernetes specified when creating the AKS managed cluster.
      dns_prefix = "" # DNS prefix specified when creating the managed cluster.
    }
  */
}

variable "admin_credentials" {
  description = "The Admin Username for the Cluster. Changing this forces a new resource to be created."
}

variable "agent_pool_profile" {
  description = "The map for the configuration of the kubernetes cluster"
  type        = "map"
  /*
    default = {
      name = "" # Unique name of the Agent Pool Profile in the context of the Subscription and Resource Group.
      count = "" # Number of Agents (VMs) in the Pool. Possible values must be in the range of 1 to 50 (inclusive). Defaults to 1.
      vm_size = "" # The size of each VM in the Agent Pool (e.g. Standard_F1)
      os_type = "" # The Operating System used for the Agents. Possible values are Linux and Windows. Defaults to Linux.
      vnet_subnet_id = "" # The ID of the Subnet where the Agents in the Pool should be provisioned.0
    }
  */
}

variable "service_principal" {
  description = "The map for the configuration of the service principal"
  type        = "map"
  /*
    default = {
      client_id = "" # (Required) The Client ID for the Service Principal.
      client_secret = "" # (Required) The Client Secret for the Service Principal.
    }
  */
}

variable "environment" {
  description = "The environment of the cluster"
}
