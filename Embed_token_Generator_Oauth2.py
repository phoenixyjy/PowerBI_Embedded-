#!/usr/bin/env python
# coding: utf-8

# In[1]:


#reportId = ''
client_secret = ''
tenantId = ''
clientId = ''
groupId = ''


# In[2]:


import requests
import argparse

# In[3]:


def getAccessToken(client_secret, tenantId, clientId):

    url =  'https://login.microsoftonline.com/%s/oauth2/token'%(tenantId)

    headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }

    body = {
        'grant_type':'client_credentials',
        'client_id': clientId,
        'client_secret': client_secret,
        'resource':'https://analysis.windows.net/powerbi/api',
        'tenantId': tenantId,
        'scope':'openid'
        }
    response = requests.post(url=url, headers=headers, data=body)    
    return response.json()['access_token']


# In[4]:


def getEmbedToken(accessToken, groupId, reportId):
    url = "https://api.powerbi.com/v1.0/myorg/groups/{0}/reports/{1}/GenerateToken"        .format(groupId, reportId)
        
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'authorization' : "Bearer {0}".format(accessToken)
    }
    
    body = {'accessLevel':'View'}
    
    response = requests.post(url=url, headers=headers, data=body)   
    return response.json()['token']



# In[5]:


def getPowerBIEmbedParam(client_secret, tenantId, clientId, groupId, reportId):
    accessToken = getAccessToken(client_secret, tenantId, clientId)
    embedToken = getEmbedToken(accessToken, groupId, reportId)
    embedURL = "https://app.powerbi.com/reportEmbed?reportId={0}&groupId={1}".format(reportId, groupId)
    
    print("embedToken: ",embedToken,'\n')
    print("embedURL: ",embedURL,'\n')
    print("reportId: ",reportId,'\n')


# In[ ]:


parser = argparse.ArgumentParser(description='Embed token generator')
parser.add_argument('--rt', help='directory, required, no default values, enter break to quit', required = True)
args = parser.parse_args()

reportId = args.rt
getPowerBIEmbedParam(client_secret, tenantId, clientId, groupId, reportId)

