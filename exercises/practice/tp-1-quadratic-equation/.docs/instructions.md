# Types

## Instructions

You have to solve a Second grade equation of the form **ax<sup>2</sup> + bx + c**.

For this create a class named Quadratic that creates from 3 Float numbers, each representing the coefficients a, b and c 

This class have all this behaviour:
* `roots`: returns a `Tuple[float, float]` that represents the (x<sub>1</sub> and x<sub>2</sub>).
  * If the equation has only one real solution then both roots will have the same value.
  * If the equation has no real solutions then return an empty Tuple
* `evaluate`: Given a `float` that represent a x<sub>1</sub> *valueY* returns a `float` that is the y<sub>1</sub>
* `__str__()`: should return a String representing the Quadratic as a String in the form `Y = A * X2 + B * X + C`
* `derivative`: should return a String representing the derived equation in the form of `Y = A * X + B`


## Examples

`Quadratic(2, 0, 0).roots()` should return `(0, 0)`

`Quadratic(1, 2, 1).roots()` should return `(-1, -1)`

`Quadratic(1, 1, 1).roots()` should return `()`

`Quadratic(1, 1, 1).evaluate(1)` should return `3`

`str(Quadratic(1, 2, 3))` should return `1 * X2 + 2 * X + 3`

`Quadratic(1, 2, 3).derivative()` should return `2 * X + 2`
