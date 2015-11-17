alba_favs = open("alba_fav_foods.txt")
alba = alba_favs.read()
print alba 

vicky_favs = open("vicky_fav_foods.txt")
vicky = vicky_favs.read()
print vicky 

def compare_favs(alba_favs, vicky_favs):
	if alba_favs == vicky_favs:
		print "Our favorite foods are the same!"
	else:
		print 'our favorite foods are different!'
compare_favs(alba_favs, vicky_favs)