import newspaper

url_elmundo = 'https://www.elmundo.es/'
url_elpais = 'https://elpais.com/'
url_20minutos = 'https://www.20minutos.es/'
url_abc = 'https://www.abc.es/'
url_larazon = 'https://www.larazon.es/'

url_marca = 'https://www.marca.com/'
url_as = 'https://as.com/'
url_mundodeportivo = 'https://www.mundodeportivo.com/'

url = 'https://www.elmundo.es'

paper = newspaper.build(url, memoize_articles=False, languaje = 'es')


print('\n\n')
print('########' + url + ': ########')

print('>> article:')
for article in paper.articles:
	print(article.url)

print('>> category:')
for category in paper.category_urls():
	print(category)

print('>> feed_url:')
for feed_url in paper.feed_urls():
    print(feed_url)

print(paper.size())

i = input("Introduce el numero del articulo: ")

first_article = paper.articles[int(i)]

first_article.download()
first_article.parse()
print('first_article.url')
print(first_article.url)
print('first_article.title')
print(first_article.title)
print('first_article.authors')
print(first_article.authors)
print('first_article.top_image')
print(first_article.top_image)
print('first_article.text')
print(first_article.text)
print('first_article.images')
print(first_article.images)
print('first_article.movies')
print(first_article.movies)
first_article.nlp()

print('first_article.summary')
print(first_article.summary)
print('first_article.keywords')
print(first_article.keywords)