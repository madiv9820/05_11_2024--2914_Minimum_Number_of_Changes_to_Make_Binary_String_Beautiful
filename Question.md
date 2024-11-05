# [2914. Minimum Number of Changes to Make Binary String Beautiful](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful)

__Type:__ Medium <br>
__Topics:__ String 
<hr>

You are given a __0-indexed__ binary string `s` having an even length.

A string is __beautiful__ if it's possible to partition it into one or more substrings such that:

- Each substring has an __even__ length.
- Each substring contains __only__ `1`'s or __only__ `0`'s.

You can change any character in `s` to `0` or `1`.

Return _the __minimum__ number of changes required to make the string_ `s` _beautiful_.
<hr>

### Examples

- __Example 1:__ <br>
__Input:__ s = "1001" <br>
__Output:__ 2 <br>
Explanation: We change s[1] to 1 and s[3] to 0 to get string "1100". <br>
It can be seen that the string "1100" is beautiful because we can partition it into "11|00". <br>
It can be proven that 2 is the minimum number of changes needed to make the string beautiful.

- __Example 2:__ <br>
__Input:__ s = "10" <br>
__Output:__ 1 <br>
__Explanation:__ We change s[1] to 1 to get string "11". <br>
It can be seen that the string "11" is beautiful because we can partition it into "11". <br>
It can be proven that 1 is the minimum number of changes needed to make the string beautiful.

__Example 3:__ <br>
__Input:__ s = "0000" <br>
__Output:__ 0 <br>
__Explanation:__ We don't need to make any changes as the string "0000" is beautiful already.
<hr>

### Constraints:

- <code>2 <= s.length <= 10<sup>5</sup></code>
- `s` has an even length.
- `s[i]` is either `'0'` or `'1'`.
<hr>

### Hints:
- For any valid partition, since each part consists of an even number of the same characters, we can further partition each part into lengths of exactly 2.
- After noticing the first hint, we can decompose the whole string into disjoint blocks of size 2 and find the minimum number of changes required to make those blocks beautiful.