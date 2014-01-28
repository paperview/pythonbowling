totalRolls = "XXXXXXXXXXXX"
#totalRolls = "5/5/5/5/5/5/5/5/5/5/5"
#totalRolls ="90909090909090909090"
#totalRolls = "905/X34068/22X0934"


def valueof(string):
	print string
	value = 0
	if string == 'X':
		value = 10
	elif string == '/':
		value = 10
	else:
		value = float(string)
	return value


def consolidateSparesIntoFrame(array):
	i = 0
	for roll in array:
		if roll['s'] == '/':
			total = roll['v'] + array[i+1]['v']*2
			total = total - array[i-1]['v']
			array[i] = {'total_for_frame':total, 's':str(total)}
		elif roll['s'] == 'X':
			if array.index(roll) <= len(array[:-3]):
				total = roll['v'] + array[i+1]['total_for_frame'] + array[i+2]['total_for_frame']
				array[i] = {'total_for_frame': total, 's':str(total)}
			elif array.index(roll) >= len(array[:-2]):
				del array[-2]
				del array[-1]
		i+=1
	return array



def tally(totalRolls):

	arrayPerRollArray = []

	for x in totalRolls:
		arrayPerRollArray.append({
			'v': valueof(x),
			's': x,
			'total_for_frame': valueof(x),
		})

	arrayPerRollArray = consolidateSparesIntoFrame(arrayPerRollArray)

	scoreTotal = 0;

	previous_frames = []
	i = 0
	for roll in arrayPerRollArray:
		previous_frames.append(roll)

		if len(previous_frames) > 2:
			previous_frames = previous_frames[1:]

		scoreTotal += roll['total_for_frame']

		i+=1

	print scoreTotal;


tally(totalRolls)