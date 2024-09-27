class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # If the input string is empty, return 0
        if not s:
            return 0
        
        # Dictionary mapping Roman numerals to integer values
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Initialize the integer result
        result = 0
        
        # Loop over each character in the string, except the last one
        for i in range(len(s) - 1):
            # If the current value is less than the next value, subtract it
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                # Otherwise, add it
                result += roman_map[s[i]]
        
        # Add the last Roman numeral value to the result
        result += roman_map[s[-1]]
        
        return result
