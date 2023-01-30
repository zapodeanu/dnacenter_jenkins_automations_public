# Cisco DNA Center Jenkins Automations

This repo includes the files for two Cisco DNA Center Jenkins automations pipelines.

- Pull from GitHub CLI templates and the devices that we need to configure in the lab and production - "jenkinsfile_templates"
Automate the process of deploying CLI templates to devices. This build may run every evening during maintenance hours or on-demand.

- Collect the device inventory and push to GitHub - "jenkinsfile_inventory"
The always up-to-date inventory may be used by other automations tools and platforms

- Create a new fabric with a Border, Control-plane and Edge node device - "jenkinsfile_fabric"
Automate the process to create new fabrics using GitHub repos with the fabric configuration saved as YAML files

**Cisco Products & Services:**

- Cisco DNA Center, devices managed by Cisco DNA Center

**Tools & Frameworks:**

- Jenkins and Docker installed
- Cisco DNA Center Python SDK, optional Cisco DNA Center Ansible Collection

**Usage**


This application will automate workflows calling Cisco DNA Center REST APIs from containers running on Jenkins..

The Jenkins pipeline, configured using the "jenkinsfile" will:
- clone the repo with the CLI template and deployment config
- deploy the CLI templates to the lab device
- deploy the CLI templates to the production devices
- create a deployment report and push to GitHub

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

The "jenkinsfile_new_pipeline" allows developers to quickly develop a new pipeline.
They will need to customize the environment variables and use the typical steps/stages included. These may be customized as needed.

The Jenkins pipeline "jenkinsfile_poe_sustainability" will:
- run two times, daily, morning and evening
- identify the Cisco DNA Center managed APs and disable/enable the access port
- identify Meraki APs and disable/enable them
- Cisco DNA Center managed APs and Meraki APs could be provided using tags or a list of APs

**Sample Output**

