import newspaper

url_elmundo = 'https://www.elmundo.es/'
url_elpais = 'https://elpais.com/'
url_20minutos = 'https://www.20minutos.es/'
url_abc = 'https://www.abc.es/'
url_larazon = 'https://www.larazon.es/'

url_marca = 'https://www.marca.com/'
url_as = 'https://as.com/'
url_mundodeportivo = 'https://www.mundodeportivo.com/'

elmundo_paper = newspaper.build(url_elmundo, memoize_articles=False)
elpais_paper = newspaper.build(url_elpais)

print('\n\n')
print('########' + url_elmundo + ': ########')

print('>> article:')
for article in elmundo_paper.articles:
	print(article.url)

print('>> category:')
for category in elmundo_paper.category_urls():
	print(category)

print('>> feed_url:')
for feed_url in elmundo_paper.feed_urls():
     print(feed_url)
print(elmundo_paper.size())


print('\n\n')
print('########' + url_elpais + ': ########')

print('>> article:')
for article in elpais_paper.articles:
	print(article.url)

print('>> category:')
for category in elpais_paper.category_urls():
	print(category)
print('>> feed_url:')
for feed_url in elpais_paper.feed_urls():
     print(feed_url)