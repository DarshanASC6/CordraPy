import getpass
import cordra
from lucenequerybuilder import Q
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt


host = "https://localhost"
obj_type = "debug"

username = "testuser1"
password = getpass.getpass()

# ········

file_1 = "example-data.csv"
payloads = {'p1': (file_1, open(file_1,'rb'))}

obj_1 = dict()
obj_1["name"] = "example 1"
obj_1["description"] = "an example of metadata for CSV payload"
obj_1["author"] = "John"

my_acl = dict()
my_acl["readers"] = ["public"]

response = cordra.Objects.create(
    host,
    obj_1,
    obj_type,
    username=username,
    password=password,
    verify=False,
    acls=my_acl,
    payloads=payloads)
print(response)



file_2 = "example-data.csv"
payloads = {'p1': (file_2, open(file_2,'rb'))}

obj_2 = dict()
obj_2["name"] = "example 2"
obj_2["description"] = "another example of metadata for CSV payload"
obj_2["author"] = "Tim"

my_acl = dict()
my_acl["readers"] = ["public"]

response = cordra.Objects.create(
    host,
    obj_2,
    obj_type,
    username=username,
    password=password,
    verify=False,
    acls=my_acl,
    payloads=payloads)
print(response)

q = Q('metadata')
my_results = cordra.Objects.find(host,str(q),verify=False)
print(my_results)



q = Q('/author','John')
my_results = cordra.Objects.find(host,str(q),verify=False)
obj_id_1 = my_results["results"][0]["id"]
print(my_results)



q = Q('/author','Tim')
my_results = cordra.Objects.find(host,str(q),verify=False)
obj_id_2 = my_results["results"][0]["id"]
print(my_results)




my_obj = cordra.Objects.read(host,obj_id_2,verify=False)
print(my_obj)


my_obj = cordra.Objects.read(host,obj_id_2,verify=False,full=True)
print(my_obj)


obj_payload_name = my_obj["payloads"][0]["name"]
print(obj_payload_name)


payload = cordra.Objects.read_payload(host,obj_id_2,obj_payload_name,verify=False)
print(payload)


df = pd.read_csv(StringIO(payload))
print(df)


df.plot.scatter(x='SAM0', y='SAM1')
plt.show()


response = cordra.Objects.update(
    host,
    obj_id_2,
    obj_json="I really need to write a better description for my data.",
    jsonPointer="/description",
    username=username,
    password=password,
    verify=False,
    dryRun=True,
    full=True)
print(response)


response = cordra.Objects.update(
    host,
    obj_id_2,
    obj_json={"SAM1":"Level of CXCR4 expression"},
    username=username,
    password=password,
    verify=False,
    dryRun=True,
    full=True)
print(response)


response = cordra.Objects.update(
    host,
    obj_id_2,
    acls={"readers":None,"writers":None},
    username=username,
    password=password,
    verify=False,
    full=True)
print(response)


my_obj = cordra.Objects.read(host,obj_id_2,verify=False,full=True)
print(my_obj)


my_obj = cordra.Objects.read(host,obj_id_2,username=username,password=password,verify=False,full=True)
print(my_obj)


response = cordra.Objects.delete(host,obj_id_1,username=username,password=password,verify=False)
print(response)

response = cordra.Objects.delete(host,obj_id_2,username=username,password=password,verify=False)
print(response)