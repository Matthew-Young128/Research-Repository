#for this exercise i was practicing creating and indexing disctionaries
#the exercises and code were provided by: https://python-course.eu/python-tutorial/dictionaries.php


city_population = {"New York City": 8_550_405, 
                   "Los Angeles": 3_971_883, 
                   "Toronto": 2_731_571, 
                   "Chicago": 2_720_546, 
                   "Houston": 2_296_224, 
                   "Montreal": 1_704_694, 
                   "Calgary": 1_239_220, 
                   "Vancouver": 631_486, 
                   "Boston": 667_137}

#We can access the value for a specific key by putting this key in brackets following the name of the dictionary:

city_population["New York City"]
#OUTPUT: 8550405

city_population["Toronto"]
#OUTPUT: 2731571

city_population["Detroit"]

#Output
#KeyError                                  Traceback (most recent call last)
#<ipython-input-5-80e422418d76> in <module>
#----> 1 city_population["Detroit"]
#KeyError: 'Detroit'

#pop() and popitem()
en_de = {"Austria":"Vienna", "Switzerland":"Bern", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capitals = {"Austria":"Vienna", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capital = capitals.pop("Austria")
print(capital)

capital = capitals.pop("Switzerland", "Bern")
print(capital)


capitals = {"Springfield": "Illinois", 
            "Augusta": "Maine", 
            "Boston": "Massachusetts", 
            "Lansing": "Michigan", 
            "Albany": "New York", 
            "Olympia": "Washington", 
            "Toronto": "Ontario"}
(city, state) = capitals.popitem()
(city, state)
print(capitals.popitem())

#accessing non-existing keys
locations = {"Toronto": "Ontario", "Vancouver": "British Columbia"}
locations["Ottawa"]
province = "Ottawa"

if province in locations: 
    print(locations[province])
else:
    print(province + " is not in locations")
    
#copy()
words = {'house': 'Haus', 'cat': 'Katze'}
w = words.copy()
words["cat"]="chat"
print(w)
print(words)

#Exercise 1: Write a function dict_merge_sum that takes two dictionaries d1 and d2 as parameters. The values of both dictionaries are numerical. The function should return the merged sum dictionary m of those dictionaries. If a key k is both in d1 and d2, the corresponding values will be added and included in the dictionary m If k is only contained in one of the dictionaries, the k and the corresponding value will be included in m
def dict_merge_sum(d1, d2):
    # Create an empty dictionary to store the merged sums
    m = {}

    # Iterate through keys in d1
    for key in d1:
        # Check if the key is also in d2
        if key in d2:
            # If present in both dictionaries, add the values
            m[key] = d1[key] + d2[key]
        else:
            # If only in d1, include the key and value in m
            m[key] = d1[key]

    # Iterate through keys in d2 that are not already processed
    for key in set(d2) - set(d1):
        # Include the key and value in m
        m[key] = d2[key]

    return m

# Example usage:
dictionary1 = {'a': 10, 'b': 20, 'c': 30}
dictionary2 = {'b': 5, 'c': 15, 'd': 25}

merged_sum = dict_merge_sum(dictionary1, dictionary2)
print("Merged Sum Dictionary:", merged_sum)

#Exercise 2: Given is the following simplified data of a supermarket:
supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}
#To be ready for an imminent crisis you decide to buy everything. This isn't particularly social behavior, but for the sake of the task, let's imagine it. The question is how much will you have to pay?
def calculate_total_cost(supermarket_data):
    total_cost = 0
    for item, details in supermarket_data.items():
        total_cost += details["quantity"] * details["price"]
    return total_cost

total_cost = calculate_total_cost(supermarket)
print(f"The total cost for buying everything in the supermarket is: ${total_cost:.2f}")

#Exercise 3: Create a virtual supermarket. For every article there is a price per article and a quantity, i.e. the stock. (Hint: you can use the one from the previous exercise!)Create shopping lists for customers. The shopping lists contain articles plus the quantity.The customers fill their carts, one after the other. Check if enough goods are available! Create a receipt for each customer.

class VirtualSupermarket:
    def __init__(self, supermarket_data):
        self.supermarket_data = supermarket_data

    def create_shopping_list(self, customer_name, items):
        shopping_list = {}
        for item, quantity in items.items():
            if item in self.supermarket_data and self.supermarket_data[item]["quantity"] >= quantity:
                shopping_list[item] = {"quantity": quantity, "price": self.supermarket_data[item]["price"]}
                self.supermarket_data[item]["quantity"] -= quantity
            else:
                print(f"Insufficient stock for {item} in the supermarket. Skipping.")

        receipt = self.generate_receipt(customer_name, shopping_list)
        return receipt

    def generate_receipt(self, customer_name, shopping_list):
        total_cost = sum(item["quantity"] * item["price"] for item in shopping_list.values())
        receipt = {
            "customer_name": customer_name,
            "shopping_list": shopping_list,
            "total_cost": total_cost
        }
        return receipt

# Create a virtual supermarket instance
virtual_supermarket = VirtualSupermarket(supermarket)

# Customer 1 shopping list
customer1_shopping_list = {"milk": 2, "biscuits": 3, "bread": 1, "cookies": 2}
customer1_receipt = virtual_supermarket.create_shopping_list("Customer 1", customer1_shopping_list)
print("Customer 1 Receipt:", customer1_receipt)

# Customer 2 shopping list
customer2_shopping_list = {"oranges": 5, "bananas": 2, "yogurt": 4}
customer2_receipt = virtual_supermarket.create_shopping_list("Customer 2", customer2_shopping_list)
print("Customer 2 Receipt:", customer2_receipt)
