from typing import List


class CustomersHandler:
    @staticmethod
    def __get_avg_len(names: List[str]) -> float:
        name_lengths = [len(name) for name in names]
        avg = sum(name_lengths) / len(name_lengths)
        return avg

    @staticmethod
    def __get_closest_avg(names: List[str], avg: float) -> str:
        closest_avg = min(names, key=lambda name: abs(len(name) - avg))
        return closest_avg

    def get_fitting_name(self, names):
        avg = self.__get_avg_len(names)
        name = self.__get_closest_avg(names, avg)
        return name