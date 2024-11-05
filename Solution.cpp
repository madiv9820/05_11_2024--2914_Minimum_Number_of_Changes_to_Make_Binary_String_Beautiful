#include <iostream>
#include <string>
using namespace std;

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

int main() {
    string s; Solution sol;
    cin >> s;

    cout << sol.minChanges(s = s) << endl;
}