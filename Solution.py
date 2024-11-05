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