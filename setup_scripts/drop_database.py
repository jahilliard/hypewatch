from src.controllers.DatabaseController import DatabaseController


def main():
    DatabaseController.drop_tables()

if __name__ == "__main__":
    main()
