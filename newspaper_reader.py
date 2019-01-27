"""
* Feedparser in Python:
https://www.pythonforbeginners.com/feedparser/using-feedparser-in-python
* Python RSS Code (Feedparser + Future):
https://wiki.python.org/moin/RssLibraries
* 
https://www.tutorialspoint.com/python/python_reading_rss_feed.htm
* Documentacion:
https://pythonhosted.org/feedparser/
* HTML to Text converter:
https://www.browserling.com/tools/html-to-text
* Feedly
"""
import feedparser
import html2text # To convert html to text (https://pypi.org/project/html2text/)

feeds = {
	'bbc': {
		'portada': 'http://www.bbc.co.uk/mundo/index.xml',
		'lo_ultimo': 'http://www.bbc.co.uk/mundo/ultimas_noticias/index.xml',
		'espana': '',
		'internacional': 'http://www.bbc.co.uk/mundo/temas/internacional/index.xml',
		'opinion': '',
		'deportes': '',
		'tecnologia': 'http://www.bbc.co.uk/mundo/temas/tecnologia/index.xml',
		'ciencia': 'http://www.bbc.co.uk/mundo/temas/ciencia/index.xml',
		'cultura': 'http://www.bbc.co.uk/mundo/temas/cultura/index.xml'
	},
	'europa_press': {
		'portada': 'https://www.europapress.es/rss/rss.aspx',
		'lo_ultimo': '',
		'espana': 'https://www.europapress.es/rss/rss.aspx?ch=00066',
		'internacional': 'https://www.europapress.es/rss/rss.aspx?ch=00069',
		'opinion': '',
		'deportes': 'https://www.europapress.es/rss/rss.aspx?ch=00067',
		'tecnologia': 'https://www.europapress.es/rss/rss.aspx?ch=00564',
		'ciencia': '',
		'cultura': 'https://www.europapress.es/rss/rss.aspx?ch=00126'
	},
	'el_espanol': {
		'portada': '',
		'lo_ultimo': '',
		'espana': '',
		'internacional': '',
		'opinion': '',
		'deportes': '',
		'tecnologia': '',
		'ciencia': '',
		'cultura': ''
	},
	'libertad_digital': {
		'portada': 'http://feeds2.feedburner.com/libertaddigital/portada',
		'lo_ultimo': '',
		'espana': 'http://feeds2.feedburner.com/libertaddigital/nacional',
		'internacional': 'http://feeds2.feedburner.com/libertaddigital/internacional',
		'opinion': 'http://feeds2.feedburner.com/libertaddigital/opinion',
		'deportes': 'http://feeds2.feedburner.com/libertaddigital/deportes',
		'tecnologia': 'http://feeds2.feedburner.com/libertaddigital/internet',
		'ciencia': '',
		'cultura': 'http://feeds.feedburner.com/libertaddigital/cultura'
	},
	'el_pais': {
		'portada': 'http://ep00.epimg.net/rss/elpais/portada.xml',
		'lo_ultimo': 'http://ep00.epimg.net/rss/tags/ultimas_noticias.xml',
		'espana': 'http://ep00.epimg.net/rss/politica/portada.xml',
		'internacional': 'http://ep00.epimg.net/rss/internacional/portada.xml',
		'opinion': 'http://ep00.epimg.net/rss/elpais/opinion.xml',
		'deportes': 'http://ep00.epimg.net/rss/deportes/portada.xml',
		'tecnologia': 'http://ep00.epimg.net/rss/tecnologia/portada.xml',
		'ciencia': 'http://ep00.epimg.net/rss/elpais/ciencia.xml',
		'cultura': 'http://ep00.epimg.net/rss/cultura/portada.xml'
	},
	# No aptos
	'20_minutos': { # Resumenes largos
		'portada': 'https://www.20minutos.es/rss/',
		'lo_ultimo': '',
		'espana': 'https://www.20minutos.es/rss/nacional/',
		'internacional': 'https://www.20minutos.es/rss/internacional/',
		'opinion': 'https://www.20minutos.es/rss/opiniones/',
		'deportes': 'https://www.20minutos.es/rss/deportes/',
		'tecnologia': 'https://www.20minutos.es/rss/tecnologia/',
		'ciencia': 'https://www.20minutos.es/rss/ciencia/',
		'cultura': 'https://www.20minutos.es/rss/cultura/'
	},
	'el_mundo': { # Sin resumenes
		'portada': 'https://e00-elmundo.uecdn.es/elmundo/rss/portada.xml',
		'lo_ultimo': '',
		'espana': 'https://e00-elmundo.uecdn.es/elmundo/rss/espana.xml',
		'internacional': 'https://e00-elmundo.uecdn.es/elmundo/rss/internacional.xml',
		'opinion': '',
		'deportes': 'https://e00-elmundo.uecdn.es/elmundodeporte/rss/portada.xml',
		'tecnologia': '',
		'ciencia': 'https://e00-elmundo.uecdn.es/elmundo/rss/ciencia.xml',
		'cultura': 'https://e00-elmundo.uecdn.es/elmundo/rss/cultura.xml'
	},
}

# Parser object
parser = html2text.HTML2Text()
parser.images_to_alt = True # Discard image data, only keep alt text
parser.ignore_images = True # Don't include any formatting for images
parser.ignore_links = True # Ignores links
parser.ignore_tables = True
parser.body_width = 1000 # Number of charcaters per line (long number so no '\n' character appears)

d = feedparser.parse(feeds['bbc']['portada'])

try:
	print('__________feed[title]:__________')
	print(d['feed']['title'])
	if(d['bozo']==0):
		print 'xml well-formed'
	else:
		print 'ERROR xml not well-formed'

	print len(d['entries'])

	n = raw_input('Numero de la noticia: ')
	n = int(n)
	print('__________title:__________')
	print(d['entries'][n]['title'])
	print('__________summary:__________')
	print(d['entries'][n]['summary'])
	print('__________summary_detail[type]:__________')
	print(d['entries'][n]['summary_detail']['type'])
	print('__________summary_detail[value]:__________')
	summary = d['entries'][n]['summary_detail']['value']
	if(d['entries'][n]['summary_detail']['type'] == 'text/html'):
		print('### Summary parsed ###')
		summary = parser.handle(summary)
		# If text ends with '\n', ti is removed
		while(summary[-1:] == '\n'):
			print 'fix n'
			summary = summary[0:-1]
	print(summary)
except KeyError as e:
	print('KeyError: ' + str(e))
