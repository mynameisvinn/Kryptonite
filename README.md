# Kryptonite
Kryptonite is a partial re-implementation of [facebook's crypten](https://github.com/facebookresearch/CrypTen) library for  multi-party computing. It lets you add two numbers `A` and `B` without knowing either `A` or `B`.

## Example
```python
from Kryptonite import Kryptonite

A = Kryptonite(1)
B = Kryptonite(2)

C = A + B
C.get_plain_text()  # prints 3.0
```