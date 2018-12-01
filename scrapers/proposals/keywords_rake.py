from rake_nltk import Rake




def extract_keywords(text):
	r = Rake()
	r.extract_keywords_from_text(text)
	return r.get_ranked_phrases_with_scores()
if __name__ == '__main__':
	file = open('output.txt', 'r')
	text = file.read()
	file.close()
	print(extract_keywords(text))