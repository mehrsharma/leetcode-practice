# Summary of Array Problems

---

## Two Sum
### Problem Summary
Given an array of integers `nums` and an integer `target`
 **Return indices of two numbers such that they add up to `target`.**

Assume that each input would have exactly one solution, and you may not use the same element twice. Return the answer in any order.

####Solution Outline:
Make a new dictionary that stores a value and its index. Create a variable `index` and increment it each time you loop. For each value in `nums`, check if
`target - nums` already exists in the new dictionary. If it does, then return the index of that value, along with the current index. If not, then add the current values of `nums` and `index` to the dictionary.

####Notes on Solution:
This is an O(n) solution. To make it cleaner, check out enumerate method.

---
