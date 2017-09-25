from mtgsdk import Card, Set, Type, Supertype, Subtype, Changelog
import matplotlib.pyplot as plt
from urllib2

# Get list of all blue cards
blue_cards = Card.where(color="U")
# Get first ten blue cards
first_ten_blue_cards = blue_cards.where(page=1).where(pageSize=10).all()

# Print name of first ten blue cards
for card in first_ten_blue_cards:
	print card.name 

# Get randomly made booster from khans of tarkir expansion
ktk_booster = Set.generate_booster('ktk')

# Print name and rarity from cards in booster
for card in ktk_booster:
	print "Name: %s" % card.name 
	print "\tRarity: %s\n" % card.rarity 


# Open image from url
f = urllib2.urlopen(ktk_booster[0].image_url)
# Load image from url
a = plt.imread(f)
# Plot card image
plt.imshow(a)
plt.show()

# Plot all cards in booster (extremely slow :s)
f, axarr = plt.subplots(4, 4)
axes = [axarr[j][i] for j in range(len(axarr)) for i in range(len(axarr[j]))]

for card, ax in zip(ktk_booster, axes[:-1]):
	# Open image from url
	img = urllib2.urlopen(card.image_url)
	# Load image from url
	a = plt.imread(img)
	ax.imshow(a)
	ax.set_axis_off()

plt.show()