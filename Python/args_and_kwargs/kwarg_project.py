
#step 1
def save_user_data(name,**kwargs):
    #print("name is ",name)
    #print("kwargs are",kwargs)

    data=""
    #{name:"John","age":23}
    for key in kwargs:
        #print("The key is",key)
        value=kwargs[key]
        #print("the value is",value)
        data=data+f"{key}:  {value}\n"
    with open(f"{name}.txt","w") as file:
        file.write(data)


#save_user_data("John",age=23,fav_color="all")

def collect_user_data():
    name=input("Enter your name:")
    print("------------------")
    print("You can fill your bio ")
    print("Enter categories and values")<
    print("done to exit")
    print("----------------------")
    user_data={}
    while True:
        
        category_name=input("Enter category name:")
        if category_name=="done":
            break
        category_description=input("Enter description:")
        user_data[category_name]=category_description
        #print(user_data)#
    save_user_data(name,**user_data)

collect_user_data()


