import requests
import json

saral=requests.get("http://saral.navgurukul.org/api/courses")
data1=saral.json()
with open ("data1.json","w") as f:
    json.dump(data1,f,indent=2)


serial_no=1
for index1 in data1["availableCourses"]:
    print(serial_no,index1["name"],index1["id"])
    serial_no+=1
topic=int(input("WHICH TOPIC DO YOU WANT?? "))
print(data1["availableCourses"][topic-1]["name"]) 

parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+data1["availableCourses"][topic-1]["id"]+" "+"/exercises")
data=parents_data.json()
## dump parents data in json file XXXX
with open("parents_data.json","w") as fl:
    json.dump(data,fl,indent=2)
course=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)") 
if course=="p"   :   
    saral=requests.get("http://saral.navgurukul.org/api/courses")
    data1=saral.json()
    with open ("data1.json","w") as f:
        json.dump(data1,f,indent=2)


    serial_no=1
    for index1 in data1["availableCourses"]:
        
        print(serial_no,index1["name"],index1["id"])
        serial_no+=1
    topic=int(input("WHICH TOPIC DO YOU WANT?? "))
    print(data1["availableCourses"][topic-1]["name"]) 

    parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+data1["availableCourses"][topic-1]["id"]+" "+"/exercises")
    data=parents_data.json()
    ## dump parents data in json file XXXX
    with open("parents_data.json","w") as fl:
        json.dump(data,fl,indent=2)
##########################################################################################################3
index_1=1
data1=data["data"]
for index_2 in data1:
    print(index_1,index_2["name"])
    index_1+=1
    i=1
    # topiclst=[]
    if (index_2["childExercises"])==0:
        # topiclst.append(index_2["name"])
        print(" ",i,index_2["slug"])
        i=i+1
    else:
        s_num2=1 
        print(" ",i,".",index_2["name"])
        Child=index_2["childExercises"]
        # topiclst.append(index_2["name"])
        for index_3 in Child:
            print(" ",s_num2,index_3["name"])
            s_num2+=1
           
            
same_course=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)")
if same_course=="p":    
    index_1=1
    data1=data["data"]
    # topiclst=[]
    for index_2 in data1:
        print(index_1,index_2["name"])
        index_1+=1
        i=1
        # topiclst=[]
        if index_2(["childExercises"])==0:
            # topiclst.append(index_2["name"])
            print(" ",i,index_2["slug"])
            i=i+1
        else:
            s_num2=1 
            print(" ",i,".",index_2["name"])
            Child=index_2["childExercises"]
            # topiclst.append(index_2["name"])
            # print(topiclst)
            for index_3 in Child:
                print(" ",s_num2,index_3["name"])
                s_num2+=1      
# print(topiclst)                  
                
##############################################################    
course_name=int(input("Enter in which topic you wants to go:"))
Data=data["data"][course_name-1]["childExercises"]
indexa=1
quelst=[]
slug_list=[]
for index_4 in Data:
    quelst.append(index_4["name"])
    print("  ",indexa,index_4["name"])
    indexa+=1
print(quelst)    

slug=int(input("WHICH QUESTION DO YOU WANT?? ......."))  
for i in range(len(quelst)): 
    que=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)") 
    if que =="n":
        slugid=Child[slug]["id"]
        ChildSlugName=Child[slug]["slug"]
        slugdata=requests.get("http://saral.navgurukul.org/api/courses/"+slugid+"/exercise/getBySlug?slug="+str(ChildSlugName))
        data8=slugdata.json()
        with open("slugdata","w") as file:
            json.dump(data8,file,indent=8)
                    # l.append(data8["content"])
            print(data8["content"]) 
            slug=slug+1
            
    if que=="p":
        slugid=Child[slug-1]["id"]
        ChildSlugName=Child[slug-1]["slug"]
        slugdata=requests.get("http://saral.navgurukul.org/api/courses/"+slugid+"/exercise/getBySlug?slug="+str(ChildSlugName))
        data8=slugdata.json()
        with open("slugdata","w") as file:
            json.dump(data8,file,indent=8)
                    # l.append(data8["content"])
            print(data8["content"]) 

else:
    s_no=1
    print(" ",s_no,data["data"][slug-1]["slug"])
    slug_list.append(data["data"][slug-1]["slug"])
    slugid=Child[slug]["id"]
    ChildSlugName=Child[slug]["slug"]
    slugdata=requests.get("http://saral.navgurukul.org/api/courses/"+slugid+"/exercise/getBySlug?slug="+str(ChildSlugName))
    data8=slugdata.json()
  
    # v=requests.get("http://saral.navgurukul.org/api/courses/"+str(data1["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["slug"]))
    # d=v.json()
    with open("questions.json","w") as f:
        json.dump(data8,f,indent=4)
        print(data8["content"])
    for i in range(len(slug_list)):
        a=input("Enter whether you want to go next or previous:(n/p)")
        if a=="n":
            print("Next page.")
            break
        if a=="p":
            print("No more questions.")
            break