jenkins_templates Build:
```shell
22:25:55  Started by user Gabi Zapodeanu
22:25:55  [Pipeline] Start of Pipeline
22:25:56  [Pipeline] node
22:25:56  Running on Jenkins in /Users/gzapodea/.jenkins/workspace/CLI Templates Deployment
22:25:56  [Pipeline] {
22:25:56  [Pipeline] isUnix
22:25:56  [Pipeline] sh
22:25:57  + docker inspect -f . python:latest
22:25:57  .
22:25:57  [Pipeline] withDockerContainer
22:25:57  Jenkins does not seem to be running inside a container
22:25:57  $ docker run -t -d -u 501:20 -w "/Users/gzapodea/.jenkins/workspace/CLI Templates Deployment" -v "/Users/gzapodea/.jenkins/workspace/CLI Templates Deployment:/Users/gzapodea/.jenkins/workspace/CLI Templates Deployment:rw,z" -v "/Users/gzapodea/.jenkins/workspace/CLI Templates Deployment@tmp:/Users/gzapodea/.jenkins/workspace/CLI Templates Deployment@tmp:rw,z" -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** python:latest cat
22:25:58  $ docker top 6430d3aa0394ec33b2e3d5aac0671c7833795a4eff11c1f0ad31b279a505ad37 -eo pid,comm
22:25:59  [Pipeline] {
22:25:59  [Pipeline] withCredentials
22:25:59  Masking supported pattern matches of $GITHUB_TOKEN
22:25:59  [Pipeline] {
22:26:00  [Pipeline] withEnv
22:26:00  [Pipeline] {
22:26:00  [Pipeline] timeout
22:26:00  Timeout set to expire in 15 min
22:26:00  [Pipeline] {
22:26:00  [Pipeline] stage
22:26:00  [Pipeline] { (Build Python Environment)
22:26:01  [Pipeline] echo
22:26:01  
22:26:01  
22:26:01  Building the Docker container and Installing Python libraries:..........
22:26:01  [Pipeline] sh
22:26:02  + git clone https://gzapodea:****@github.com/zapodeanu/dnacenter_jenkins.git
22:26:02  Cloning into 'dnacenter_jenkins'...
22:26:04  [Pipeline] withEnv
22:26:04  [Pipeline] {
22:26:04  [Pipeline] sh
22:26:05  + pip install -r dnacenter_jenkins/requirements.txt --no-warn-script-location
22:26:06  Defaulting to user installation because normal site-packages is not writeable
22:26:07  Collecting requests
22:26:07    Downloading requests-2.27.1-py2.py3-none-any.whl (63 kB)
22:26:07       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.1/63.1 KB 602.0 kB/s eta 0:00:00
22:26:07  Collecting urllib3
22:26:07    Downloading urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
22:26:08       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 139.0/139.0 KB 1.1 MB/s eta 0:00:00
22:26:08  Collecting dnacentersdk
22:26:08    Downloading dnacentersdk-2.4.10-py3-none-any.whl (2.4 MB)
22:26:09       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 2.2 MB/s eta 0:00:00
22:26:09  Collecting pyopenssl
22:26:09    Downloading pyOpenSSL-22.0.0-py2.py3-none-any.whl (55 kB)
22:26:09       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.8/55.8 KB 1.1 MB/s eta 0:00:00
22:26:09  Collecting python-dotenv
22:26:09    Downloading python_dotenv-0.20.0-py3-none-any.whl (17 kB)
22:26:10  Collecting PyYAML
22:26:10    Downloading PyYAML-6.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (682 kB)
22:26:10       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 682.2/682.2 KB 3.5 MB/s eta 0:00:00
22:26:10  Collecting charset-normalizer~=2.0.0
22:26:10    Downloading charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
22:26:10  Collecting idna<4,>=2.5
22:26:10    Downloading idna-3.3-py3-none-any.whl (61 kB)
22:26:10       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 KB 2.3 MB/s eta 0:00:00
22:26:11  Collecting certifi>=2017.4.17
22:26:11    Downloading certifi-2022.5.18.1-py3-none-any.whl (155 kB)
22:26:11       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.2/155.2 KB 4.5 MB/s eta 0:00:00
22:26:11  Collecting fastjsonschema<3.0.0,>=2.14.5
22:26:11    Downloading fastjsonschema-2.15.3-py3-none-any.whl (22 kB)
22:26:11  Collecting future<0.19.0,>=0.18.2
22:26:11    Downloading future-0.18.2.tar.gz (829 kB)
22:26:11       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 829.2/829.2 KB 3.7 MB/s eta 0:00:00
22:26:11    Preparing metadata (setup.py): started
22:26:12    Preparing metadata (setup.py): finished with status 'done'
22:26:12  Collecting requests-toolbelt<0.10.0,>=0.9.1
22:26:12    Downloading requests_toolbelt-0.9.1-py2.py3-none-any.whl (54 kB)
22:26:12       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.3/54.3 KB 2.4 MB/s eta 0:00:00
22:26:13  Collecting cryptography>=35.0
22:26:13    Downloading cryptography-37.0.2-cp36-abi3-manylinux_2_24_x86_64.whl (4.0 MB)
22:26:14       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.0/4.0 MB 3.7 MB/s eta 0:00:00
22:26:14  Collecting cffi>=1.12
22:26:14    Downloading cffi-1.15.0-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (446 kB)
22:26:15       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 446.3/446.3 KB 3.9 MB/s eta 0:00:00
22:26:15  Collecting pycparser
22:26:15    Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
22:26:15       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 KB 3.0 MB/s eta 0:00:00
22:26:15  Building wheels for collected packages: future
22:26:15    Building wheel for future (setup.py): started
22:26:16    Building wheel for future (setup.py): finished with status 'done'
22:26:16    Created wheel for future: filename=future-0.18.2-py3-none-any.whl size=491070 sha256=3ce5566a3728ea13300a6f1ced862c2a70e0ff77bb0117c8374fea2bdc7a5ac0
22:26:16    Stored in directory: /Users/gzapodea/.jenkins/workspace/CLI Templates Deployment/.cache/pip/wheels/22/73/06/557dc4f4ef68179b9d763930d6eec26b88ed7c389b19588a1c
22:26:16  Successfully built future
22:26:16  Installing collected packages: fastjsonschema, urllib3, PyYAML, python-dotenv, pycparser, idna, future, charset-normalizer, certifi, requests, cffi, requests-toolbelt, cryptography, pyopenssl, dnacentersdk
22:26:44  Successfully installed PyYAML-6.0 certifi-2022.5.18.1 cffi-1.15.0 charset-normalizer-2.0.12 cryptography-37.0.2 dnacentersdk-2.4.10 fastjsonschema-2.15.3 future-0.18.2 idna-3.3 pycparser-2.21 pyopenssl-22.0.0 python-dotenv-0.20.0 requests-2.27.1 requests-toolbelt-0.9.1 urllib3-1.26.9
22:26:44  WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
22:26:44  You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
22:26:44  [Pipeline] echo
22:26:44  
22:26:44  
22:26:44  Verify Python version and Libraries:............
22:26:44  [Pipeline] sh
22:26:45  + python --version
22:26:45  Python 3.10.5
22:26:45  [Pipeline] sh
22:26:46  + pip3 list
22:26:48  Package            Version
22:26:48  ------------------ -----------
22:26:48  certifi            2022.5.18.1
22:26:48  cffi               1.15.0
22:26:48  charset-normalizer 2.0.12
22:26:48  cryptography       37.0.2
22:26:48  dnacentersdk       2.4.10
22:26:48  fastjsonschema     2.15.3
22:26:48  future             0.18.2
22:26:48  idna               3.3
22:26:48  pip                22.0.4
22:26:48  pycparser          2.21
22:26:48  pyOpenSSL          22.0.0
22:26:48  python-dotenv      0.20.0
22:26:48  PyYAML             6.0
22:26:48  requests           2.27.1
22:26:48  requests-toolbelt  0.9.1
22:26:48  setuptools         58.1.0
22:26:48  urllib3            1.26.9
22:26:48  wheel              0.37.1
22:26:48  WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
22:26:48  You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
22:26:48  [Pipeline] echo
22:26:48  
22:26:48  
22:26:48  Verify Application Files:..........
22:26:48  [Pipeline] sh
22:26:49  + ls dnacenter_jenkins/
22:26:49  cli_template.txt
22:26:49  deploy_templates.py
22:26:49  jenkinsfile
22:26:49  lab_deploy_templates.py
22:26:49  project_details.yml
22:26:49  requirements.txt
22:26:49  [Pipeline] }
22:26:49  [Pipeline] // withEnv
22:26:49  [Pipeline] }
22:26:49  [Pipeline] // stage
22:26:49  [Pipeline] stage
22:26:49  [Pipeline] { (Download the Project Repo)
22:26:50  [Pipeline] echo
22:26:50  
22:26:50  
22:26:50  Downloading the CLI Templates:..........
22:26:50  [Pipeline] sh
22:26:50  + git clone https://gzapodea:****@github.com/zapodeanu/templates_jenkins.git
22:26:50  Cloning into 'templates_jenkins'...
22:26:52  [Pipeline] withEnv
22:26:52  [Pipeline] {
22:26:52  [Pipeline] echo
22:26:52  
22:26:52  
22:26:52  Verify Templates Files:............
22:26:52  [Pipeline] sh
22:26:53  + ls templates_jenkins/
22:26:53  cli_template.txt
22:26:53  deployment_report.json
22:26:53  project_details.yml
22:26:53  [Pipeline] }
22:26:53  [Pipeline] // withEnv
22:26:53  [Pipeline] }
22:26:54  [Pipeline] // stage
22:26:54  [Pipeline] stage
22:26:54  [Pipeline] { (Deploy the CLI Templates - Lab)
22:26:54  [Pipeline] echo
22:26:54  
22:26:54  
22:26:54  Lab Deploying the CLI Templates:..........
22:26:54  [Pipeline] withEnv
22:26:54  [Pipeline] {
22:26:54  [Pipeline] echo
22:26:54  
22:26:54  
22:26:54  Verify Working Path:............
22:26:54  [Pipeline] sh
22:26:55  + pwd
22:26:55  /Users/gzapodea/.jenkins/workspace/CLI Templates Deployment
22:26:55  [Pipeline] dir
22:26:55  Running in /Users/gzapodea/.jenkins/workspace/CLI Templates Deployment/dnacenter_jenkins
22:26:55  [Pipeline] {
22:26:55  [Pipeline] sh
22:26:56  + python3 lab_deploy_templates.py
22:27:00  INFO:root:App "lab_deploy_templates.py" Start, 2022-06-07 22:26:59
22:27:19  INFO:root:Project name: Jenkins
22:27:19  INFO:root:Project id: 4b78d5e7-ae3f-45bf-81a9-94f11b2a1d2b
22:27:19  INFO:root:Created template with the name: cli_template
22:27:32  INFO:root:Template committed
22:27:36  INFO:root:Deploying template to lab device: PDX-RN
22:27:52  INFO:root:Lab Deployment Report:
22:27:52  INFO:root:[{"hostname": "PDX-RN", "status": "successful"}]
22:27:52  INFO:root:End of Application "lab_deploy_templates.py" Run: 2022-06-07 22:27:51
22:27:52  [Pipeline] }
22:27:52  [Pipeline] // dir
22:27:52  [Pipeline] }
22:27:52  [Pipeline] // withEnv
22:27:53  [Pipeline] }
22:27:53  [Pipeline] // stage
22:27:53  [Pipeline] stage
22:27:53  [Pipeline] { (Deploy the CLI Templates - Production)
22:27:53  [Pipeline] echo
22:27:53  
22:27:53  
22:27:53  Deploying the CLI Templates:..........
22:27:53  [Pipeline] withEnv
22:27:53  [Pipeline] {
22:27:53  [Pipeline] echo
22:27:53  
22:27:53  
22:27:53  Verify Working Path:............
22:27:53  [Pipeline] sh
22:27:55  + pwd
22:27:55  /Users/gzapodea/.jenkins/workspace/CLI Templates Deployment
22:27:55  [Pipeline] dir
22:27:55  Running in /Users/gzapodea/.jenkins/workspace/CLI Templates Deployment/dnacenter_jenkins
22:27:55  [Pipeline] {
22:27:55  [Pipeline] sh
22:27:56  + python3 deploy_templates.py
22:27:59  INFO:root:App "deploy_templates.py" Start, 2022-06-07 22:27:59
22:28:00  INFO:root:Project name: Jenkins
22:28:00  INFO:root:Project id: 4b78d5e7-ae3f-45bf-81a9-94f11b2a1d2b
22:28:00  INFO:root:Template found and deleted
22:28:16  INFO:root:Created template with the name: cli_template
22:28:32  INFO:root:Template committed
22:28:35  INFO:root:Deploying template to device: PDX-RO
22:28:51  INFO:root:Deploying template to device: SP
22:29:07  INFO:root:Deploying template to device: NYC-RO
22:29:23  INFO:root:Deployment Report:
22:29:23  INFO:root:{"timestamp": "2022-06-07 22:27:59", "template_content": "!\n!\ninterface loopback 500\n description Interface - Jenkins_config\n!\nip access-list extended RETAIL\n remark Access List for RETAIL - Jenkins_config\n 10 permit ip any host 10.94.141.90\n 20 permit ip any host 10.94.141.91\n!\n!", "report": [{"hostname": "PDX-RO", "status": "successful"}, {"hostname": "SP", "status": "successful"}, {"hostname": "NYC-RO", "status": "successful"}]}
22:29:23  INFO:root:End of Application "deploy_templates.py" Run: 2022-06-07 22:29:21
22:29:23  [Pipeline] }
22:29:23  [Pipeline] // dir
22:29:23  [Pipeline] }
22:29:23  [Pipeline] // withEnv
22:29:23  [Pipeline] }
22:29:24  [Pipeline] // stage
22:29:24  [Pipeline] stage
22:29:24  [Pipeline] { (Upload Deployment Report)
22:29:24  [Pipeline] echo
22:29:24  
22:29:24  
22:29:24  Verify if the deployment report file exists:..........
22:29:24  [Pipeline] withEnv
22:29:24  [Pipeline] {
22:29:24  [Pipeline] dir
22:29:24  Running in /Users/gzapodea/.jenkins/workspace/CLI Templates Deployment/templates_jenkins
22:29:24  [Pipeline] {
22:29:25  [Pipeline] sh
22:29:26  + ls deployment_report.json
22:29:26  deployment_report.json
22:29:26  [Pipeline] echo
22:29:26  
22:29:26  
22:29:26  Uploading to GitHub the deployment report:..........
22:29:26  [Pipeline] sh
22:29:27  + git config --global user.email gzapodea@cisco.com
22:29:27  [Pipeline] sh
22:29:27  + git config --global user.name gzapodea
22:29:28  [Pipeline] sh
22:29:28  + git add deployment_report.json
22:29:28  [Pipeline] sh
22:29:29  + git commit -m committed by Jenkins
22:29:29  [master 136dfaf] committed by Jenkins
22:29:29   1 file changed, 1 insertion(+), 1 deletion(-)
22:29:29   rewrite deployment_report.json (85%)
22:29:29  [Pipeline] sh
22:29:30  + git push origin master --force
22:29:31  To https://github.com/zapodeanu/templates_jenkins.git
22:29:31     dba9938..136dfaf  master -> master
22:29:31  [Pipeline] }
22:29:31  [Pipeline] // dir
22:29:31  [Pipeline] }
22:29:32  [Pipeline] // withEnv
22:29:32  [Pipeline] }
22:29:32  [Pipeline] // stage
22:29:32  [Pipeline] stage
22:29:32  [Pipeline] { (Declarative: Post Actions)
22:29:32  [Pipeline] echo
22:29:32  
22:29:32  
22:29:32  Jenkins CLI Templates Deployment end
22:29:32  [Pipeline] cleanWs
22:29:32  [WS-CLEANUP] Deleting project workspace...
22:29:32  [WS-CLEANUP] Deferred wipeout is used...
22:29:32  [WS-CLEANUP] done
22:29:32  [Pipeline] }
22:29:33  [Pipeline] // stage
22:29:33  [Pipeline] }
22:29:33  [Pipeline] // timeout
22:29:33  [Pipeline] }
22:29:33  [Pipeline] // withEnv
22:29:33  [Pipeline] }
22:29:33  [Pipeline] // withCredentials
22:29:33  [Pipeline] }
22:29:33  $ docker stop --time=1 6430d3aa0394ec33b2e3d5aac0671c7833795a4eff11c1f0ad31b279a505ad37
22:29:35  $ docker rm -f 6430d3aa0394ec33b2e3d5aac0671c7833795a4eff11c1f0ad31b279a505ad37
22:29:36  [Pipeline] // withDockerContainer
22:29:36  [Pipeline] }
22:29:36  [Pipeline] // node
22:29:36  [Pipeline] End of Pipeline
22:29:36  Finished: SUCCESS
```

