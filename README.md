#Install Ansible
apt-get install ansible

#Run start_app.yaml with your host list or localhost. 
ansible-playbook -i 'localhost,' start_app.yaml -e 'ansible_connection=local'

