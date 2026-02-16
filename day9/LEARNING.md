# Day 9: Tuples & Sets - Learning.md

## 1. Tuples

**Definition**: Tuples are immutable sequences in Python. Once created, elements cannot be changed.

**Characteristics:**

- Ordered collection
- Can contain duplicates
- Faster than lists because they are immutable

**Use Cases:**

- Storing fixed collections (coordinates, configurations)
- Returning multiple values from functions

**Examples:**

```python
# Tuple creation
point = (10, 20, 30)

# Tuple unpacking
x, y, z = point

# Returning multiple values
def min_max(lst):
    return min(lst), max(lst)
low, high = min_max([4, 7, 1, 9])
```
