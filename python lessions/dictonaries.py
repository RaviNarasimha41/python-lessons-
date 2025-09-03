# band = {
#          "ravi":"narasimha","fruits":"apple","bike":"hero",
#          "movie":"og"

# }

# print(band)
# print(type(band))

# band2=dict(mood="happy",vocal="plant")
# print(band2)

# #accessing item
# print(band.get("bike"))

# #key values
# print(band2.keys())

# print(band.values())

# #removing items 
# band.pop("ravi")
# print(band)

# #pop items 
# band.popitem()
# print(band)

# # del key word 
# del band["fruits"]
# print(band)

# sets 
thisset={"apple","orange","banana","papaya"}
fruits={"kiwi","grapes"}
print(thisset)

print(len(thisset))

#accesing item
for x in thisset:
    print(x)

print("banana" in thisset)
print("banana" not in thisset)

#adding item in set
thisset.add("cherry")
print(thisset)

thisset.update(fruits)
print(thisset)

#remove item in sets 
thisset.remove("banana")
print(thisset)

#join sets
one={1,2,3,4,5}
two={6,7,8,9,10}

three=one|two
print(three)

#join multiple sets 
set1={"a","b","c","d","e"}
set2={11,12,13,14,15}
set3={"ravi","sravan","guna"}

myset=set1|set2|set3

print(myset)