set={1,2,3,3,3,3,"hi","hello"}

print(set)

print(type(set))

print(len(set))

#  empty set:-----

set=set()
print(set)
print(type(set))


#  method:------

set.add(99)
print(set)

set.remove(3)
print(set)

set.clear()
print(set)


set1={1,2,3}
set2={1,3,5}

print(set2.difference(set1))

print(set1.union(set2))

print(set1.intersection(set2))