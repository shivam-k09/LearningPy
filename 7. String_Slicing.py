#Slicing : Creating a sub string by extracting parts of another string ||||| Indexing [] or slice()
#Indexing syntax >>> [Start:Stop:Step]>>> Start is inclusive, Stop is exclusive, step is number of indexes to skip(default is 1, meaning normal count)

name = "Dastardly Phantom"

first_name = name[0:9]              # also name[:9]
last_name = name[10:17]             #also name[10:]
funky_name = name[0:17:2]           #also name[::2]... skiping one index
reverse_name = name[::-1]           #going backwards

print(first_name)
print(last_name)
print(funky_name)
print(reverse_name)

# Creating a slice object using slice() fuction with similar input arguments as above but seperated by comma

website1 = "http://google.com"
website2 = "http://wikipedia.com"

site_slice = slice(7,-4)                #Using nagative indexing as stop index argument to isolate the middle portion of the string

print(website1[site_slice])
print(website2[site_slice])
print()
