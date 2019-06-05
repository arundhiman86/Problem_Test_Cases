# Geeks and Strings
Geek recently read about strings, and he got interested in them.Geek has a list containing N words (not necessarily distinct)-denoted by Li.Now, he will ask Q queries.Each query will consist of a string x. You need to tell How many strings in the List has the string x as its prefix.

##### *Note:-*
1. You need to create a file by the name of "**geeksandstrings.py**"
2. Create a function by the name of "**substring()**" which should take two parameters:-
    - First parameter would be the list of strings in which you need to check the substring.
    - Second parameter would be the list of sub-string which you will using to check if that sub-string starts with list of strings given as first parameter.

**e.g.:-** 
```python
lines = ['abracadabra', 'geeksforgeeks', 'abracadabra', 'geeks', 'geeksthrill']
queries = ['abr', 'geeks', 'geeksforgeeks', 'ge', 'gar']
substring(lines, queries) should return ['2', '3', '1', '3', '0']
```

#### Explanation:
There are 2 strings that have prefix "abr" - "abracadabra" and "abracadabra"
There are 3 strings that have prefix "geeks" - "geeksforgeeks" and "geeks" and "geeksthrill"
There is 1 string thathave prefix "geeksforgeeks" - "geeksforgeeks".
There are 3 strings that have prefix "ge" - "geeksforgeeks" and "geeks" and "geeksthrill"
There is No string thathave prefix as "gar".
