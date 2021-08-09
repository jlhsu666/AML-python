from azureml.core import Workspace

ws = Workspace.create(name='ws-vsc0809',
               subscription_id='961985cd-58cf-4a54-9a72-5fb6dad0511c',
               resource_group='rg-vsc0809',
               create_resource_group=True,
               location='eastus2'
               )

ws.write_config()

# Clean workspace
# ws.delete(delete_dependent_resources=False, no_wait=False)