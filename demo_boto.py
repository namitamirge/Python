# Login to aws management console
# go to services
#3. Iam-users, groups, roles, policies

# session ---aws management console
import boto3


#creating variable for session for aws management console
aws_mg_con = boto3.session.Session(profile_name = 'nami') 

#iam console will come when we acess management console
iam_con = aws_mg_con.resource('iam')

#list all IAm users
for each_user in iam_con.users.all():
    print(each_user.name)
