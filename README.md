# Minimum Changes to Make Binary String Beautiful (All Approaches)

**Referal Video Explanation (Not a Paid Promotion)** - [Minimum Number of Changes to Make Binary String Beautiful - Leetcode 2914 - Python](https://youtube.com/watch?v=qhxhrTA4HJw)
<hr>

- ## Approach 1:- Pairwise Comparison (Greedy)

    - ### Intuition
        The problem you're solving likely involves making changes to a string, ensuring that some pattern or condition is satisfied, where mismatches need to be corrected. A common interpretation of such problems is to count the number of "interchanges" (or changes) required to achieve a desired structure or arrangement of characters in the string.

        In this particular case, the string might need to satisfy the rule that characters at **odd indices** (1-based indexing) must match characters at **even indices** (or some similar pattern). For example, you might need characters at positions 0, 2, 4, ... to match the characters at positions 1, 3, 5, ...

        The core idea behind this approach is to:
        - Traverse through the string using two pointers.
        - Compare characters at positions that are supposed to form groups (in this case, even and odd indexed characters).
        - If a mismatch is detected, count it as an interchange (change required).
        - Continue this process until the entire string has been processed.

    - ### Approach

        1. **Initialize Pointers and Counters:**
            - You initialize a pointer `left_Ptr` to track the character in the "even" position group (0-based index).
            - `right_Ptr` is used to traverse through the entire string.
            - You also initialize a counter `total_InterChanges` to count how many changes are needed.

        2. **Iterate Through the String:**
            - As you loop through the string using `right_Ptr`, you compare each character at `right_Ptr` with the character at `left_Ptr`.
            - If they are different, you may need an interchange, depending on whether `right_Ptr` is an odd index. This is determined using `right_Ptr & 1` (a bitwise operation to check if `right_Ptr` is odd).
            - If `right_Ptr` is odd, increment the `total_InterChanges` counter, because a change would be needed to fix this mismatch.
            - Move `left_Ptr` to the current `right_Ptr` to continue processing the next pair of characters.

        3. **Return the Count:**
            - Finally, after looping through the entire string, return `total_InterChanges` to give the number of changes required to make the string valid according to the specified rule.

    - ### Time Complexity

        - **Time Complexity:**  
            - The approach iterates through the string exactly once, comparing each character at `right_Ptr` with the character at `left_Ptr`. This results in a time complexity of **O(n)**, where `n` is the length of the string.
        
            - Since there is only a single loop that processes each character once, and all operations inside the loop (comparisons and updates) are constant time operations, the time complexity remains linear with respect to the size of the input.

    - ### Space Complexity
        - **Space Complexity: O(1)**
            - The algorithm only uses a fixed amount of space for variables left_Ptr, total_InterChanges, and right_Ptr. No additional data structures are used that grow with the input size.

    - ### Code
        - **Python Solution**
            ```python3 []
            class Solution:
                def minChanges(self, s: str) -> int:
                    # Initialize two pointers: left_Ptr and right_Ptr
                    # left_Ptr will track the most recent character that is part of the current "group"
                    # total_InterChanges will count the number of changes needed to make the string "valid"
                    left_Ptr, total_InterChanges = 0, 0
                    
                    # Iterate through the string with right_Ptr acting as the current position in the string
                    for right_Ptr in range(len(s)):
                        # If the characters at left_Ptr and right_Ptr are different, we need an interchange
                        if s[left_Ptr] != s[right_Ptr]: 
                            # Check if right_Ptr is an odd index (1-based) 
                            # We process only when right_Ptr is an odd index
                            # (right_Ptr & 1) checks if right_Ptr is odd
                            if right_Ptr & 1:
                                total_InterChanges += 1

                            # Move left_Ptr to the position of right_Ptr, essentially moving to the next "pair"
                            left_Ptr = right_Ptr
                    
                    # Return the total number of interchanges (or changes) needed to make the string "valid"
                    return total_InterChanges
            ```
        - **C++ Solution**
            ```C++ []
            class Solution {
                public:
                    int minChanges(string s) {
                        // Initialize two pointers: left_Ptr and right_Ptr
                        // left_Ptr will track the most recent character that is part of the current "group"
                        // total_InterChanges will count the number of changes needed to make the string "valid"
                        int left_Ptr = 0, total_InterChanges = 0;

                        // Iterate through the string with right_Ptr acting as the current position in the string
                        for(int right_Ptr = 0; right_Ptr < s.length(); ++right_Ptr) {
                            // If the characters at left_Ptr and right_Ptr are different
                            if(s[left_Ptr] != s[right_Ptr]) {
                                // Check if right_Ptr is odd (1-based index)
                                // If right_Ptr is odd, increment the number of interchanges (changes required)
                                if(right_Ptr & 1) {
                                    ++total_InterChanges;
                                }
                                // Move left_Ptr to the position of right_Ptr, essentially moving to the next "pair"
                                left_Ptr = right_Ptr;
                            }
                        }

                        // Return the total number of interchanges (or changes) needed to make the string "valid"
                        return total_InterChanges;
                    }
            };
            ```

- ## Approach 2:- Consecutive Characters Comparison (Greedy)

    - ### Intuition
        The goal of this problem is to count how many changes are needed to make the string conform to a specific pattern. The pattern requires characters at even indices to match the characters at the next odd indices (i.e., characters at positions `0, 2, 4, ...` should match those at positions `1, 3, 5, ...`). 

        To solve this, we traverse the string in steps of 2 and compare adjacent characters (pairs). Whenever we find a mismatch, we count it as a change needed to make the string valid according to the pattern.

    - ### Approach

        1. **Initialize a Counter:**
            - We initialize a variable `total_InterChanges` to 0, which will count how many changes are required.

        2. **Iterate Through the String in Steps of 2:**
            - We loop through the string with a step size of 2, comparing characters at positions `0` and `1`, `2` and `3`, `4` and `5`, and so on.
            - For each pair of characters at indices `(index, index + 1)`, if they are not equal, it means an interchange (change) is needed to make them match.

        3. **Count the Changes:**
            - Whenever a mismatch is found between the characters at `index` and `index + 1`, increment the `total_InterChanges` counter.

        4. **Return the Total Number of Changes:**
            - After the loop finishes, return the `total_InterChanges` which represents the total number of changes required to make the string valid.

    - ### Time Complexity

        - **Time Complexity: O(n)**  
            - We loop through the string once with a step size of 2. Each operation inside the loop (comparing two characters and potentially updating the counter) takes constant time. Since we process `n` characters and each comparison happens in constant time, the overall time complexity is **O(n)**, where `n` is the length of the string.

    - ### Space Complexity

        - **Space Complexity: O(1)**
            - The algorithm uses a constant amount of extra space. We only need a few integer variables (`total_InterChanges`, `index`) and don't use any additional data structures like arrays or hashmaps. Thus, the space complexity is __O(1)__.

    - ### Code
        - **Python Solution**
            ```python3 []
                class Solution:
                    def minChanges(self, s: str) -> int:
                        # Initialize a counter to keep track of the required number of changes
                        total_InterChanges = 0
                        
                        # Iterate over the string with a step of 2, starting from index 0
                        # This ensures that we compare pairs of characters at indices (0, 1), (2, 3), (4, 5), etc.
                        for index in range(0, len(s) - 1, 2):
                            # Compare the characters at positions index and index + 1
                            if s[index] != s[index + 1]:
                                # If the characters do not match, increment the change counter
                                total_InterChanges += 1

                        # Return the total number of interchanges (changes required)
                        return total_InterChanges
            ```
        - **C++ Solution**
            ```C++ []
            class Solution {
                public:
                    int minChanges(string s) {
                        // Initialize a counter to keep track of the required number of changes
                        int total_InterChanges = 0;
                        
                        // Iterate over the string, checking pairs of characters at indices (0, 1), (2, 3), (4, 5), etc.
                        // The loop runs with a step of 2, comparing characters at even and odd indices
                        for (int index = 0; index < s.length() - 1; index += 2) {
                            // Compare the characters at the current pair of indices
                            if (s[index] != s[index + 1]) {
                                // If the characters do not match, increment the change counter
                                ++total_InterChanges;
                            }
                        }
                        
                        // Return the total number of interchanges (changes required)
                        return total_InterChanges;
                    }
            };
            ```