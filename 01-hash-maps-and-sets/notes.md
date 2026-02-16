# Hash Maps & Sets

## When to Use
- "Have I seen this?" → **Set**
- "Find complement/pair" → **Dict** (value→index)
- "Count frequencies" → **Dict** (item→count)

## Syntax
```python
# Set
seen = set()
seen.add(5)
if 5 in seen: ...

# Dictionary
mapping = {}
mapping[5] = "value"
if 5 in mapping: ...
mapping.get(5, 0)  # Returns 0 if key doesn't exist
```

## Key Insights
1. **Build as you go** - Check and add in same loop
2. **Early return** - Return immediately when found
3. **O(1) lookup** - Hash structures vs O(n) for lists

## Cleaner Code Tips
```python
# ❌ Don't do this
for i in range(len(arr)):
    item = arr[i]

# ✅ Do this
for item in arr:
    ...

# ❌ Don't do this
if condition:
    return True
return False

# ✅ Do this
return condition

# ❌ Don't do this (frequency counting)
if char in count:
    count[char] += 1
else:
    count[char] = 1

# ✅ Do this
count[char] = count.get(char, 0) + 1
```

## Problems Solved
1. **Two Sum** - Dict (num→index), O(n)/O(n)
2. **Contains Duplicate** - Set, O(n)/O(n)
3. **Valid Anagram** - Dict (char→count), O(n)/O(n)