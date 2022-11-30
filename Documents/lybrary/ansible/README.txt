*yaml 
	see tutorials/yaml.md

*setting up environment
	- you can use virtual machines or real machines or use cloud providers machines or mix of all of these. connection between acn and node is enough (if you clone virtual machines do not ferget to reset machine-id)
	- ansible control node with ansible python and ssh-client installed (optionally sshpass)
	- other nodes with sshd and python installed
	- (optionally) edit /etc/hosts file for name resolution if servers does not have 
	- make initial connections with nodes from acn (fow known hosts file) (you may want to add '[defaults]\n host_key_checking = False' to ansible.cfg file for not making initial connections but this is not recommended)
	- create ssh key and(you can use ssh-agent for passphrase or do not use passphrase for connections)
		- copy key files manually (ssh-copy-id)
		- copy key files automated (ansible --ask-pass) (install sshpass)
			- make sure authorized_keys file exists
			- ansible --ask-pass -i hosts.ini -m ansible.builtin.file -a "path=/home/ubuntu/.ssh/authorized_keys owner=ubuntu group=ubuntu mode='0600'" all
			- append your private-key to authorized_keys file
			- ansible --ask-pass -i hosts.ini -m ansible.builtin.shell -a "echo [public key file conents] >> /home/ubuntu/.ssh/authorized_keys" all
			- verify your key is there
			- ansible --ask-pass -i hosts.ini -m ansible.builtin.shell -a "cat /home/ubuntu/.ssh/authorized_keys" all
			- then connect with key
			- ansible -i hosts.ini -m ping (--private-key or --key-file) [private key file] all (or use ansible_ssh_private_key_file var in inventory and do not specify key file in command)
	- before configure sshd learn become and ask-become-pass privilege-escalation
	- configure sshd to (create a sshd_config file then copy or learn regex in ansible.builtin.replace examples)(after following steps you wont be able to ssh directly to the machines you control if ansible control node is not machine you are using. you could create one more ssh key for your machine too if you want to ssh directly)
		- Not permit root login
		- accept publickey authentication
		- do not accept password authentication
	- restart sshd service (service module)
	- make sure acn can ping nodes

*inventory
	see inventory.md

*ansible.cfg
	- uncomment and modify parameters you need from example ansible config 
		- create default ansible config (ansible-config init --disabled -t all > ansible.cfg)
		- online default ansible config (https://github.com/ansible/ansible/blob/stable-2.9/examples/ansible.cfg)
	- for example
		- inventory = /path/to/hosts.yml
		- forks     = 5 # 5 is default value for parallel jobs
		- private_key_file = /path/to/file # you can use this instead of --private-key parameter
		- remote_user = ansible
*ansible-doc
	- documentation for modules 
	- has good examples too
*playbooks
	- written in yaml format
	- name it with name tag
	- specify hosts with hosts tag
	- become root or not? become tag with yes or no
	- has tasks tag which you specify tasks to play
		- name of the task with name
		- module name as tag for exapmle ping tag or copy tag or service tag
	- has vars tag for variables
	- has handlers tag. almost dame as tasks but wont run on its own. you should call them with notify tag in tasks. then they will run after task completes. 
	- with vars_files tag you can put variables in different yaml files than only write file name for using taht variables

real world scenario

read ebook
