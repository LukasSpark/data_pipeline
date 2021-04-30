from pathlib import Path
from typing import Generator

# print("Path: ", Path(__file__).resolve().parent.parent)   # wenn die parents wegg genommen werden sieht
# man wie man höher steigt im Pfad mal ausprobieren

DATA_DIR = Path(__file__).resolve().parent.parent / "data"    # / ist hier ein überladener Operator vom pathlib Modul


# ETL: Extract, Transform, Load
def read_data(file_name: str) -> Generator:
    """große Datei einlesen"""
    with open(DATA_DIR / file_name) as f:
        for line in f:
            yield line


"""
# So eher nicht bei zu großen datein würde das den speicher sprengen
def split_line(g: Generator):
    result = []
    for el in g:
        result.append(el.split())
    return result
"""


def split_line(g: Generator):
    result = (line.strip().split(",") for line in g) # Würde alles ausgeben
    # result = (line.strip().split(",") for line in g if "Life" in line)  # gibt nur die lit Life in der Zeile
    """
    # Ist der Code von oben und dann bräuchte man kein return aber yield
    for line in g:
        yield line.strip().split(",")
    """
    return result


def dictify(g: Generator):
    header = next(g)
    return (dict(zip(header, line)) for line in g)


def load_data(file_name: str) -> Generator:
    file_generator = read_data(file_name)
    split_lines = split_line(file_generator)
    return dictify(split_lines)


if __name__ == "__main__":
    load_data('techcrunch.csv')
