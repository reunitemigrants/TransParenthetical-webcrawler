from topia.termextract import extract


def extract_keywords(path):
	file = open(path,'r')
	text = file.read()
	extractor = extract.TermExtractor()
	extracted = extractor(text)
	return extracted

print 'Extract Keywords'

keywords = extract_keywords('output.txt')
import json
with open('data.json', 'w') as outfile:
    json.dump(keywords, outfile)
