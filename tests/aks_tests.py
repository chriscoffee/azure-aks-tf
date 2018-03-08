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
                name = "aks_prod_kc
                kubernetes_version = "1.10"
                dns_prefix = "acidburn"
              }
              
              admin_credentials {
                username = "chris"
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
        self.assertEqual(self.result["aci"]["destroy"], False)

    def test_azurerm_resource_group_name(self):
        self.assertEqual("aks_prod_rg", self.result["aks"]["azurerm_resource_group.aks_rg"]["name"])

if __name__ == '__main__':
    unittest.main()
