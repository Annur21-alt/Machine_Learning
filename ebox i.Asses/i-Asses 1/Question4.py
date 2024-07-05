# Read input from the user
set1 = set(map(int, input().strip().split(',')))
set2 = set(map(int, input().strip().split(',')))

# Check subset relationships
is_set1_subset_of_set2 = set1.issubset(set2)
is_set2_subset_of_set1 = set2.issubset(set1)

# Check superset relationships
is_set1_superset_of_set2 = set1.issuperset(set2)
is_set2_superset_of_set1 = set2.issuperset(set1)

# Print the results
print(is_set1_subset_of_set2)
print(is_set2_subset_of_set1)
print(is_set1_superset_of_set2)
print(is_set2_superset_of_set1)
