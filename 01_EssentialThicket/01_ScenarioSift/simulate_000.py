class HighPrecisionArithmetic:
    def __init__(self, base_size: int = 9):
        self.base_size = base_size
        self.base = 10 ** base_size

    def _split_number(self, number: str) -> List[int]:
        return [int(number[max(i - self.base_size, 0):i]) for i in range(len(number), 0, -self.base_size)]

    def add(self, number1: str, number2: str) -> str:
        num1 = self._split_number(number1)
        num2 = self._split_number(number2)
        carry = 0
        result = []
        max_len = max(len(num1), len(num2))
        for i in range(max_len):
            val1 = num1[i] if i < len(num1) else 0
            val2 = num2[i] if i < len(num2) else 0
            sum_val = val1 + val2 + carry
            result.append(sum_val % self.base)
            carry = sum_val // self.base
        if carry:
            result.append(carry)
        result_str = ""
        for i in reversed(range(len(result))):
            result_str += str(result[i]) if i == len(result) - 1 else f"{result[i]:09d}"
        return result_str

    def subtract(self, number1: str, number2: str) -> str:
        num1_bigger = (len(number1) > len(number2)) or (len(number1) == len(number2) and number1 > number2)
        if not num1_bigger:
            number1, number2 = number2, number1
        num1 = self._split_number(number1)
        num2 = self._split_number(number2)
        result = []
        borrow = 0
        for i in range(max(len(num1), len(num2))):
            val1 = num1[i] if i < len(num1) else 0
            val2 = num2[i] if i < len(num2) else 0
            diff = val1 - val2 - borrow
            if diff < 0:
                diff += self.base
                borrow = 1
            else:
                borrow = 0
            result.append(diff)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        if result == [0]:
            return '0'
        result_str = ''.join(map(lambda x: f"{x:09d}", reversed(result))).lstrip('0')
        return result_str if num1_bigger else "-" + result_str

    def multiply(self, number1: str, number2: str) -> str:
        if number2 == '0' or number1 == '0':
            return '0'
        num1_list = self._split_number(number1)
        num2_list = self._split_number(number2)
        result = [0] * (len(num1_list) + len(num2_list))
        for i in range(len(num1_list)):
            for j in range(len(num2_list)):
                result[i + j] += num1_list[i] * num2_list[j]
                result[i + j + 1] += result[i + j] // self.base
                result[i + j] %= self.base
        for i in range(len(result) - 1):
            result[i + 1] += result[i] // self.base
            result[i] %= self.base
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return ''.join(str(x).zfill(9) for x in reversed(result)).lstrip('0')

    def divide(self, dividend: str, divisor: str) -> Tuple[str, int]:
        dividend_parts = self._split_number(dividend)[::-1]
        divisor_int = int(divisor)
        remainder = 0
        result = []
        for part in dividend_parts:
            current = remainder * self.base + part
            result.append(current // divisor_int)
            remainder = current % divisor_int
        if result:
            final_result = [str(result[0])]
            final_result.extend(f"{num:09d}" for num in result[1:])
            quotient = ''.join(final_result).lstrip('0') or '0'
        else:
            quotient = '0'
        return quotient, remainder