jenkinsfile_fabric Build:
```shell
10:25:18  Started by user Gabi Zapodeanu
10:25:18  [Pipeline] Start of Pipeline
10:25:19  [Pipeline] node
10:25:19  Running on Jenkins in /Users/gzapodea/.jenkins/workspace/Device Inventory
10:25:19  [Pipeline] {
10:25:20  [Pipeline] isUnix
10:25:20  [Pipeline] sh
10:25:20  + docker inspect -f . python:latest
10:25:21  .
10:25:21  [Pipeline] withDockerContainer
10:25:21  Jenkins does not seem to be running inside a container
10:25:21  $ docker run -t -d -u 501:20 -w "/Users/gzapodea/.jenkins/workspace/Device Inventory" -v "/Users/gzapodea/.jenkins/workspace/Device Inventory:/Users/gzapodea/.jenkins/workspace/Device Inventory:rw,z" -v "/Users/gzapodea/.jenkins/workspace/Device Inventory@tmp:/Users/gzapodea/.jenkins/workspace/Device Inventory@tmp:rw,z" -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** python:latest cat
10:25:22  $ docker top 1374eb16e7c2510171d09671090aecf742446af3f6ef812be933f62e245401cb -eo pid,comm
10:25:22  [Pipeline] {
10:25:22  [Pipeline] withCredentials
10:25:22  Masking supported pattern matches of $GITHUB_TOKEN
10:25:23  [Pipeline] {
10:25:23  [Pipeline] withEnv
10:25:23  [Pipeline] {
10:25:23  [Pipeline] timeout
10:25:23  Timeout set to expire in 15 min
10:25:23  [Pipeline] {
10:25:23  [Pipeline] stage
10:25:23  [Pipeline] { (Build Python Environment)
10:25:24  [Pipeline] echo
10:25:24  
10:25:24  
10:25:24  Jenkins Device Inventory pipeline start..............................
10:25:24  [Pipeline] echo
10:25:24  
10:25:24  
10:25:24  Building the Docker container:..............................
10:25:24  [Pipeline] }
10:25:24  [Pipeline] // stage
10:25:24  [Pipeline] stage
10:25:24  [Pipeline] { (Install Python libraries)
10:25:24  [Pipeline] echo
10:25:24  
10:25:24  
10:25:24  Installing Python libraries:..............................
10:25:24  [Pipeline] sh
10:25:25  + git clone https://gzapodea:****@github.com/zapodeanu/dnacenter_jenkins_automations.git
10:25:25  Cloning into 'dnacenter_jenkins_automations'...
10:25:27  [Pipeline] withEnv
10:25:27  [Pipeline] {
10:25:27  [Pipeline] sh
10:25:28  + pip install -r dnacenter_jenkins_automations/requirements.txt --no-warn-script-location
10:25:30  Defaulting to user installation because normal site-packages is not writeable
10:25:30  Collecting requests
10:25:30    Downloading requests-2.27.1-py2.py3-none-any.whl (63 kB)
10:25:31       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 63.1/63.1 KB 367.5 kB/s eta 0:00:00
10:25:31  Collecting urllib3
10:25:31    Downloading urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
10:25:31       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 139.0/139.0 KB 940.0 kB/s eta 0:00:00
10:25:31  Collecting dnacentersdk
10:25:31    Downloading dnacentersdk-2.4.10-py3-none-any.whl (2.4 MB)
10:25:33       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 1.2 MB/s eta 0:00:00
10:25:33  Collecting pyopenssl
10:25:33    Downloading pyOpenSSL-22.0.0-py2.py3-none-any.whl (55 kB)
10:25:33       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.8/55.8 KB 556.4 kB/s eta 0:00:00
10:25:33  Collecting python-dotenv
10:25:33    Downloading python_dotenv-0.20.0-py3-none-any.whl (17 kB)
10:25:34  Collecting PyYAML
10:25:34    Downloading PyYAML-6.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (682 kB)
10:25:34       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 682.2/682.2 KB 3.2 MB/s eta 0:00:00
10:25:34  Collecting PyGithub
10:25:34    Downloading PyGithub-1.55-py3-none-any.whl (291 kB)
10:25:34       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 291.7/291.7 KB 2.9 MB/s eta 0:00:00
10:25:34  Collecting idna<4,>=2.5
10:25:34    Downloading idna-3.3-py3-none-any.whl (61 kB)
10:25:34       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 KB 1.2 MB/s eta 0:00:00
10:25:35  Collecting charset-normalizer~=2.0.0
10:25:35    Downloading charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
10:25:35  Collecting certifi>=2017.4.17
10:25:35    Downloading certifi-2022.5.18.1-py3-none-any.whl (155 kB)
10:25:35       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.2/155.2 KB 1.6 MB/s eta 0:00:00
10:25:35  Collecting future<0.19.0,>=0.18.2
10:25:35    Downloading future-0.18.2.tar.gz (829 kB)
10:25:35       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 829.2/829.2 KB 3.6 MB/s eta 0:00:00
10:25:35    Preparing metadata (setup.py): started
10:25:36    Preparing metadata (setup.py): finished with status 'done'
10:25:36  Collecting requests-toolbelt<0.10.0,>=0.9.1
10:25:36    Downloading requests_toolbelt-0.9.1-py2.py3-none-any.whl (54 kB)
10:25:36       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.3/54.3 KB 572.5 kB/s eta 0:00:00
10:25:37  Collecting fastjsonschema<3.0.0,>=2.14.5
10:25:37    Downloading fastjsonschema-2.15.3-py3-none-any.whl (22 kB)
10:25:38  Collecting cryptography>=35.0
10:25:38    Downloading cryptography-37.0.2-cp36-abi3-manylinux_2_24_x86_64.whl (4.0 MB)
10:25:43       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.0/4.0 MB 740.3 kB/s eta 0:00:00
10:25:43  Collecting pyjwt>=2.0
10:25:43    Downloading PyJWT-2.4.0-py3-none-any.whl (18 kB)
10:25:43  Collecting deprecated
10:25:43    Downloading Deprecated-1.2.13-py2.py3-none-any.whl (9.6 kB)
10:25:44  Collecting pynacl>=1.4.0
10:25:44    Downloading PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (856 kB)
10:25:44       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 856.7/856.7 KB 2.2 MB/s eta 0:00:00
10:25:45  Collecting cffi>=1.12
10:25:45    Downloading cffi-1.15.0-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (446 kB)
10:25:45       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 446.3/446.3 KB 2.6 MB/s eta 0:00:00
10:25:46  Collecting wrapt<2,>=1.10
10:25:46    Downloading wrapt-1.14.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (77 kB)
10:25:46       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.9/77.9 KB 1.5 MB/s eta 0:00:00
10:25:46  Collecting pycparser
10:25:46    Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
10:25:46       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 KB 1.4 MB/s eta 0:00:00
10:25:46  Building wheels for collected packages: future
10:25:46    Building wheel for future (setup.py): started
10:25:47    Building wheel for future (setup.py): finished with status 'done'
10:25:47    Created wheel for future: filename=future-0.18.2-py3-none-any.whl size=491070 sha256=0503e6a6216bb86e79a4667e3b831f216e8f9736e03a197fb0ae885898426028
10:25:47    Stored in directory: /Users/gzapodea/.jenkins/workspace/Device Inventory/.cache/pip/wheels/22/73/06/557dc4f4ef68179b9d763930d6eec26b88ed7c389b19588a1c
10:25:47  Successfully built future
10:25:48  Installing collected packages: fastjsonschema, wrapt, urllib3, PyYAML, python-dotenv, pyjwt, pycparser, idna, future, charset-normalizer, certifi, requests, deprecated, cffi, requests-toolbelt, pynacl, cryptography, pyopenssl, PyGithub, dnacentersdk
10:26:36  Successfully installed PyGithub-1.55 PyYAML-6.0 certifi-2022.5.18.1 cffi-1.15.0 charset-normalizer-2.0.12 cryptography-37.0.2 deprecated-1.2.13 dnacentersdk-2.4.10 fastjsonschema-2.15.3 future-0.18.2 idna-3.3 pycparser-2.21 pyjwt-2.4.0 pynacl-1.5.0 pyopenssl-22.0.0 python-dotenv-0.20.0 requests-2.27.1 requests-toolbelt-0.9.1 urllib3-1.26.9 wrapt-1.14.1
10:26:36  WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
10:26:36  You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
10:26:36  [Pipeline] echo
10:26:36  
10:26:36  
10:26:36  Verify Python version and Libraries:..............................
10:26:36  [Pipeline] sh
10:26:37  + python --version
10:26:37  Python 3.10.5
10:26:37  [Pipeline] sh
10:26:37  + pip3 list
10:26:40  Package            Version
10:26:40  ------------------ -----------
10:26:40  certifi            2022.5.18.1
10:26:40  cffi               1.15.0
10:26:40  charset-normalizer 2.0.12
10:26:40  cryptography       37.0.2
10:26:40  Deprecated         1.2.13
10:26:40  dnacentersdk       2.4.10
10:26:40  fastjsonschema     2.15.3
10:26:40  future             0.18.2
10:26:40  idna               3.3
10:26:40  pip                22.0.4
10:26:40  pycparser          2.21
10:26:40  PyGithub           1.55
10:26:40  PyJWT              2.4.0
10:26:40  PyNaCl             1.5.0
10:26:40  pyOpenSSL          22.0.0
10:26:40  python-dotenv      0.20.0
10:26:40  PyYAML             6.0
10:26:40  requests           2.27.1
10:26:40  requests-toolbelt  0.9.1
10:26:40  setuptools         58.1.0
10:26:40  urllib3            1.26.9
10:26:40  wheel              0.37.1
10:26:40  wrapt              1.14.1
10:26:40  WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
10:26:40  You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
10:26:40  [Pipeline] echo
10:26:40  
10:26:40  
10:26:40  Verify Application Files:..............................
10:26:40  [Pipeline] sh
10:26:41  + ls dnacenter_jenkins_automations/
10:26:41  CODE_OF_CONDUCT.md
10:26:41  CONTRIBUTING.md
10:26:41  LICENSE
10:26:41  NOTICE
10:26:41  README.md
10:26:41  create_fabric.py
10:26:41  device_inventory.py
10:26:41  environment.env
10:26:41  fabric_info.yml
10:26:41  inventory
10:26:41  jenkinsfile_fabric
10:26:41  jenkinsfile_inventory
10:26:41  requirements.txt
10:26:41  [Pipeline] }
10:26:41  [Pipeline] // withEnv
10:26:41  [Pipeline] }
10:26:41  [Pipeline] // stage
10:26:41  [Pipeline] stage
10:26:41  [Pipeline] { (Device inventory collection)
10:26:42  [Pipeline] echo
10:26:42  
10:26:42  
10:26:42  Collect the inventory of devices managed by Cisco DNA Center:..............................
10:26:42  [Pipeline] withEnv
10:26:42  [Pipeline] {
10:26:42  [Pipeline] echo
10:26:42  
10:26:42  
10:26:42  Verify Working Path:..............................
10:26:42  [Pipeline] sh
10:26:43  + pwd
10:26:43  /Users/gzapodea/.jenkins/workspace/Device Inventory
10:26:43  [Pipeline] dir
10:26:43  Running in /Users/gzapodea/.jenkins/workspace/Device Inventory/dnacenter_jenkins_automations
10:26:43  [Pipeline] {
10:26:44  [Pipeline] sh
10:26:45  + python3 device_inventory.py
10:26:51  INFO:root:  App "device_inventory.py" run start, 2022-06-08 10:26:50
10:26:51  INFO:root:  Number of devices managed by Cisco DNA Center: 13
10:26:51  INFO:root:  Collected the device list from Cisco DNA Center
10:27:07  INFO:root:  Collected the device inventory from Cisco DNA Center
10:27:07  INFO:root:  Saved the device inventory to file "device_inventory.json"
10:27:07  INFO:root:  Saved the device inventory to file "device_inventory.yaml"
10:27:07  INFO:root:  Saved the device inventory to file "ap_inventory.json"
10:27:07  INFO:root:  Saved the device inventory to file "ap_inventory.yaml"
10:27:07  INFO:root:  Number of devices image non-compliant: 2
10:27:07  INFO:root:  Image non-compliant devices: 
10:27:07  INFO:root:      LO-CN, Site Hierarchy: Global/OR/LO/Floor-3
10:27:07  INFO:root:      LO-BN, Site Hierarchy: Global/OR/LO/Floor-3
10:27:07  INFO:root:  Saved the image non-compliant device inventory to file "non_compliant_devices.json"
10:27:07  INFO:root:  Saved the image non-compliant device inventory to file "non_compliant_devices.yaml"
10:27:07  INFO:root:  GitHub push for file: ap_inventory.json
10:27:07  INFO:root:  GitHub push for file: ap_inventory.yaml
10:27:08  INFO:root:  GitHub push for file: device_inventory.json
10:27:09  INFO:root:  GitHub push for file: device_inventory.yaml
10:27:10  INFO:root:  GitHub push for file: non_compliant_devices.json
10:27:11  INFO:root:  GitHub push for file: non_compliant_devices.yaml
10:27:11  INFO:root:  App "device_inventory.py" run end: 2022-06-08 10:27:11
10:27:11  [Pipeline] }
10:27:12  [Pipeline] // dir
10:27:12  [Pipeline] }
10:27:12  [Pipeline] // withEnv
10:27:12  [Pipeline] }
10:27:12  [Pipeline] // stage
10:27:12  [Pipeline] stage
10:27:12  [Pipeline] { (List the "inventory" folder content)
10:27:12  [Pipeline] echo
10:27:12  
10:27:12  
10:27:12  The inventory files that have been created:..............................
10:27:12  [Pipeline] withEnv
10:27:12  [Pipeline] {
10:27:13  [Pipeline] echo
10:27:13  
10:27:13  
10:27:13  Verify Working Path:..............................
10:27:13  [Pipeline] sh
10:27:13  + pwd
10:27:13  /Users/gzapodea/.jenkins/workspace/Device Inventory
10:27:14  [Pipeline] dir
10:27:14  Running in /Users/gzapodea/.jenkins/workspace/Device Inventory/dnacenter_jenkins_automations/inventory
10:27:14  [Pipeline] {
10:27:14  [Pipeline] sh
10:27:14  + ls -l -A
10:27:14  total 24
10:27:14  -rw-r--r-- 1 501 dialout  285 Jun  8 17:27 ap_inventory.json
10:27:14  -rw-r--r-- 1 501 dialout  273 Jun  8 17:27 ap_inventory.yaml
10:27:14  -rw-r--r-- 1 501 dialout 3478 Jun  8 17:27 device_inventory.json
10:27:14  -rw-r--r-- 1 501 dialout 3184 Jun  8 17:27 device_inventory.yaml
10:27:14  -rw-r--r-- 1 501 dialout  560 Jun  8 17:27 non_compliant_devices.json
10:27:14  -rw-r--r-- 1 501 dialout  523 Jun  8 17:27 non_compliant_devices.yaml
10:27:15  [Pipeline] }
10:27:15  [Pipeline] // dir
10:27:15  [Pipeline] }
10:27:15  [Pipeline] // withEnv
10:27:15  [Pipeline] }
10:27:15  [Pipeline] // stage
10:27:15  [Pipeline] stage
10:27:15  [Pipeline] { (Declarative: Post Actions)
10:27:15  [Pipeline] echo
10:27:15  
10:27:16  
10:27:16  Jenkins Device Inventory pipeline end
10:27:16  [Pipeline] cleanWs
10:27:16  [WS-CLEANUP] Deleting project workspace...
10:27:16  [WS-CLEANUP] Deferred wipeout is used...
10:27:16  [WS-CLEANUP] done
10:27:16  [Pipeline] }
10:27:16  [Pipeline] // stage
10:27:16  [Pipeline] }
10:27:16  [Pipeline] // timeout
10:27:16  [Pipeline] }
10:27:16  [Pipeline] // withEnv
10:27:16  [Pipeline] }
10:27:17  [Pipeline] // withCredentials
10:27:17  [Pipeline] }
10:27:17  $ docker stop --time=1 1374eb16e7c2510171d09671090aecf742446af3f6ef812be933f62e245401cb
10:27:18  $ docker rm -f 1374eb16e7c2510171d09671090aecf742446af3f6ef812be933f62e245401cb
10:27:19  [Pipeline] // withDockerContainer
10:27:19  [Pipeline] }
10:27:19  [Pipeline] // node
10:27:19  [Pipeline] End of Pipeline
10:27:19  Finished: SUCCESS
```

