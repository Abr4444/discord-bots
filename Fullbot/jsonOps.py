import json

def check_existence(id):
  with open("./cogs/data.json", "r") as f:
    data = json.load(f)
    f.close()

  if data.get(str(id)) is None:
    data[str(id)] = 0

    jsonString = json.dumps(data)
    with open("./cogs/data.json", "w+") as f:
      f.write(jsonString)
      f.close()

    return data

  return data

def check_balances(id):
  with open("./cogs/data.json", "r") as f:
    data = json.load(f)
    f.close()

  if data.get(str(id)) is None:
    data[str(id)] = 0

    jsonString = json.dumps(data)
    with open("./cogs/data.json", "w+") as f:
      f.write(jsonString)
      f.close()

    return data[str(id)]

  return data[str(id)]

def update_balances(method, id, value):
  if type(value) != int and type(value) != float:
    return

  with open("./cogs/data.json", "r") as f:
    bal_data = json.load(f)
    f.close()

  if method.lower() == "add":
    bal_data[str(id)] += value
  elif method.lower() == "subtract":
    bal_data[str(id)] -= value

  jsonString = json.dumps(bal_data)
  with open("./cogs/data.json", "w+") as f:
    f.write(jsonString)
    f.close()

  return bal_data

def supply():
  with open("./cogs/data.json", "r") as f:
    bal_data = json.load(f)
    f.close()

  supply = 0

  for value in bal_data.values():
    supply += value

  return supply