# 20220915 - Python - Python Advanced - Tuples and Sets


# Sets are UNORDERED MUTABLE collections of data with UNIQUE elements


print('\n------------- Set Operators ---------------\n')


a = set([1, 2, 3, 4])                   # Set from a list
print(a)

b = set([3, 4, 5, 6])
print(b, '\n')

print(a | b)        # {1, 2, 3, 4, 5, 6} - Union (combines 'a' and 'b')
print(a & b)        # {3, 4}             - Intersection (finds the elements contained in 'a' and in 'b')
print(a < b)        # False              - Subset (is 'a' subset of 'b')
print(a > b)        # False              - Superset (Is 'a' superset of 'b')
print(a - b)        # {1, 2}             - Difference (elements from 'a' in 'a' but not in 'b')
print(a ^ b)        # {1, 2, 5, 6}       - Symmetric Difference (elements from 'a' not in 'b' AND elements in 'b' but not in 'a')


print('\n------------- Set Methods ----------------\n')


a = set([1, 2, 3, 4])
print(a)

b = set([3, 4, 5, 6])
print(b, '\n')

print(a.union(b))			            # Equivalent to 'a | b'
print(a.intersection(b))                # Equivalent to 'a & b'
print(a.issubset(b))                    # Equivalent to 'a <= b'
print(a.issuperset(b))                  # Equivalent to 'a >= b'
print(a.difference(b))                  # Equivalent to 'a - b'
print(a.symmetric_difference(b))        # Equivalent to 'a ^ b' (The exact opposite of Intersection 'a & b')


print('\n--------------- Methods ----- .discard() ----- .remove() ---------')


test_set = {1, 2, 3}
print(test_set)
print(type(test_set))

print(test_set.discard(2))              # None (returns nothing), removes the specified element and no Error if the element is not part of the set
print(test_set)

print(test_set.remove(1))               # None (returns nothing), removes the specified element and Error if the element is not present in the set
print(test_set)

print(test_set.add(4))                  # None (returns nothing), adds element if not present in the set, if present -> no effect
print(test_set)

print(test_set.update() )
