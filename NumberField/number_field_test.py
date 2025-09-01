from number_field import PrimeNumberField

class TestSolution():

    def test_attr(self):
        field_7 = PrimeNumberField(7)
        field_5 = PrimeNumberField(5)
        field_3 = PrimeNumberField(3)

        assert field_7.modulus == 7
        assert field_7.roots == [3, 5]
        assert field_7.elements == [0,1,2,3,4,5,6]
        assert field_5.modulus == 5
        assert field_5.roots == [2, 3]
        assert field_5.elements == [0,1,2,3,4]
        assert field_3.modulus == 3
        assert field_3.roots == [2]
        assert field_3.elements == [0,1,2]

    def test_get_inverse(self):
        field_5 = PrimeNumberField(5)

        assert field_5.get_inverse(3) == 2
        assert field_5.get_inverse(2) == 3
        assert field_5.get_inverse(4) == 4

    def test_get_order(self):
        field_7 = PrimeNumberField(7)

        assert field_7.get_order(3) == 6
        assert field_7.get_order(5) == 6
        assert field_7.get_order(6) == 2

    def test_is_primitive_root(self):
        field_5 = PrimeNumberField(5)

        assert field_5._is_primitive_root(1) == False
        assert field_5._is_primitive_root(2) == True
        assert field_5._is_primitive_root(3) == True
        assert field_5._is_primitive_root(4) == False

    def test_is_prime_static(self):
        
        assert PrimeNumberField._is_prime_static(3) == True
        assert PrimeNumberField._is_prime_static(4) == False