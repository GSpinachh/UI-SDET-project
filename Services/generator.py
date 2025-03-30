from random import randint

class Generator:
    @staticmethod
    def generate_code(bottom_threshold=0, top_threshold=100, 
                      code_size=10, digit_size=2) -> str:
        return ''.join(str(randint(bottom_threshold, top_threshold)).zfill(digit_size)
                       for _ in range(code_size))