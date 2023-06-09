# Matrix Operations

## Instructions

You have to implement some operations over **Matrices**

### Matrix multiplication 

Given 2 Matrices represented as `List[List[float]]` You have to multiply them and return the result.

If **A** has dimensions **m × n** and **B** has dimensions **n x p**.

Then the product **C = A x B** has dimensions **m x p**.

Where C<sub>i,j</sub> = Sum of each element of the row A<sub>i</sub> by each element of the column B<sub>j</sub>.

![See](matrixmultiplication.jpeg)

For example:

```python

multiply([[1, 2, 3],
          [4, 5, 6]],
         [[1, 2],
          [3, 4],
          [5, 6]]
)
```
Should return:
```python
[[22 , 28],
 [49, 64]]
```
          
          
