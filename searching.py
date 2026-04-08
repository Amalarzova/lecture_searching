from pathlib import Path
import json



def read_data(file_name, field):
    path = Path(__file__).parent / file_name
    with open(file_name, "r") as f:
        data = json.load(f)

        if field not in data:
            return None

    return data[field]

def main():
    sequential_data = read_data("sequential.json","unordered_numbers" )
    print(sequential_data)




if __name__ == "__main__":
    main()
