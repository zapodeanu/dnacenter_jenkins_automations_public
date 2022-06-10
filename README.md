# Cisco DNA Center Jenkins Automations

This repo includes the files for two Cisco DNA Center Jenkins automations pipelines.

- Collect the device inventory and push to GitHub - "jenkinsfile_inventory"
The always up-to-date inventory may be used by other automations tools and platforms

- Create a new fabric with a Border, Control-plane and Edge node device - "jenkinsfile-fabric"
Automate the process to create new fabrics using GitHub repos with the fabric configuration saved as YAML files

**Cisco Products & Services:**

- Cisco DNA Center, devices managed by Cisco DNA Center

**Tools & Frameworks:**

- Jenkins and Docker installed
- Cisco DNA Center Python SDK, optional Cisco DNA Center Ansible Collection

**Usage**

This application will automate workflows calling Cisco DNA Center REST APIs from containers running on Jenkins..

The Jenkins pipeline "jenkinsfile_inventory" will:
- Run on a schedule, every 15 minutes
- Will collect the Cisco DNA Center device inventory
- Push the device inventory files to GitHub
- It includes device, AP and software non-compliant devices inventories, formatted as JSON and YAML files

The Jenkins pipeline "jenkinsfile_fabric" will:
- Run on a schedule, every 5 minutes
- Network engineer will push to GitHub when a new fabric needs to be configured
- Build will pull GitHub to download the fabric configuration file
- Skip deployment of fabric if no file
- Deploy fabrics only when a new fabric must be configured and the config file is pushed to GitHub


**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).



