"""
Practice Problem: Tuples

Task:
   -Write a function to:
   - Access the 2nd and 4th city.
   - Check if a given city exists in the tuple.
   - Convert the tuple into a list and add one more city.
"""


def access_second_fourth_city(tup):
    print(f"tuple is : {tup}")
    print(f"Second city is : {tup[1]}\n"
          f"Fourth city is : {tup[3]}")


#access_second_fourth_city(("blore", "hub", "delhi", "mysore", "mumbai", "chennai"))


def check_given_city(city_name: str, tup: tuple):

    return True if city_name in tup else False

city = "ooty"
tup = ("blore", "hub", "delhi", "mysore", "mumbai", "chennai")
#print(f"Whether the city-{city} exists in {tup} ? : {check_given_city(city,tup)}")

def convert_tuple_to_list(tup,another_city):
    list1=list(tup)
    list1.append(another_city)
    print(f"Tuple is : {tup}\n"
          f"Tuple after converting to list : {list1}\n"
          f"List after adding {another_city} : {list1}")

city = "ooty"
tup = ("blore", "hub", "delhi", "mysore", "mumbai", "chennai")
convert_tuple_to_list(tup,city)