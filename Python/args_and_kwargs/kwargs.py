#kwargs->key word arguments
#dict or js object from js
#acces object bracke or dot notation
#in python dictionary use only bracker
# args->number of inputs or arguments go into function tuple:list
#kwargs->number of inputs: input is labled
def check_the_magic(**kwargs):
    print(f"The data type is: {type(kwargs)}")
    print(f"The content is: {kwargs}")
    print(f"Location is: ",{kwargs["location"]})

#kwargs destcturcted
#they can also be arguments
def check_the_magic2(name,age,location):
    print(f"name ",name)
    print(f"age ",age)
    print(f"location ",location)


#order is args then kwargs
check_the_magic(location="Kenya",name="Joseph",age=34,favCountry="Saudi Arabia")#work
#check_the_magic2("Kenya","Joseph",34,)#will not work