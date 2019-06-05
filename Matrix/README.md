# Matrix
Given a string representing a matrix of numbers, return the rows and columns of that matrix.

So given a string with embedded newlines like:

```
9 8 7
5 3 2
6 6 7
```
representing this matrix:
```
    0  1  2
  |---------
0 | 9  8  7
1 | 5  3  2
2 | 6  6  7
```
your code should be able to spit out:

- A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
- A list of the columns, reading each column top-to-bottom while moving from left-to-right.

The rows for our example matrix:
```
9, 8, 7
5, 3, 2
6, 6, 7
```
And its columns:
```
9, 5, 6
8, 3, 6
7, 2, 7
```

##### *Note:-*
1. You need to create a file by the name of "**matrix.py**"
2. Create a Class by the name of "**Matrix()**" which should have two methods "**row and column**", which in turn gives the list of the elements from the matrix, as mentioned below:-

**e.g.:-** matrix = Matrix("1 2\n3 4"), matrix.row(1) should return [3, 4] as a result and matrix.column(1) should return [1, 3] as a result.
