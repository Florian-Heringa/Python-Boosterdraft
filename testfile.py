from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog
import matplotlib.pyplot as plt
from urllib.request import urlopen

# Get list of all blue cards
blue_cards = Card.where(color="U")
# Get first ten blue cards
first_ten_blue_cards = blue_cards.where(page=1).where(pageSize=10).all()

# Print name of first ten blue cards
for card in first_ten_blue_cards:
	print(card.name)

# Get randomly made booster from khans of tarkir expansion
ktk_booster = Set.generate_booster('ktk')

# Print name and rarity from cards in booster
for card in ktk_booster:
	print("Name: %s" % card.name)
	print("\tRarity: %s" % card.rarity)


# Open image from url
f = urlopen(ktk_booster[0].image_url)
# Load image from url
a = plt.imread(f)
# Plot card image
plt.imshow(a)
plt.show()