import csv
import json
import pickle
import os
import sys


# ===================== BASE CLASS =====================
class FileHandler:
    def __init__(self, path):
        self.path = path
        self.data = []

    def load(self):
        raise NotImplementedError

    def save(self, path):
        raise NotImplementedError

    def show(self):
        print("\n--- FILE CONTENT ---")
        for i, row in enumerate(self.data):
            print(i, row)

    def apply_changes(self, changes):
        for change in changes:
            try:
                col, row, value = change.split(",", 2)
                col = int(col)
                row = int(row)

                # check bounds
                if row < 0 or row >= len(self.data):
                    print(f"Invalid row: {row}")
                    continue

                if col < 0 or col >= len(self.data[row]):
                    print(f"Invalid column: {col}")
                    continue

                self.data[row][col] = value

            except Exception as e:
                print(f"Error in change '{change}': {e}")


# ===================== CSV =====================
class CSVHandler(FileHandler):
    def load(self):
        with open(self.path, "r", newline="") as file:
            reader = csv.reader(file)
            self.data = list(reader)

    def save(self, path):
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.data)


# ===================== JSON =====================
class JSONHandler(FileHandler):
    def load(self):
        with open(self.path, "r") as file:
            self.data = json.load(file)

    def save(self, path):
        with open(path, "w") as file:
            json.dump(self.data, file, indent=2)


# ===================== PICKLE =====================
class PickleHandler(FileHandler):
    def load(self):
        with open(self.path, "rb") as file:
            self.data = pickle.load(file)

    def save(self, path):
        with open(path, "wb") as file:
            pickle.dump(self.data, file)


# ===================== FACTORY =====================
def get_handler(path):
    if path.endswith(".csv"):
        return CSVHandler(path)
    elif path.endswith(".json"):
        return JSONHandler(path)
    elif path.endswith(".pickle"):
        return PickleHandler(path)
    else:
        raise ValueError("Unsupported file type")


# ===================== MAIN =====================
def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py source destination [changes...]")
        return

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    # check file exists
    if not os.path.isfile(src):
        print(f"File not found: {src}")
        print("\nAvailable files:")
        for f in os.listdir("."):
            print("-", f)
        return

    # load source
    handler = get_handler(src)
    handler.load()

    # apply changes
    handler.apply_changes(changes)

    # show result
    handler.show()

    # save to destination
    out_handler = get_handler(dst)
    out_handler.data = handler.data
    out_handler.save(dst)

    print(f"\nSaved to: {dst}")


# ===================== RUN =====================
if __name__ == "__main__":
    main()