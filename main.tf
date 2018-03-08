resource "azurerm_resource_group" "aks_rg" {
  name     = "${var.resource_group["name"]}"
  location = "${var.location}"
}

resource "azurerm_kubernetes_cluster" "aks_kc" {
  name                = "${var.kubernetes_cluster["name"]}"
  location            = "${azurerm_resource_group.aks_rg.location}"
  resource_group_name = "${azurerm_resource_group.aks_rg.name}"
  kubernetes_version  = "${var.kubernetes_cluster["version"]}"
  dns_prefix          = "${var.kubernetes_cluster["dns_prefix"]}"

  linux_profile {
    admin_username = "${var.admin_credentials["username"]}"

    ssh_key {
      key_data = "${var.admin_credentials["ssh_key"]}"
    }
  }

  agent_pool_profile {
    name    = "${var.agent_pool_profile["name"]}"
    count   = "${var.agent_pool_profile["count"]}"
    vm_size = "${var.agent_pool_profile["vm_size"]}"
    os_type = "${var.agent_pool_profile["os_type"]}"
  }

  service_principal {
    client_id     = "${var.service_principal["client_id"]}"
    client_secret = "${var.service_principal["client_secret"]}"
  }

  tags {
    environment = "${var.environment}"
  }
}
