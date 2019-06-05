# String Conversion

Given two strings X and Y (call letters in uppercase). Check if it is possible to convert X to Y by performing following operations.

- Make some lowercase letters uppercase.
- Delete all the lowercase letters.

Print "Yes" if it's  possible to convert X to Y by performing following operations else "No".

##### *Note:-*
1. You need to create a file by the name of "**string_conversion.py**"
2. Create a function by the name of "**conversion()**" which takes two arguments as strings and returns "Yes" or "No" based upon the avobe operations.

**Example:**
```python
conversion('daBcd', 'ABC') should return as 'Yes'

conversion('ABcd', 'BCD') should return as 'No'
```

## Explanation :
Test Case 1:  daBcd -> dABCd -> ABC Covert a and b at index 1 and 3 to upper case, delete the rest those are lowercase. We get the string Y so the output is: Yes.
