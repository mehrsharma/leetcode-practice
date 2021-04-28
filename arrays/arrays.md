# Summary of Array Problems

## 1. Two Sum
### Problem Description
**Given**
- integer array `nums`
- integer `target`

**Return**
- indices of two numbers such that they add up to `target`

Assume that each input would have exactly one solution, and you may not use the same element twice. Return the answer in any order.

### Solution Notes
Make a new dictionary that stores a value and its index. Create a variable `index` and increment it each time you loop. For each value in `nums`, check if
`target - nums` already exists in the new dictionary. If it does, then return the index of that value, along with the current index. If not, then add the current values of `nums` and `index` to the dictionary.

This is an O(n) solution. To make it cleaner, check out enumerate method.

---

## 2. Best Time to Buy and Sell Stock
### Problem Description
**Given**
- array `prices` where `prices[i]` is stock price on the ith day

**Return**
- maximum profit you can get from transaction

Maximize profit by picking a day to buy the stock and a different day in the future to sell that stock

### Solution Notes
Create variables `maxProfit` and `purchaseVal`. Go through `prices` and if any value is less than the current `purchaseVal`, update it. Otherwise, check if `prices[i] - purchaseVal` beats the current maximum profit. If it does, update this value. Return `maxProfit` at the end

This is an O(n) solution since it passes through `prices` just once.

---

## 3. Contains Duplicate
### Problem Description
**Given**
- integer array `nums`

**Return**
- `true` if any value appears at least twice
- `false` if every element is distinct

### Solution Notes
Solution1 (faster): puts array into a set, which will eliminate duplicate values. If the length of this set is the same as the length of the original array, then all values are distinct, otherwise they are not.

Solution2: sorts array and then passes through them and compares if any side by side values are the same (sort method has a O(nlogn) time complexity)
