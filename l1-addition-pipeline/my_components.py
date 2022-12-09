from kfp.v2.dsl import (
    component,
)

# Addition function based component
@component
def add(a: float, b: float) -> float:
  '''Calculates sum of two arguments'''
  return a + b