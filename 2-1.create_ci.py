import datetime
import time

from azureml.core.compute import ComputeTarget, ComputeInstance
from azureml.core.compute_target import ComputeTargetException
from azureml.core import Workspace

ws = Workspace.from_config()
# Choose a name for your instance
# Compute instance name should be unique across the azure region
compute_name = "ci{}".format(ws._workspace_id)[:10]

# Verify that instance does not exist already
try:
    instance = ComputeInstance(workspace=ws, name=compute_name)
    print('Found existing instance, use it.')
except ComputeTargetException:
    compute_config = ComputeInstance.provisioning_configuration(
        # Standard_DS1_v2
        # Standard_D2s_v3
        # STANDARD_D3_V2
        vm_size='Standard_DS1_v2',
        ssh_public_access=False,
        # vnet_resourcegroup_name='<my-resource-group>',
        # vnet_name='<my-vnet-name>',
        # subnet_name='default',
        # admin_user_ssh_public_key='<my-sshkey>'
    )
    instance = ComputeInstance.create(ws, compute_name, compute_config)
    instance.wait_for_completion(show_output=True)

    # # get_status() gets the latest status of the ComputeInstance target
    # instance.get_status()

    # # stop() is used to stop the ComputeInstance
    # # Stopping ComputeInstance will stop the billing meter and persist the state on the disk.
    # # Available Quota will not be changed with this operation.
    # instance.stop(wait_for_completion=True, show_output=True)

    # # start() is used to start the ComputeInstance if it is in stopped state
    # instance.start(wait_for_completion=True, show_output=True)

    # # restart() is used to restart the ComputeInstance
    # instance.restart(wait_for_completion=True, show_output=True)

    # # delete() is used to delete the ComputeInstance target. Useful if you want to re-use the compute name
    # instance.delete(wait_for_completion=True, show_output=True)