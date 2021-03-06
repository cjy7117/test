#from ironicclient import client
from novaclient import client as nClient
from glanceclient import client as gclient

import keystoneclient.v2_0.client as kclient
from keystoneauth1 import loading


#from novaclient import GlanceManager


from keystoneauth1.identity import v2
from keystoneauth1 import session
#from keystoneclient.v3 import client

import os

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_name'] = os.environ['OS_TENANT_NAME']
    return d





#kwargs = {'os_username': 'cjy7117',
#          'os_password': 'Wait4aTrain7!',
#          'os_auth_url': 'https://chi.tacc.chameleoncloud.org:5000/v2.0',
#          'os_project_name': 'CH-819321'}

#ironic = client.get_client(1, **kwargs)

#ironic.node.list()


#nova = nclient.Client('2',
#                     username = 'cjy7117',
#                     password = 'Wait4aTrain7!',
#                     project_name = 'CH-819321',
#                     auth_url = 'https://chi.tacc.chameleoncloud.org:5000/v2.0')

#flavers = nova.flavors.list()
#for f in flavers:
#    print (f)
#images = nova.images.list()
#for i in images:
#    print (i)


#flavor = nova.flavors.get('baremetal')
#image = nova.images.find(name='CC-Ubuntu14.04-Docker')


#auth = v3.Password(auth_url = 'https://chi.tacc.chameleoncloud.org:5000',
#                   username = 'cjy7117',
#                   password = 'Wait4aTrain7!',
#                   project_name = 'CH-819321')

auth = v2.Password(auth_url = 'https://chi.tacc.chameleoncloud.org:5000/v2.0',                                                   
                   username = 'cjy7117',                                                                  
                   password = 'Wait4aTrain7!',                                                                                            
                   tenant_name = 'CH-819321')

#loader = loading.get_plugin_loader('password')

#auth = loader.load_from_options(auth_url = 'https://chi.tacc.chameleoncloud.org:5000/v3',
#                                username = 'cjy7117',
#                                password = 'Wait4aTrain7!',
#                                project_name = 'CH-819321')


sess = session.Session(auth=auth)

#3ks = kclient.Client(session=sess)
#users = ks.tenants.list()

nova = nClient.Client('2', sess)
#creds = get_nova_creds()
#nova = nclient.Client("2", **creds)

nova.servers.list()

#glance = gclient.Client('2', sess)
#glance.images.list()

#keystone = client.Client(session=sess)


#GlanceManager.list()

#print(flavor)
#print(image)
