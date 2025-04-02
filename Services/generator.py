from random import randint


class Generator:
    @staticmethod
    def generate_code() -> str:
        post_code = ''
        for _ in range(0, 10):
            post_code += str(randint(0, 9))

        return post_code
    
    @staticmethod
    def generate_name(code: int):
        name = ''
        for i in range(0, 10, 2):
            name += chr(97 + int(code[i:i+2]) % 26)
        return name