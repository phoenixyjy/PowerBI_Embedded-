# PowerBI_Embedded

## Backgroud
If you want to publish your Power BI reports, there are several ways you can do this:
1. Publish the report to the website or portal by means of iframe/url
    
    This method requires the views to log-in, and they must have permission to access and view the report
2. Publish the report to the public in form of iframe or url

    This method is similar to the previous one, however, permission is not required to view the report. This could create data leakage problems.
3. Embed your code into your own developing envirnment, and make it becomes a part of your project.

    This method is called PowerBI embedded. It is another service provided by Microsoft. It is really tricky to set up in the beginning, and I've spent a lot of time figuring out how have everything ready.
**PS**: PowerBI Embedded has an extra charge.

## Description
Embedded token, embedded url and report ID are three essential elements that allow your application to retrive the report from Power BI server. However, none of the tutorials has done a good job describing how to get them.
The code I've compiled had coped with this hassle. It will sent request to Power BI and use the authentication to request access token. Once the access token is generated, we can use the access token to generate the embedded token.
**Note**: The access token is only valid for one hour. So if you need the report to be shown in your application. You will need to constantly request the access token.
 When calling for access token, there are two methods of authentication:
 1. login with username and password. This is not recommended by MS
 2. Oauth 2.0. This is the best solution, but you need some set ups to have the secreat key
 
## pre-requisite
You will need several inforamtion before calling an access token with oauth 2 authentication method
1. client_secret
2. tenantId
3. clientId
4. groupId
5. report id

You will need several information in order to generate the access token with username and password
1. username
2. password
3. reportid
4. group id

All those detail can be obtained from Azure and Power BI server
## Implementation
After obtaining the access token, we need to use the access token to generate the embedded Token. With embedded token, we will be able to embed in the application in our own development. We also need the Power BI SDK for report control (e.g. setting slicer state)

The SDK can be downloaded at:https://github.com/Microsoft/PowerBI-JavaScript/blob/master/dist/powerbi.js

I've attached an HTML code to show all the entire procedure works. Just copy the embedded token into the HTML. 
**Note: the embedded token is only valid for 1 hour, we need constantly refresh the code to generate the newest token**

**This script is using client_secret as the authentication process**

**This procedure can also be done in Postman**
