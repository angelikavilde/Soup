"""File to load initial dataset for searches"""

from json import load
from csv import reader


def load_json(filename: str) -> 'list[dict]':
    """"""
    with open(filename, "r") as f:
        return load(f)


def process_takeout_data() -> set:
    """"""
    takeout_food_data_filename = "food_raw_data/foods.json"
    takeout_food_data = load_json(takeout_food_data_filename)

    takeout_data_cleaned = set()
    for restaurant in takeout_food_data:
        for item in restaurant["foodItems"]:
            takeout_data_cleaned.add(item["foodName"])

    return takeout_data_cleaned


def process_fruit_data() -> set:
    """"""
    fruit_data_filename = "food_raw_data/fruits.json"
    fruit_data = load_json(fruit_data_filename)
    return set(fruit_data["fruits"])


def process_groceries_dataset():
    """"""
    with open("food_raw_data/Groceries_dataset.csv", newline="") as f:
        groceries_data = [obj[2] for obj in reader(f)]
    return set(groceries_data)


def get_combined_data_file(data_set: set) -> None:
    """"""
    food_data = "\n".join(data_set)
    with open("seach_data.txt", "w") as f:
        f.write(food_data)


if __name__ == "__main__":
    takeout_data = process_takeout_data()
    fruit_data = process_fruit_data()
    groceries_data = process_groceries_dataset()
    get_combined_data_file((takeout_data.union(fruit_data)).union(groceries_data))
    