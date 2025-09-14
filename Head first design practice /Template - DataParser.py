from abc import ABC, abstractmethod


# --- Abstract Base Class ---
class DataParser(ABC):
    """Template method defines the skeleton of the algorithm."""

    def process_file(self, filename: str) -> None:
        self.load_file(filename)
        data = self.parse_data(filename)
        if self.should_validate():  # hook
            if not self.validate_data(data):
                print("❌ Validation failed. Aborting.")
                return
        self.save_to_db(data)

    def load_file(self, filename: str) -> None:
        print(f"Loading file: {filename}")

    @abstractmethod
    def parse_data(self, filename: str):
        pass

    def validate_data(self, data) -> bool:
        print("Validating data...")
        return bool(data)  # default: just check non-empty

    def save_to_db(self, data) -> None:
        print(f"✅ Saving {len(data)} records to database...")

    # --- Hook (optional step) ---
    def should_validate(self) -> bool:
        return True


# --- Concrete Parsers ---
class CSVParser(DataParser):
    def parse_data(self, filename: str):
        print("Parsing CSV data...")
        # Simulated parse: split on commas
        return ["row1,col1,col2", "row2,col1,col2"]


class JSONParser(DataParser):
    def parse_data(self, filename: str):
        print("Parsing JSON data...")
        # Simulated parse: pretend to read JSON
        return [{"id": 1, "value": "A"}, {"id": 2, "value": "B"}]


class XMLParser(DataParser):
    def parse_data(self, filename: str):
        print("Parsing XML data...")
        # Simulated parse: pretend to read XML
        return ["<record>1</record>", "<record>2</record>"]

    # override hook: skip validation for XML
    def should_validate(self) -> bool:
        print("Skipping validation for XML files.")
        return False


# --- Demo ---
if __name__ == "__main__":
    print("\n--- CSV ---")
    parser = CSVParser()
    parser.process_file("data.csv")

    print("\n--- JSON ---")
    parser = JSONParser()
    parser.process_file("data.json")

    print("\n--- XML ---")
    parser = XMLParser()
    parser.process_file("data.xml")
