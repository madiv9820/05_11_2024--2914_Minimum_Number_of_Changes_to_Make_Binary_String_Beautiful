#include <iostream>
#include <string>
using namespace std;

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

int main() {
    string s; Solution sol;
    cin >> s;

    cout << sol.minChanges(s = s) << endl;
}