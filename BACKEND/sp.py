article = '''
East Repair Inc.

1912 Harvest Lane
New York, NY 12210

Bill To Ship To
Vinayak Smith John Smith
2 Court Square 3787 Pineview Drive
New York, NY 12210 Cambridge, MA 12210
ary DESCRIPTION
1 | Front and rear brake cables
2 | New set of pedal arms

3 | Labor 3hrs.

Terms & Conditions
Payment is due within 15 days

Please make checks payable to: East Repair Inc.

INVOICE

Invoice # us-001

Invoice Date 1102/2019

P.o# 2312/2019

Due Date 26/02/2019

UNIT PRICE AMOUNT

100.00 100.00
15.00 30.00
5.00 15.00
Subtotal 145.00
Sales Tax 6.25% 9.08
TOTAL $154.06
'''

import spacy


def get_details(text):
	spacy_nlp = spacy.load('testnew')
	document = spacy_nlp(text)

	print('Original Sentence: %s' % (text))
	txt=""
	for element in document.ents:
	    print('Type: %s, Value: %s' % (element.label_, element))
	    txt+="Type: "+ str(element.label_)+" , "+"Value: " +str(element)

	return txt