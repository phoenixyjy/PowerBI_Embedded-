#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


def getAccessToken (username, password, clientId):

    url =  'https://login.microsoftonline.com/common/oauth2/token'

    headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }

    body = {
          'grant_type':'password',
          'client_id': clientId,
          'resource':'https://analysis.windows.net/powerbi/api',
          'scope':'openid',
          'username':username,
          'password':password
        }

    response = requests.post(url=url, headers=headers, data=body)    
    return response.json()['access_token']   


# In[3]:


def getEmbedToken(accessToken, groupId, reportId):

    url = "https://api.powerbi.com/v1.0/myorg/groups/{0}/reports/{1}/GenerateToken"        .format(groupId, reportId)
        
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'authorization' : "Bearer {0}".format(accessToken)
    }
    
    body = {'accessLevel':'View'}
    
    response = requests.post(url=url, headers=headers, data=body)   
    return response.json()['token']


# In[4]:


def getPowerBIEmbedParam(username, password, clientId, groupId, reportId):
    accessToken = getAccessToken(username, password, clientId)
    embedToken = getEmbedToken(accessToken, groupId, reportId)
    embedURL = "https://app.powerbi.com/reportEmbed?reportId={0}&groupId={1}".format(reportId, groupId)
    
    print(embedToken)
    print(embedURL)
    print(reportId)


# In[ ]:



getPowerBIEmbedParam(username, password, 'client_id','group_id','report_id')

