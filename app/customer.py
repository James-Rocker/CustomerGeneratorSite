import random
import os


def build_new():
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    customer_name = random.choice(
        open(f"{absolute_path}\\static\\Name.txt", "r")
        .read()
        .replace("\n", " ")
        .replace("\r", "")
        .split(",")
    ).strip()

    customer_demand = random.choice(
        (
            open(f"{absolute_path}\\static\\Customer_Demand.txt", "r")
            .read()
            .replace("\n", " ")
            .replace("\r", "")
            .split(",")
        )
    ).strip()

    customer_race = random.choice(
        open(f"{absolute_path}\\static\\Race.txt", "r").read().split(",")
    )
    customer_profession = random.choice(
        open(f"{absolute_path}\\static\\Profession.txt", "r").read().split(",")
    )
    will_they_haggle = random.choice(
        open(f"{absolute_path}\\static\\WTH.txt", "r").read().split(",")
    )

    return {
        "Customer Demand": customer_demand,
        "Customer Name": customer_name,
        "Customer Profession": customer_profession,
        "Customer Race": customer_race,
        "Will They Haggle?": will_they_haggle,
    }
