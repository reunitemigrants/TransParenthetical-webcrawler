
def contains_keywords(keywords):
	det_keywords = ['ICE','ice', 'immigration']

	for score, word in keywords:
		if word in det_keywords:
			print('keyword found {0}'.format(word))
			return True
	print('No Matches')
	return False