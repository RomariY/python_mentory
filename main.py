import json

from collection.models import Author, Collection
from icon.models import Icon

path = "./data.json"
with open(path, "r") as f:
    data = json.load(f)

icon = Icon(**data["icon"])
print(icon.dict())

author = Author(**data["icon"]["collections"][0]["author"])
# print(author.dict())
collection = Collection(**data["icon"]["collections"][0])
# print(collection.dict())

if __name__ == '__main__':
    print("Running main.py")

