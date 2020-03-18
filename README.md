# IBM Cloud Machine Learning CLI - delete deployments

## Introduction

If you use the Watson Machine Learning Lite plan, and can't create any more Watson Machine Learning deployments because you already created 5, it can be annoying to delete one by one.

Therefore, I created this script to delete all your deployments for you.

## Instructions

1. Install [IBM Cloud CLI](https://cloud.ibm.com/docs/cli?topic=cloud-cli-getting-started)
2. Install IBM Cloud ML plugin
   `ibmcloud plugin install machine-learning`
3. Find your WML instance `ibmcloud ml list instances`
4. Set the WML instance you wish to delete deployments `ibmcloud ml set instance <instance-id>`
5. Clone and acces the repo `git clone https://github.com/danitrod/wml-delete-deployments.git && cd wml-delete-deployments`
6. Run the script `sh deleteDeployments.sh`

## License

Copyright 2020 Daniel T. Rodrigues

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
