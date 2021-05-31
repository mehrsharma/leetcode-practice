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
**Solution1 (faster):** puts array into a set, which will eliminate duplicate values. If the length of this set is the same as the length of the original array, then all values are distinct, otherwise they are not.

**Solution2:** sorts array and then passes through them and compares if any side by side values are the same (sort method has a O(nlogn) time complexity)

---

## 4. Product of Array Except Self
### Problem Description
**Given**
- integer array `nums`

**Return**
- Array of values `finalArray` that are the total product of `nums` excluding the current value

### Solution Notes
2 pass solution, first create empty `finalArray[]`, an integer value `numZeros` to count the number of zeroes, and a `product` value set equal to 1. Now, pass through the `nums` and multiply original product value with the current one you're on. If this value is a zero, do not do the last step, and instead increment `numZeros`. After this, we know if `numZeros >= 2`, then the product of all the values excluding themselves are zero, so set product equal to 0.

Now, on our second pass through the array, if `numZeros == 0` then we can add `product/nums[x]` to finalArray. If `numZeros != 0 and nums[x] != 0` we append 0 to `finalArray` since we know that anything multiplied by 0 is 0. Finally, if `nums[x] == 0`, then we append the product, since it is calculated omitting zeros.

This approach is O(2n) and omits division by 0.

---
