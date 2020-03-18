import subprocess

with open('deployment_ids.txt', 'r') as f:
    temp = f.readlines()
    content = [x.strip() for x in temp]
    depIds = list(filter(lambda x: len(x) > 12, content))
    print(content)

with open('model_ids.txt', 'r') as f:
    temp = f.readlines()
    content = [x.strip() for x in temp]
    modIds = list(filter(lambda x: len(x) > 12, content))
    print(content)

for i in range(len(depIds)):  
    subprocess.call(["ibmcloud", "ml", "delete", "deployments", modIds[i], depIds[i]])
