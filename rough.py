# lst = [1,2,3]
# my_str = "MLOps concepts"
# my_int = 155

# print(type(lst))
# print(type(my_str))
# print(type(my_int))


# my_str = my_str.capitalize()
# print(my_str)

from oops_proj import chatbook

user1 = chatbook()
print(user1.id)

chatbook.set_id(10)

user2 = chatbook()
print(user2.id)


# Getter & Setter
# print(user1.get_name())

# user1.set_name("Agent X")

# print(user1.get_name())


