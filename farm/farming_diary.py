"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

from farm.corn import Corn


print("\n\n📝 Day One: Corn")

# 1. Instantiate a corn crop
corn = Corn()

# 2. Water the corn crop
corn.water()

# 3. Print "The corn crop produced ## grains"
print(f"The corn crop produced {corn.grains} grains")

# 4. Print "The corn crop is ripe" or "The corn crop is not ripe"
if corn.ripe():
    print(f"The corn crop is ripe ")
else:
    print(f"The corn crop is not ripe")

print("\n\n📝 Day Two: Rice")

# 1. Instantiate a rice crop
pass  # YOUR CODE HERE

# 2. Water the rice crop
pass  # YOUR CODE HERE

# 3. Transplant the rice crop
pass  # YOUR CODE HERE

# 4. Print "The rice crop produced ## grains"
pass  # YOUR CODE HERE

# 5. Print "The rice crop is ripe" or "The rice crop is not ripe"
pass  # YOUR CODE HERE
