from random import randint

class Generator:
    post_code_length = 10
    name_length = 10
    char_offset = 97
    alphaber_size = 26


    @staticmethod
    def generate_code() -> str:
        post_code = ''
        for _ in range(Generator.post_code_length):
            post_code += str(randint(0, 9))
        return post_code
    
    @staticmethod
    def generate_name(code: str) -> str:
        name = ''
        for i in range(0, Generator.name_length, 2):
            name += chr(Generator.char_offset + int(code[i:i+2]) % Generator.alphaber_size)
        return name