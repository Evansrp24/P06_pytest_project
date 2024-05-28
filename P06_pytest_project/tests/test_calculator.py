from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add_normal_1(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_add_normal_2(self):
        # arrange
        a = 20
        b = 30
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 50
        assert result == expected

    def test_add_negative(self):
        # arrange
        a = -10
        b = -2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = -12
        assert result == expected

    #Subtract
    def test_subtract_normal_1(self):
        # arrange
        a = 10
        b = 2
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 8
        assert result == expected

    def test_subtract_normal_2(self):
        # arrange
        a = 20
        b = 15
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 5
        assert result == expected

    def test_subtract_negative(self):
        # arrange
        a = 3
        b = -4
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 7
        assert result == expected

    #Multiply
    def test_multiply_normal_1(self):
        # arrange
        a = 10
        b = 2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 20
        assert result == expected

    def test_multiply_normal_2(self):
        # arrange
        a = 2
        b = 15
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 30
        assert result == expected

    def test_multiply_negative(self):
        # arrange
        a = -4
        b = -2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 8
        assert result == expected

    #Divide
    def test_divide_normal_1(self):
        # arrange
        a = 14
        b = 7
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 2
        assert result == expected

    def test_divide_normal_2(self):
        # arrange
        a = 16
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 8
        assert result == expected

    def test_divide_zero(self):
        # arrange
        a = 4
        b =  0
        cal = Calculator()

        # act and assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)

   

