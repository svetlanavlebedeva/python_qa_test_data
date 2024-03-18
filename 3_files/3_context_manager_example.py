import os


class TempFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        # Create empty file
        open(self.filename, 'w').close()
        print(f"File {self.filename} created.")
        return self.filename

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Delete file
        os.remove(self.filename)
        print(f"File {self.filename} deleted.")


# usage
if __name__ == "__main__":
    with TempFile('temp_test_file.txt') as tempfile:
        print(f"Using {tempfile}...")
        # other code
    print("Testing is over.")
