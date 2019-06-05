# Leap year

Given a year, report if it is a leap year.
The tricky thing here is that a leap year in the Gregorian calendar occurs:
```
1. on every year that is evenly divisible by 4
2. except every year that is evenly divisible by 100
3. unless the year is also evenly divisible by 400
```
For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is. 

If your language provides a method in the standard library that does this look-up, pretend it doesn't exist and implement it yourself.

##### *Note:-*
1. You need to create a file by the name of "**leap_year.py**"
2. Create a function by the name of "**leap()**" which takes year as an input and retruns 'Leap Year' if leap year else return 'Not a leap year'.

**e.g.:-** 
```python
leap_check(2000) should return "Leap Year"
```