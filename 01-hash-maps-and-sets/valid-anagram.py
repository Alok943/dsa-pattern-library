# valid_anagram.py

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Pattern: Hash Map for frequency counting
        Time: O(n), Space: O(n)
        """
        if len(s) != len(t):
            return False
            
        count_s = {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        return count_s == count_t


# ========== LOCAL TESTING ==========

def test_valid_anagram():
    """Test cases for local execution"""
    solution = Solution()
    
    # Test Case 1
    assert solution.isAnagram("anagram", "nagaram") == True
    print("✓ Test 1 passed")
    
    # Test Case 2
    assert solution.isAnagram("rat", "car") == False
    print("✓ Test 2 passed")
    
    # Test Case 3
    assert solution.isAnagram("a", "ab") == False
    print("✓ Test 3 passed")
    
    # Test Case 4
    assert solution.isAnagram("", "") == True
    print("✓ Test 4 passed")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_valid_anagram()