jenkinsfile_fabric Build
```shell
16:27:42  Started by user Gabi Zapodeanu
16:27:44  [Pipeline] Start of Pipeline
16:27:45  [Pipeline] node
16:27:45  Running on Jenkins in /Users/gzapodea/.jenkins/workspace/SDA as Code
16:27:45  [Pipeline] {
16:27:46  [Pipeline] isUnix
16:27:46  [Pipeline] sh
16:27:47  + docker inspect -f . python:latest
16:27:47  .
16:27:47  [Pipeline] withDockerContainer
16:27:47  Jenkins does not seem to be running inside a container
16:27:47  $ docker run -t -d -u 501:20 -w "/Users/gzapodea/.jenkins/workspace/SDA as Code" -v "/Users/gzapodea/.jenkins/workspace/SDA as Code:/Users/gzapodea/.jenkins/workspace/SDA as Code:rw,z" -v "/Users/gzapodea/.jenkins/workspace/SDA as Code@tmp:/Users/gzapodea/.jenkins/workspace/SDA as Code@tmp:rw,z" -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** python:latest cat
16:27:48  $ docker top e430227316f783011ca70268af90ae2e9aba064a0fa15e344db270196055b9ff -eo pid,comm
16:27:48  [Pipeline] {
16:27:48  [Pipeline] withCredentials
16:27:48  Masking supported pattern matches of $GITHUB_TOKEN
16:27:48  [Pipeline] {
16:27:48  [Pipeline] withEnv
16:27:48  [Pipeline] {
16:27:49  [Pipeline] timeout
16:27:49  Timeout set to expire in 15 min
16:27:49  [Pipeline] {
16:27:49  [Pipeline] stage
16:27:49  [Pipeline] { (Build Python Environment)
16:27:49  [Pipeline] echo
16:27:49  
16:27:49  
16:27:49  Jenkins Create Fabric build start..............................
16:27:49  [Pipeline] echo
16:27:49  
16:27:49  
16:27:49  Building the Docker container:..............................
16:27:49  [Pipeline] }
16:27:49  [Pipeline] // stage
16:27:49  [Pipeline] stage
16:27:49  [Pipeline] { (Install Python libraries)
16:27:49  [Pipeline] echo
16:27:49  
16:27:49  
16:27:49  Installing Python libraries:..............................
16:27:49  [Pipeline] sh
16:27:50  + git clone https://gzapodea:****@github.com/zapodeanu/dnacenter_jenkins_automations.git
16:27:50  Cloning into 'dnacenter_jenkins_automations'...
16:27:51  [Pipeline] withEnv
16:27:51  [Pipeline] {
16:27:52  [Pipeline] sh
16:27:52  + pip install -r dnacenter_jenkins_automations/requirements.txt --no-warn-script-location
16:27:54  Defaulting to user installation because normal site-packages is not writeable
16:27:54  Collecting requests
16:27:54    Downloading requests-2.28.0-py3-none-any.whl (62 kB)
16:27:54       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.8/62.8 KB 930.3 kB/s eta 0:00:00
16:27:54  Collecting urllib3
16:27:54    Downloading urllib3-1.26.9-py2.py3-none-any.whl (138 kB)
16:27:54       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 139.0/139.0 KB 2.4 MB/s eta 0:00:00
16:27:55  Collecting dnacentersdk
16:27:55    Downloading dnacentersdk-2.4.10-py3-none-any.whl (2.4 MB)
16:27:55       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 5.1 MB/s eta 0:00:00
16:27:55  Collecting pyopenssl
16:27:55    Downloading pyOpenSSL-22.0.0-py2.py3-none-any.whl (55 kB)
16:27:55       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.8/55.8 KB 2.0 MB/s eta 0:00:00
16:27:55  Collecting python-dotenv
16:27:55    Downloading python_dotenv-0.20.0-py3-none-any.whl (17 kB)
16:27:56  Collecting PyYAML
16:27:56    Downloading PyYAML-6.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (682 kB)
16:27:56       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 682.2/682.2 KB 5.1 MB/s eta 0:00:00
16:27:56  Collecting PyGithub
16:27:56    Downloading PyGithub-1.55-py3-none-any.whl (291 kB)
16:27:56       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 291.7/291.7 KB 4.4 MB/s eta 0:00:00
16:27:56  Collecting idna<4,>=2.5
16:27:56    Downloading idna-3.3-py3-none-any.whl (61 kB)
16:27:56       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 61.2/61.2 KB 2.3 MB/s eta 0:00:00
16:27:56  Collecting charset-normalizer~=2.0.0
16:27:56    Downloading charset_normalizer-2.0.12-py3-none-any.whl (39 kB)
16:27:56  Collecting certifi>=2017.4.17
16:27:57    Downloading certifi-2022.5.18.1-py3-none-any.whl (155 kB)
16:27:57       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 155.2/155.2 KB 5.5 MB/s eta 0:00:00
16:27:57  Collecting requests-toolbelt<0.10.0,>=0.9.1
16:27:57    Downloading requests_toolbelt-0.9.1-py2.py3-none-any.whl (54 kB)
16:27:57       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.3/54.3 KB 2.5 MB/s eta 0:00:00
16:27:57  Collecting fastjsonschema<3.0.0,>=2.14.5
16:27:57    Downloading fastjsonschema-2.15.3-py3-none-any.whl (22 kB)
16:27:57  Collecting future<0.19.0,>=0.18.2
16:27:57    Downloading future-0.18.2.tar.gz (829 kB)
16:27:57       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 829.2/829.2 KB 4.0 MB/s eta 0:00:00
16:27:57    Preparing metadata (setup.py): started
16:27:58    Preparing metadata (setup.py): finished with status 'done'
16:27:58  Collecting cryptography>=35.0
16:27:58    Downloading cryptography-37.0.2-cp36-abi3-manylinux_2_24_x86_64.whl (4.0 MB)
16:27:59       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.0/4.0 MB 5.5 MB/s eta 0:00:00
16:27:59  Collecting pyjwt>=2.0
16:27:59    Downloading PyJWT-2.4.0-py3-none-any.whl (18 kB)
16:27:59  Collecting deprecated
16:27:59    Downloading Deprecated-1.2.13-py2.py3-none-any.whl (9.6 kB)
16:28:00  Collecting pynacl>=1.4.0
16:28:00    Downloading PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl (856 kB)
16:28:00       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 856.7/856.7 KB 5.8 MB/s eta 0:00:00
16:28:00  Collecting cffi>=1.12
16:28:00    Downloading cffi-1.15.0-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (446 kB)
16:28:00       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 446.3/446.3 KB 9.7 MB/s eta 0:00:00
16:28:01  Collecting wrapt<2,>=1.10
16:28:01    Downloading wrapt-1.14.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (77 kB)
16:28:01       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.9/77.9 KB 3.4 MB/s eta 0:00:00
16:28:01  Collecting pycparser
16:28:01    Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
16:28:01       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 KB 3.0 MB/s eta 0:00:00
16:28:01  Building wheels for collected packages: future

16:28:01    Building wheel for future (setup.py): started

16:28:02    Building wheel for future (setup.py): finished with status 'done'
16:28:02    Created wheel for future: filename=future-0.18.2-py3-none-any.whl size=491070 sha256=9ea3223ae004e081f0a7b86be8648b2b422313e9055d2c830378226981440454
16:28:02    Stored in directory: /Users/gzapodea/.jenkins/workspace/SDA as Code/.cache/pip/wheels/22/73/06/557dc4f4ef68179b9d763930d6eec26b88ed7c389b19588a1c
16:28:02  Successfully built future
16:28:02  Installing collected packages: fastjsonschema, wrapt, urllib3, PyYAML, python-dotenv, pyjwt, pycparser, idna, future, charset-normalizer, certifi, requests, deprecated, cffi, requests-toolbelt, pynacl, cryptography, pyopenssl, PyGithub, dnacentersdk

16:28:30  Successfully installed PyGithub-1.55 PyYAML-6.0 certifi-2022.5.18.1 cffi-1.15.0 charset-normalizer-2.0.12 cryptography-37.0.2 deprecated-1.2.13 dnacentersdk-2.4.10 fastjsonschema-2.15.3 future-0.18.2 idna-3.3 pycparser-2.21 pyjwt-2.4.0 pynacl-1.5.0 pyopenssl-22.0.0 python-dotenv-0.20.0 requests-2.28.0 requests-toolbelt-0.9.1 urllib3-1.26.9 wrapt-1.14.1
16:28:30  WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
16:28:30  You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
16:28:30  [Pipeline] echo
16:28:30  
16:28:30  
16:28:30  Verify Python version and Libraries:..............................
16:28:30  [Pipeline] sh

16:28:31  + python --version
16:28:31  Python 3.10.5

16:28:31  [Pipeline] sh
16:28:32  + pip3 list

16:28:34  Package            Version
16:28:34  ------------------ -----------
16:28:34  certifi            2022.5.18.1
16:28:34  cffi               1.15.0
16:28:34  charset-normalizer 2.0.12
16:28:34  cryptography       37.0.2
16:28:34  Deprecated         1.2.13
16:28:34  dnacentersdk       2.4.10
16:28:34  fastjsonschema     2.15.3
16:28:34  future             0.18.2
16:28:34  idna               3.3
16:28:34  pip                22.0.4
16:28:34  pycparser          2.21
16:28:34  PyGithub           1.55
16:28:34  PyJWT              2.4.0
16:28:34  PyNaCl             1.5.0
16:28:34  pyOpenSSL          22.0.0
16:28:34  python-dotenv      0.20.0
16:28:34  PyYAML             6.0
16:28:34  requests           2.28.0
16:28:34  requests-toolbelt  0.9.1
16:28:34  setuptools         58.1.0
16:28:34  urllib3            1.26.9
16:28:34  wheel              0.37.1
16:28:34  wrapt              1.14.1
16:28:34  WARNING: You are using pip version 22.0.4; however, version 22.1.2 is available.
16:28:34  You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
16:28:34  [Pipeline] echo
16:28:34  
16:28:34  
16:28:34  Verify Application Files:..............................
16:28:34  [Pipeline] sh

16:28:35  + ls dnacenter_jenkins_automations/
16:28:35  CODE_OF_CONDUCT.md
16:28:35  CONTRIBUTING.md
16:28:35  LICENSE
16:28:35  NOTICE
16:28:35  README.md
16:28:35  create_fabric.py
16:28:35  device_inventory.py
16:28:35  environment.env
16:28:35  fabric_operations.yml
16:28:35  inventory
16:28:35  jenkinsfile_fabric
16:28:35  jenkinsfile_inventory
16:28:35  requirements.txt
16:28:35  [Pipeline] }
16:28:35  [Pipeline] // withEnv
16:28:35  [Pipeline] }
16:28:35  [Pipeline] // stage

16:28:35  [Pipeline] stage
16:28:35  [Pipeline] { (Identify if new config file)
16:28:36  [Pipeline] fileExists
16:28:36  [Pipeline] echo
16:28:36  New fabric config file found..............................
16:28:36  [Pipeline] }

16:28:37  [Pipeline] // stage
16:28:37  [Pipeline] stage
16:28:37  [Pipeline] { (Review the fabric config)
16:28:37  [Pipeline] fileExists
16:28:37  [Pipeline] echo
16:28:37  
16:28:37  
16:28:37  "fabric_operations.yml":..............................
16:28:37  [Pipeline] withEnv
16:28:37  [Pipeline] {
16:28:37  [Pipeline] echo
16:28:37  
16:28:37  
16:28:37  Verify Working Path:..............................
16:28:37  [Pipeline] sh

16:28:38  + pwd
16:28:38  /Users/gzapodea/.jenkins/workspace/SDA as Code
16:28:38  [Pipeline] dir
16:28:38  Running in /Users/gzapodea/.jenkins/workspace/SDA as Code/dnacenter_jenkins_automations
16:28:38  [Pipeline] {
16:28:38  [Pipeline] sh

16:28:39  + cat fabric_operations.yml
16:28:39  area_info:
16:28:39    name: OR
16:28:39    hierarchy: Global
16:28:39  
16:28:39  building_info:
16:28:39    name: LO
16:28:39  
16:28:39  floor_info:
16:28:39    name: Floor-3
16:28:39  
16:28:39  devices_info:
16:28:39    device_ips: [10.93.141.20, 10.93.141.28, 10.93.141.19]
16:28:39    device_roles: [control-plane, border, edge]
16:28:39  
16:28:39  fabric_info:
16:28:39    name: Floor-3
16:28:39  
16:28:39  ip_transit_pool:
16:28:39    name: LO_transit_pool
16:28:39    type: Generic
16:28:39    subnet: 10.1.4.0/24
16:28:39    gateway: 10.1.4.1
16:28:39    dhcp_server: 10.93.141.46
16:28:39    address_family: IPv4
16:28:39  
16:28:39  l3_vn:
16:28:39    name: Servers
16:28:39  
16:28:39  control_plane_devices:
16:28:39    ip: [10.93.141.20]
16:28:39  
16:28:39  border_devices:
16:28:39    ip: [10.93.141.28]
16:28:39    routing_protocol: BGP
16:28:39    internal_bgp_as: 65001
16:28:39    external_bgp_as: 65002
16:28:39    external_interface: TenGigabitEthernet1/1/1
16:28:39    transit_network: IP_Transit
16:28:39    transit_vlan: 602
16:28:39  
16:28:39  edge_devices:
16:28:39    ip: [10.93.141.19]
16:28:39  
16:28:39  auth_profile:
16:28:39    name: No Authentication
16:28:39  [Pipeline] }

16:28:39  [Pipeline] // dir
16:28:39  [Pipeline] }
16:28:40  [Pipeline] // withEnv
16:28:40  [Pipeline] }
16:28:40  [Pipeline] // stage
16:28:40  [Pipeline] stage
16:28:40  [Pipeline] { (Create Fabric, add CP, BN, EN)
16:28:40  [Pipeline] fileExists
16:28:40  [Pipeline] echo
16:28:40  
16:28:40  
16:28:40  Create a new fabric and add devices to the fabric:..............................

16:28:40  [Pipeline] withEnv
16:28:41  [Pipeline] {
16:28:41  [Pipeline] echo
16:28:41  
16:28:41  
16:28:41  Verify Working Path:..............................
16:28:41  [Pipeline] sh
16:28:41  + pwd
16:28:41  /Users/gzapodea/.jenkins/workspace/SDA as Code

16:28:42  [Pipeline] dir
16:28:42  Running in /Users/gzapodea/.jenkins/workspace/SDA as Code/dnacenter_jenkins_automations
16:28:42  [Pipeline] {
16:28:42  [Pipeline] sh
16:28:43  + python3 create_fabric.py

16:28:45  INFO:root:  App "create_fabric.py" run start, 2022-06-10 16:28:45

16:28:47  INFO:root:  Creating new fabric at site:Global/OR/LO/Floor-3

16:29:06  INFO:root:  Assign L3 Virtual Network: Servers

16:29:10  INFO:root:  Adding default auth profile to fabric: No Authentication

16:29:23  INFO:root:  Adding control plane devices to fabric: 10.93.141.20

16:29:30  INFO:root:  Adding a border node device: 10.93.141.28

16:29:36  INFO:root:  Adding edge node devices to fabric: 10.93.141.19

16:29:43  INFO:root:  App "create_fabric.py" end, : 2022-06-10 16:29:42
16:29:43  [Pipeline] }
16:29:43  [Pipeline] // dir
16:29:43  [Pipeline] }

16:29:43  [Pipeline] // withEnv
16:29:43  [Pipeline] }
16:29:44  [Pipeline] // stage
16:29:44  [Pipeline] stage
16:29:44  [Pipeline] { (Declarative: Post Actions)
16:29:44  [Pipeline] echo
16:29:44  
16:29:44  
16:29:44  Jenkins Device Inventory build end
16:29:44  [Pipeline] cleanWs
16:29:44  [WS-CLEANUP] Deleting project workspace...
16:29:44  [WS-CLEANUP] Deferred wipeout is used...

16:29:44  [WS-CLEANUP] done
16:29:44  [Pipeline] }
16:29:45  [Pipeline] // stage
16:29:45  [Pipeline] }
16:29:45  [Pipeline] // timeout
16:29:45  [Pipeline] }
16:29:45  [Pipeline] // withEnv
16:29:45  [Pipeline] }

16:29:45  [Pipeline] // withCredentials
16:29:45  [Pipeline] }
16:29:45  $ docker stop --time=1 e430227316f783011ca70268af90ae2e9aba064a0fa15e344db270196055b9ff

16:29:47  $ docker rm -f e430227316f783011ca70268af90ae2e9aba064a0fa15e344db270196055b9ff
16:29:48  [Pipeline] // withDockerContainer
16:29:48  [Pipeline] }
16:29:48  [Pipeline] // node
16:29:48  [Pipeline] End of Pipeline

16:29:49  Finished: SUCCESS
```

**License**

This project is licensed to you under the terms of the [Cisco Sample Code License](./LICENSE).



