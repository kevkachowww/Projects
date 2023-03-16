'''
Event Coordinator
You are starting up your own event coordination business and want to create a Python application using generators to help manage your events.

This project will help you practice and further master the use of generators by managing and coordinating customer events for your business.
'''
guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  plusOne = None
  while True:
    if plusOne is not None:
      line_data = plusOne.strip().split(",")
    else:
      line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age

    plusOne = yield name
    if plusOne is not None:
      line_data = plusOne.strip().split(",")
      name = line_data[0]
      age = int(line_data[1])
      guests[name] = age
      yield name

guest_gen = read_guestlist('guest_list.txt')
for _ in range(10):
  print(next(guest_gen))

guest_gen.send("Jane,35")

for guest in guest_gen:
  print(guest)

over21_gen = (name for name, age in guests.items() if age >= 21)
for guest in over21_gen:
  print(guest)

def table1():
  for i in range(1, 5+1):
    yield ('Chicken', 'Table 1', f'Seat {i}')
def table2():
  for i in range(1, 5+1):
    yield ('Beef', 'Table 1', f'Seat {i}')
def table3():
  for i in range(1, 5+1):
    yield ('Fish', 'Table 1', f'Seat {i}')

def connectedTable():
  yield from table1()
  yield from table2()
  yield from table3()

connect_iter = connectedTable().__iter__()

def assignTable():
  for name in guests:
    yield (name, next(connect_iter))

res = assignTable().__iter__()
for r in res:
  print(r)