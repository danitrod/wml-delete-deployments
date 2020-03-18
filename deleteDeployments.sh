ibmcloud ml list deployments | awk '{print $3}' | tee model_ids.txt
ibmcloud ml list deployments | awk '{print $2}' | tee deployment_ids.txt
python3 deleteDeployments.py