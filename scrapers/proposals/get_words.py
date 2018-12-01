import keywords_rake as kw
import download as dl



def get_keywords_from_file(path):
	text = dl.convert_pdf_to_txt(path)
	keywords = kw.extract_keywords(text)
	return keywords	

if __name__ == '__main__':
	keywords = get_keywords_from_file('minutes_test.pdf')
	print(keywords)