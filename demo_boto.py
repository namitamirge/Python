# Login to aws management console
# go to services
#3. Iam-users, groups, roles, policies

# session ---aws management console
import boto3


#creating variable for session for aws management console
aws_mg_con = boto3.session.Session(profile_name = 'nami') 
'''
#iam console will come when we acess management console
iam_con = aws_mg_con.resource('iam')

#list all IAm users
for each_user in iam_con.users.all():
    print(each_user.name)

#returning methods for iam console
print(dir(aws_mg_con))

#Printing services accessed using resourses method
print(aws_mg_con.get_available_resources())  #this resources method return only few services to access
'''

#accessing client 
iam_con = aws_mg_con.client(service_name='iam', region_name='us-west-2')
print(iam_con.list_users())         #gives dictionary output

#extracting UserName from client dictionary 
for each_user in iam_con.list_users()["Users"]:
    print(each_user["UserName"])

