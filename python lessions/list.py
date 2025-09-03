users = ['ravi','sravan','guna']
data =['ravi',33,True]
emptylist=[]
print("ravi"in emptylist)
print(users[0])
print(users[-1])

print(len(data))
print(len(users))
print(len(emptylist))

users.append("kumar")
print(users)
users.extend(["raghu , nithin"])
print(users)
users.insert(0,'vinay')
print(users)
users.remove('vinay')
print(users)

nums=[1,6,8,9,0,9,0]
nums.sort()
print(nums)

#tuple
mytuple=tuple(('ravi',3,'sravan'))
anothertuple=(1,6,7,8,9)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("vinay")
print(newlist)
print(mytuple)