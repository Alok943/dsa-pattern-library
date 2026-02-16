# Hash Maps & Sets Pattern

## When to Use This Pattern
- Need O(1) lookup time
- Checking "have I seen this before?"
- Need to map one value to another
- Counting frequencies
- Finding pairs/complements

---

## Set vs Dictionary - Quick Reference

| Use Case | Data Structure | Why |
|----------|---------------|-----|
| Just checking existence | **Set** | Simpler, less memory |
| Need to store associated data | **Dictionary** | Can map key → value |
| Counting occurrences | **Dictionary** | Map number → count |
| Finding complements | **Dictionary** | Map number → index |

---

## Core Operations (Both O(1))

### Set
```python
seen = set()           # Create empty set
seen.add(5)           # Add element
if 5 in seen:         # Check existence
    print("Found!")
```

### Dictionary
```python
mapping = {}          # Create empty dict
mapping[5] = "value"  # Add key-value pair
if 5 in mapping:      # Check if key exists
    print("Found!")
value = mapping.get(5, "default")  # Safe access with default
```

---

## Pattern Recognition

### Pattern 1: "Have I seen this before?"
**→ Use a Set**
- Contains Duplicate
- First unique character

### Pattern 2: "What's the complement/pair?"
**→ Use a Dictionary (store value → index/data)**
- Two Sum
- Valid Anagram (letter → count)

### Pattern 3: "Count frequencies"
**→ Use a Dictionary (element → count)**
- Top K Frequent Elements
- Group Anagrams

---

## Key Insights

1. **Early Return Optimization**: If you find what you're looking for, return immediately. Don't keep looping.

2. **Build as You Go**: Don't populate the entire hash map first, then search. Check and add in the same loop.

3. **Space Trade-off**: Hash maps/sets use O(n) space but give you O(1) lookups. Worth it when you need speed.

---

## Problems Solved

### 1. Two Sum
- **Pattern**: Dictionary (number → index)
- **Key Idea**: Store complement, check if current number was someone's complement
- **Time**: O(n), **Space**: O(n)

### 2. Contains Duplicate  
- **Pattern**: Set (just existence check)
- **Key Idea**: Check if seen before adding
- **Time**: O(n), **Space**: O(n)

---

## Common Mistakes to Avoid

1. ❌ Using `for i in range(len(array))` when you don't need the index
   - ✅ Use `for item in array` instead

2. ❌ Building entire hash map first, then searching
   - ✅ Check and add in same pass

3. ❌ Using dictionary when set would work
   - ✅ If you only need existence, use set

4. ❌ Forgetting that `in` operator is O(1) for hash structures, O(n) for lists
   - ✅ Never use list for lookups in a loop

---

## Template Code

### "Have I Seen This?" Pattern
```python
def solve(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True  # or whatever you need to do
        seen.add(item)
    return False
```

### "Find Complement" Pattern  
```python
def solve(arr, target):
    mapping = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in mapping:
            return [mapping[complement], i]
        mapping[num] = i
    return []
```

---

## Next Patterns to Learn
- Two Pointers
- Sliding Window
- Fast & Slow Pointers
- Binary Search