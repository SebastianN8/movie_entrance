#
# movie_entrance.py
#
# Created by: Sebastian N
# Created on: March
#
# This program decides what type of movies can the user watch
#

def movie_entrance(age_passed_in):
	if age_passed_in > 17:
		print 'You can watch R rated movies alone!!'
	elif age_passed_in > 13:
		print 'You can watch PG-13 rated movies alone!!'
	else:
		print 'You can watch G rated movies!!'


# Variable
age = int(input('Please input your age here: '))

# Calling function
the_result = movie_entrance(age)
