import math
from typing_extensions import Self

class PrimeNumberField:
    def __new__(cls, modulus: int) -> Self:
        if not cls._is_prime_static(modulus):
            raise ValueError(f"Modulus is not prime - cannot build NumberField")
        return super().__new__(cls)

    def __init__(self, modulus: int) -> None:
        self.modulus = modulus
        self.roots = self.primitive_roots()
        self.elements = [x for x in range(self.modulus)]

    def __repr__(self) -> str:
        if len(self.elements) < 30: 
            return f"F_{self.modulus}\n----------\nElements: {self.elements}\nPrimitive Roots: {self.roots}"
        else:
            return f"F_{self.modulus}\n----------\nElements: {self.elements[:3]},...,{self.elements[-3:]}\nPrimitive Roots: {self.roots}"
    
    def get_inverse(self, num: int):
        num %= self.modulus
        if math.gcd(num, self.modulus) == 1:
            for i in range(1, self.modulus):
                if (num * i) % self.modulus == 1:
                    return i
        else:
            return None
        
    def get_order(self, root: int):
        for i in range(1, self.modulus):
            if root**i % self.modulus == 1:
                return i
        return None
        
    @staticmethod
    def _is_prime_static(n: int) -> bool:
        return all(n % i for i in range(2, int(n**0.5) + 1)) if n > 1 else False
    
    def _is_primitive_root(self, n: int) -> bool:
        powers = []
        for i in range(self.modulus - 1):
            powers.append((n**i) % self.modulus)
            if len(powers) != len(set(powers)):
                return False
        return True
        
    def primitive_roots(self) -> list:
        return [root for root in range(1, self.modulus) if self._is_primitive_root(root)]