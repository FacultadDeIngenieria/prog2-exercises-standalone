# Trapezoid Rule

In calculus, the trapezoidal rule (also known as the trapezoid rule or trapezium rule)
is a technique for approximating the definite integral.

The function is divided into many sub-intervals
and each interval is approximated by a Trapezium.
Then the area of trapeziums is calculated and summed to find the integral.
The more is the number of trapeziums used, the better is the approximation.

![image](https://www.bragitoff.com/wp-content/uploads/2015/08/TrapezoidRule1.png)

## Instructions

You need to create a function that aproximate the integral using the trapezoid rule.

The function should receive as parameters:
- The function to be integrated
- The limits of the integral (`a` and `b`).
- The number of intervals (`n`)

For example:

```python
> integrate(lambda x: 1, 0, 10, 100)
10.0
> integrate(math.cos, 0, math.pi/2, 1000)
0.999...
> integrate(lambda x: math.e**(-x**2), -10, 10, 100)
1.77..
```