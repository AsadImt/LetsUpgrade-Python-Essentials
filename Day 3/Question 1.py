print('You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is 1000ft, if it is less than that tell pilot to land the plane, or it is more than that but less than 5000ft ask the pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try later”')
altitude = input('Enter altitude - ')
altitude = int(altitude)
if altitude < 1000:
	print('Land the plane')
elif altitude < 5000:
	print('come down to 1000ft')
else:
	print('go around and try')