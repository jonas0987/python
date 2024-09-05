  #1:---------
dict={
 "table":
 [
    "a piece of furniture"," list of fact & figure",
 ],
"cat":"a small animal"
 
}
print(dict)

# 2:--------

subject={"python","java","c++",'python',"java script","java","python","java","c++","c"}

c=(len(subject))

print("the minimum no   of room  requried for exam :",c)

# 3:------

dic={}

sub1=int(input("enter marks in your subject 1:-"))
sub2=int(input("enter marks in your subject 2:-"))
sub3=int(input("enter marks in your subject 3:-"))

dic.update({"marks in subject 1":sub1})
dic.update({"marks in subject 2":sub2})
dic.update({"marks in subject 3":sub3})

print(dic)


# 4:-----------

setA={("int",9),("float",9.0)}

setB={"9","9.0"}

print(setA)
print(setB)
