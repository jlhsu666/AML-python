from azureml.core.model import InferenceConfig, Model
from azureml.core.webservice import AciWebservice, Webservice
from azureml.core import Workspace
from azureml.core.environment import Environment
from azureml.core import Model

ws = Workspace.from_config()

# Register the model to deploy
model = Model.register(ws, model_name="bidaf_onnx", model_path="./model.onnx")

myenv = Environment(name="project_environment")
# Combine scoring script & environment in Inference configuration
inference_config = InferenceConfig(entry_script="./src/echo_score.py", environment=myenv)

# Set deployment configuration
deployment_config = AciWebservice.deploy_configuration(cpu_cores = 1, memory_gb = 1)

# Define the model, inference, & deployment configuration and web service name and location to deploy
service = Model.deploy(
    ws,
    "my-web-service",
    [model],
    inference_config,
    deployment_config)