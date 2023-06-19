import sys

DATABASE_PATH = "personas.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/personas_test.csv"
