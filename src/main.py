class Main:
    def __init__(self):
        self.name = "Main"
        self.version = "1.0.0"

    def run(self):
        print(f"Running {self.name} version {self.version}")

    def add_numbers(self, a, b):
        """Ajoute deux nombres et retourne le résultat."""
        return a + b


if __name__ == "__main__":
    main = Main()
    main.run()
