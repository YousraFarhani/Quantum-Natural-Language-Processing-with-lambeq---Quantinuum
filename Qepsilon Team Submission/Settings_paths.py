import os

PROJECT_ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
SOURCE_PATH = os.path.join(PROJECT_ROOT_PATH, 'Tool', 'src', 'main')
TEST_PATH = os.path.join(PROJECT_ROOT_PATH, 'Tool', 'src', 'test')
DATA_PATH = os.path.join(PROJECT_ROOT_PATH, 'Datasets')


def print_paths():
    print(PROJECT_ROOT_PATH, SOURCE_PATH, TEST_PATH, DATA_PATH, GEN_PATH, sep='\n')
