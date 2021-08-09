# Deploy to AKS
from azureml.core.webservice import AksWebservice, Webservice
from azureml.core.model import Model

aks_target = AksCompute(ws,"myaks")
# If deploying to a cluster configured for dev/test, ensure that it was created with enough
# cores and memory to handle this deployment configuration. Note that memory is also used by
# things such as dependencies and AML components.
deployment_config = AksWebservice.deploy_configuration(cpu_cores = 1, memory_gb = 1)
service = Model.deploy(ws, "myservice", [model], inference_config, deployment_config, aks_target)
service.wait_for_deployment(show_output = True)
print(service.state)
print(service.get_logs())

# # Create an endpoint
# import azureml.core,
# from azureml.core.webservice import AksEndpoint
# from azureml.core.compute import AksCompute
# from azureml.core.compute import ComputeTarget
# # select a created compute
# compute = ComputeTarget(ws, 'myaks')

# # define the endpoint and version name
# endpoint_name = "mynewendpoint"
# version_name= "versiona"
# # create the deployment config and define the scoring traffic percentile for the first deployment
# endpoint_deployment_config = AksEndpoint.deploy_configuration(cpu_cores = 0.1, memory_gb = 0.2,
#                                                               enable_app_insights = True,
#                                                               tags = {'sckitlearn':'demo'},
#                                                               description = "testing versions",
#                                                               version_name = version_name,
#                                                               traffic_percentile = 20)
#  # deploy the model and endpoint
#  endpoint = Model.deploy(ws, endpoint_name, [model], inference_config, endpoint_deployment_config, compute)
#  # Wait for he process to complete
#  endpoint.wait_for_deployment(True)