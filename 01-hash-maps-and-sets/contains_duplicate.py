# contains_duplicate.py

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Pattern: Hash Set for "Have I seen this before?"
        Time: O(n), Space: O(n)
        """
        # Your LeetCode solution code goes here
        seen = set()
        for num in nums:  # Instead of for i in range(len(nums))
            if num in seen:
                return True
            seen.add(num)  # No else needed
        return False
        pass


# ========== LOCAL TESTING (Below this line) ==========

def test_contains_duplicate():
    """Test cases for local execution"""
    solution = Solution()
    
    # Test Case 1
    assert solution.containsDuplicate([1,2,3,1]) == True
    print("✓ Test 1 passed")
    
    # Test Case 2
    assert solution.containsDuplicate([1,2,3,4]) == False
    print("✓ Test 2 passed")
    
    # Test Case 3
    assert solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
    print("✓ Test 3 passed")
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_contains_duplicate()