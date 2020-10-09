from azureml.core import Workspace
from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException

ws = Workspace.from_config() # This automatically looks for a directory .azureml

cpu_cluster_name = "cpu-cluster"

try:
    cpu_cluster = ComputeTarget(workspace=ws, name=cpu_cluster_name)
    print ("Found existing cluster, use it")
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_D2_V2', max_nodes=4, idle_seconds_before_scaledown=2400)

    cpu_cluster = ComputeTarget.create(ws, cpu_cluster_name, compute_config)

cpu_cluster.wait_for_completion(show_output=True)