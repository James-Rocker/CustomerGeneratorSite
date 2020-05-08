import random


class GCN:
    def __init__(self):
        # Get Customer Name
        name = open('Generator/docs/Name.txt', 'r').read().split(',')
        print("Customer name: " + random.choice(name))
        super().__init__()


class GCD:
    def __init__(self):
        # Get Customer Demand
        customer_demand = open('Generator/docs/Customer_Demand.txt', 'r').read().replace('\n', ' ').replace('\r',
                                                                                                            '').split(
            ',')
        print("Customer item enquiry: " + random.choice(customer_demand))
        super().__init__()


class GP:
    def __init__(self):
        # Get Profession
        profession = open('Generator/docs/Profession.txt', 'r').read().split(',')
        print("Profession: " + random.choice(profession))
        super().__init__()


class GR:
    def __init__(self):
        # Get Race
        race = open('Generator/docs/Race.txt', 'r').read().split(',')
        print("Customer race: " + random.choice(race))
        super().__init__()


class WTH:
    def __init__(self):
        # Will They Haggle
        haggle = open('Generator/docs/WTH.txt', 'r').read().split(',')
        print("Will they haggle? " + random.choice(haggle))
        super().__init__()


class Customer(GCN, GCD, GP, GR, WTH):
    def __init__(self):
        super().__init__()
