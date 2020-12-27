import random


def build_customer():
    customer_name = random.choice(
        open("Generator/docs/Name.txt", "r")
        .read()
        .replace("\n", " ")
        .replace("\r", "")
        .split(",")
    ).strip()

    customer_demand = random.choice(
        (
            open("Generator/docs/Customer_Demand.txt", "r")
            .read()
            .replace("\n", " ")
            .replace("\r", "")
            .split(",")
        )
    ).strip()

    customer_race = random.choice(
        open("Generator/docs/Race.txt", "r").read().split(",")
    )
    customer_profession = random.choice(
        open("Generator/docs/Profession.txt", "r").read().split(",")
    )
    will_they_haggle = random.choice(
        open("Generator/docs/WTH.txt", "r").read().split(",")
    )

    return {
        "Customer Demand": customer_demand,
        "Customer Name": customer_name,
        "Customer Profession": customer_profession,
        "Customer Race": customer_race,
        "Will They Haggle?": will_they_haggle,
    }
