# Day 8: Lists & List Operations

## Morning Session: Theory

Today i learnt about **Python Lists**. Lists are ordered collection and they can store many different types of data. They are mutable so we can change values after creating it.
Some examples of lists:

```python
mylist = [1, "hello", 3.5, True]
```


 **Common list methods** :

* `append()` → add item at the end
* `insert()` → insert at certain index
* `remove()` → remove first occurance of item
* `pop()` → remove item by index, default last one
* `sort()` → sort items, works only if all same type
* `reverse()` → reverse the list
* `clear()` → remove all items

 **List slicing** :

We can get sublists by `[start:end:step]`.

* negative index works like `-1` for last item
* Example: `mylist[1:4]`, `mylist[::-1]`

 **List comprehensions** :

Concise way to create list from iterable.

<pre class="overflow-visible! px-0!" data-start="993" data-end="1042"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>squares = [x**</span><span>2</span><span></span><span>for</span><span> x </span><span>in</span><span></span><span>range</span><span>(</span><span>10</span><span>)]
</span></span></code></div></div></pre>

 **When to use lists** :

* When data is sequential or ordered
* When we need index access
* When size is not too big (for large data dict or numpy is better)

## Afternoon Session: Practical Tasks

### Task 1: Student Grade Manager

* Create two list: one for student names and one for grades
* Add, remove, update grade, calculate average
* Find highest and lowest grades
* Sort descending to get top 3
* Use list comprehension to filter students above/below average

Example mistake i noticed: sometimes i forget to update both lists when removing student.
