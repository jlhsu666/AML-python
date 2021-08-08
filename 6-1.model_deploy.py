from azureml.core import Workspace
ws = Workspace.from_config()

# Register a model from a local file

import urllib.request
from azureml.core.model import Model

# Download model
urllib.request.urlretrieve("https://aka.ms/bidaf-9-model", "model.onnx")

# Register model
model = Model.register(ws, model_name="bidaf_onnx", model_path="./model.onnx")
print(model.name, model.id, model.version, sep='\t')

# Define a dummy entry script
# The entry script receives data submitted to a deployed web service and passes it to the model. 
# It then returns the model's response to the client. 

# The script is saved in dirctory ./src as echo_score.py, which will be upploaded when you deploy a webservice

# Define an inference configuration
from azureml.core import Environment
from azureml.core.model import InferenceConfig

env = Environment(name="project_environment")
dummy_inference_config = InferenceConfig(
    environment=env,
    source_directory="./src",
    entry_script="./echo_score.py",
)

# Define a deployment configuration
from azureml.core.webservice import LocalWebservice

deployment_config = LocalWebservice.deploy_configuration(port=6789)

# Deploy your machine learning model
service = Model.deploy(
    ws,
    "myservice",
    [model],
    dummy_inference_config,
    deployment_config,
    overwrite=True,
)
service.wait_for_deployment(show_output=True)
print(service.get_logs())

