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

portada_feed = ['https://www.europapress.es/rss/rss.aspx', 'http://ep00.epimg.net/rss/elpais/portada.xml', 'https://e00-elmundo.uecdn.es/elmundo/rss/portada.xml', 'https://www.abc.es/rss/feeds/abcPortada.xml', 'https://www.lavanguardia.com/mvc/feed/rss/home']
lo_ultimo_feed = ['http://ep00.epimg.net/rss/tags/ultimas_noticias.xml', 'https://e00-elmundo.uecdn.es/elmundo/rss/espana.xml', 'https://www.abc.es/rss/feeds/abc_ultima.xml']
espana_feed = ['http://ep00.epimg.net/rss/politica/portada.xml', 'https://e00-elmundo.uecdn.es/elmundo/rss/espana.xml', 'https://www.abc.es/rss/feeds/abc_EspanaEspana.xml']
internacional_feed = ['http://ep00.epimg.net/rss/internacional/portada.xml', 'https://e00-elmundo.uecdn.es/elmundo/rss/internacional.xml', 'https://www.abc.es/rss/feeds/abc_Internacional.xml']
opinion_feed = ['http://ep00.epimg.net/rss/elpais/opinion.xml', 'https://www.abc.es/rss/feeds/abc_opinioncompleto.xml']
deportes_feed = ['http://ep00.epimg.net/rss/deportes/portada.xml', 'https://e00-elmundo.uecdn.es/elmundodeporte/rss/portada.xml', 'https://www.abc.es/rss/feeds/abc_Deportes.xml']
tecnologia_feed = ['http://ep00.epimg.net/rss/tecnologia/portada.xml', 'http://rss.elmundo.es/rss/descarga.htm?data2=13', 'https://www.abc.es/rss/feeds/abc_Tecnologia.xml']
ciencia_feed = ['http://ep00.epimg.net/rss/elpais/ciencia.xml', 'https://e00-elmundo.uecdn.es/elmundo/rss/ciencia.xml', 'https://www.abc.es/rss/feeds/abc_Ciencia.xml']
cultura_feed = ['http://ep00.epimg.net/rss/cultura/portada.xml', 'https://e00-elmundo.uecdn.es/elmundo/rss/cultura.xml', 'https://www.abc.es/rss/feeds/abc_Cultura.xml']
local_feed = ['/home/sergio/Downloads/rss']


d = feedparser.parse(portada_feed[0])
#print d.headers['content-type']
'''file = open('testfile.json','w')
file.write(d)
file.close()'''
new_n = input('Escoge la noticia: ')
#if(not d['bozo']):
if(True):
	'''print("d['url']", d['url'])
				print("d['version']: ", d['version'])
				print("d['channel']['title']", d['channel']['title'])
				print("d['channel']['description']", d['channel']['description'])
				print("d['channel']['link']", d['channel']['link'])
				#print(d['channel']['wiki_interwiki'])
				print("d['items']", d['items'])'''
	print len(d['entries'])
	
	print '>> link: ', d['entries'][new_n]['link']
	print '>> title: ', d['entries'][new_n]['title']
	#print '>> description: ', d.entries[new_n].description
	print '>> summary: ',d['entries'][new_n]['summary']
	print '>> text: ',d['entries'][new_n].content
	print '>> keys: ', d['entries'][new_n].keys()
else:
	print 'ERROR xml not well-formed'

'''print '>> summary:',d['entries'][new_n]['summary']
print '>> text:',d['entries'][new_n].content

print '>> fsffsafaf ', d["items"][0]['summary']'''