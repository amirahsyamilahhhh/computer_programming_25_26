"""Session 2: practice variables, basic arithmetic, comparisons, type conversions, and adding a second flower.
Note: Variable names must match exactly because later sessions import these names.
"""

# Task 1: Print Flower Summary
id = "flower1"  # Task 2: Change this to "flower_2x"
print("\n=== Flower Summary ===")
print("ID:", id)

# Task 3: Define more variables for one Iris flower
id_flower = "flower1"
sepal_length = 5.1 
sepal_width = 3.5  
petal_length = 1.4   
petal_width = 0.2
species = "setosa"

# Task 3a: Uncomment the print statements below to see the values of the variables you defined
print ("=== Flower Summary ===")
print("ID:", id_flower)
print("Sepal Length:", sepal_length)
print("Sepal Width:", sepal_width)
print("Petal Length:", petal_length)
print("Petal Width:", petal_width)
print("Species:", species)

# Task 4: Compute petal area
petal_area = petal_length * petal_width
print("\nPetal Area:", petal_area)  

threshold = 2.0
feature_name = "petal_length"
positive_label = "setosa"
negative_label = "not_setosa"
label_key = "species"

# Task 5: Comparing with threshold
is_short_petal = petal_length < threshold
print(is_short_petal)

# Task 6: Print Flower 2 Summary
id = "flower2"  # Task 2: Change this to "flower_2x"
print("\n=== Flower Summary ===")
print("ID:", id)

#Task 7: Define Variables for flower 2
id_flower = "flower2"
sepal_length_2 = 5.1 
sepal_width_2 = 3.5  
petal_length_2 = 1.4   
petal_width_2 = 0.2
species_2 = "setosa"
print ("=== Flower Summary ===")
print("ID:", id_flower)
print("Sepal Length:", sepal_length_2)
print("Sepal Width:", sepal_width_2)
print("Petal Length:", petal_length_2)
print("Petal Width:", petal_width_2)
print("Species:", species_2)

#Task 8: Area of flower 2
petal_area_2 = petal_length_2 * petal_width_2
print("\nPetal Area:", petal_area_2)  

