# tutorial/01-create-workspace.py
from azureml.core import Workspace

ws = Workspace.create(name='tutorial_python', # provide a name for your workspace
                      subscription_id='06863575-f2fe-45dc-a86d-6395a9cfe972', # provide your subscription ID
                      resource_group='azure_python', # provide a resource group name
                      create_resource_group=True,
                      location='westeurope') # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')