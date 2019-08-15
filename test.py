from models.item import Item

url = "https://www.johnlewis.com/samsung-addwash-ww90k5410ww-eu-washing-machine-9kg-load-a-energy-rating-1400rpm-spin-white/p2523271"
tag_name = "p"
query = {"class": "price price--large"}

item = Item(url, tag_name, query)
item.save_to_mongo()

items_loaded = Item.all()
print(items_loaded[0].load_price())