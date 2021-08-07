from azureml.core import Workspace

ws = Workspace.from_config()
print(ws.name)

# Clean workspace
# ws.delete(delete_dependent_resources=False, no_wait=False)