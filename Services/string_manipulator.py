class StringManipulator:
    def extract_name_from_code(self, code: str) -> str:
        return self.__internal_extractor(code[:10])

    def extract_surname_from_code(self, code: str) -> str:
        return self.__internal_extractor(code[10:])

    @staticmethod
    def check_for_length(num: int, limit: int) -> int:
        return num % limit if num > limit else num

    def __internal_extractor(self, code: str, step: int = 2) -> str:
        extracted_line = ""
        for i in range(0, len(code), step):
            char_code = self.check_for_length(int(code[i:i + 2]), 25)
            extracted_line += chr(char_code + 97)
        return extracted_line