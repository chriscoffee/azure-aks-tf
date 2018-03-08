import unittest
from runner import Runner


class TestE2E(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.snippet = """

            provider "azurerm" {
              subscription_id = "null"
              client_id = "null"
              client_secret = "null"
              tenant_id = "null"
              skip_credentials_validation = true
            }

            module "aks" {
            
              source = "./mymodule"

              resource_group {
                name = "aks_prod_rg"
              }

              location = "UK South"
              
              kubernetes_cluster {
                name = "aks_prod_kc"
                version = "1.10"
                dns_prefix = "acidburn"
              }
              
              admin_credentials {
                username = "chris"
                ssh_key = "null"
              }
              
              agent_pool_profile {
                name = "aks_prod_app"
                count = "1"
                vm_size = "Standard_F1"
                os_type = "Linux"
              }
              
              service_principal {
                client_id = "correct-horse-battery-staple"
                client_secret = "correct-horse-battery-staple"
              }

              environment = "production"
            }
        """
    self.result = Runner(self.snippet).result

  def test_root_destroy(self):
    self.assertEqual(self.result["destroy"], False)
    self.assertEqual(self.result["aks"]["destroy"], False)

  def test_azurerm_kubernetes_cluster(self):
    self.assertIn("azurerm_resource_group.aks_rg", self.result["aks"])

  def test_azurerm_resource_group_name(self):
    self.assertEqual("aks_prod_rg", self.result["aks"]["azurerm_resource_group.aks_rg"]["name"])

  def test_azurerm_location(self):
    self.assertEqual("uksouth", self.result["aks"]["azurerm_resource_group.aks_rg"]["location"])

  def test_azurerm_kubernetes_cluster(self):
    self.assertIn("azurerm_kubernetes_cluster.aks_kc", self.result["aks"])

  def test_azurerm_kubernetes_cluster_name(self):
    self.assertEqual("aks_prod_kc", self.result["aks"]["azurerm_kubernetes_cluster.aks_kc"]["name"])

  def test_azurerm_kubernetes_cluster_kuberentes_version(self):
    self.assertEqual("1.10", self.result["aks"]["azurerm_kubernetes_cluster.aks_kc"]["kubernetes_version"])

  def test_azurerm_kubernetes_cluster_dns_prefix(self):
    self.assertEqual("acidburn", self.result["aks"]["azurerm_kubernetes_cluster.aks_kc"]["dns_prefix"])

  def test_azurerm_kubernetes_cluster_admin_username(self):
    self.assertEqual("chris", self.result["aks"]["azurerm_kubernetes_cluster.aks_kc"]["linux_profile.0.admin_username"])

  def test_azurerm_kubernetes_cluster_agent_pool_profile_name(self):
    self.assertEqual("aks_prod_app", self.result["aks"]["azurerm_kubernetes_cluster.aks_kc"]["agent_pool_profile.0.name"])

  def test_azurerm_kubernetes_cluster_agent_pool_profile_count(self):
    self.assertEqual("1", self.result["aks"]["azurerm_kubernetes_cluster.aks_kc"]["agent_pool_profile.0.count"])

  def test_azurerm_kubernetes_cluster_agent_pool_profile_vm_size(self):
     self.assertEqual("Standard_F1", self.result["aks"]["azurerm_kubernetes_cluster.aks_kc"]["agent_pool_profile.0.vm_size"])

  def test_azurerm_kubernetes_cluster_agent_pool_profile_os_type(self):
     self.assertEqual("Linux", self.result["aks"]["azurerm_kubernetes_cluster.aks_kc"]["agent_pool_profile.0.os_type"])



if __name__ == '__main__':
  unittest.main()
