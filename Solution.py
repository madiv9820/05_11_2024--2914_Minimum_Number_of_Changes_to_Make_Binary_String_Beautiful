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