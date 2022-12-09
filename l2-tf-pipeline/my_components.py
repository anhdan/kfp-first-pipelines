from kfp.v2.dsl import (
    component,
    Input,
    Output,
    Dataset,
    Metrics
)
from typing import NamedTuple

# Addition function based component
@component
def add(a: float, b: float) -> float:
  '''Calculates sum of two arguments'''
  return a + b

# Divmod function based component
@component(base_image='tensorflow/tensorflow')
# @component
def my_divmod(
  dividend: float,
  divisor: float,
  metrics: Output[Metrics]) -> NamedTuple(
    'MyDivmodOutput',
    [
      ('quotient', float),
      ('remainder', float),
    ]):
    '''Divides two numbers and calculate  the quotient and remainder'''

    # Import the numpy package inside the component function
    import numpy as np

    # Define a helper function
    def divmod_helper(dividend, divisor):
        return np.divmod(dividend, divisor)

    (quotient, remainder) = divmod_helper(dividend, divisor)

    # Export two metrics
    metrics.log_metric('quotient', float(quotient))
    metrics.log_metric('remainder', float(remainder))

    from collections import namedtuple
    divmod_output = namedtuple('MyDivmodOutput',
        ['quotient', 'remainder'])
    return divmod_output(quotient, remainder)