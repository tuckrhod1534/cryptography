import shanks

class TestSolution():
    def test_get_order(self):
        assert shanks.get_order(5, 7) == 6
        assert shanks.get_order(2, 3) == 2
        assert shanks.get_order(3, 7) == 6
        assert shanks.get_order(2, 5) == 4
        assert shanks.get_order(4, 5) == 2
        assert shanks.get_order(3, 5) == 4

    def test_get_inverse(self):
        assert shanks.get_inverse(4, 5) == 4
        assert shanks.get_inverse(2, 2) == None
        assert shanks.get_inverse(5, 6) == 5
        assert shanks.get_inverse(1, 2) == 1
        assert shanks.get_inverse(36, 71) == 2

    def test_baby_step_giant_step(self):
        assert shanks.baby_step_giant_step(11, 71, 21) == 37
        assert shanks.baby_step_giant_step(3, 7, 5) == 5
        assert shanks.baby_step_giant_step(3, 7, 4) == 4
        assert shanks.baby_step_giant_step(5, 23, 8) == 6