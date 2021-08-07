from azureml.core import Experiment
from azureml.core import Workspace

ws = Workspace.from_config()

# Create an experiment in your workspace.
experiment_name = 'my_experiment'
experiment = Experiment(workspace=ws, name=experiment_name)

# Select a compute target

# Create an environment where the script will run 1.local compute target or 2. remote compute target
from azureml.core import Environment

myenv = Environment.get(workspace=ws, name="AzureML-Minimal")

# You can choose a specific Python environment by pointing to a Python path 
# myenv.python.interpreter_path = '/home/johndoe/miniconda3/envs/myenv/bin/python'
# # 1. Local compute target
# myenv = Environment("user-managed-env")
# myenv.python.user_managed_dependencies = True


# # 2. remote compute target
# Select the compute target where your training script will run on. 
# If no compute target is specified in the ScriptRunConfig, or if compute_target='local', 
# Azure ML will execute your script locally.

from azureml.core import ScriptRunConfig

src = ScriptRunConfig(source_directory='./to-run',
                      script='hello.py',
                      compute_target='ci44131a22',
                      environment=myenv)

# # Set compute target
# # Skip this if you are running on your local computer
# script_run_config.run_config.target = my_compute_target


# Submit the experiment
run = experiment.submit(config=src)
run.wait_for_completion(show_output=True)