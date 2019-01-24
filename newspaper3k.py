# https://newspaper.readthedocs.io/en/latest/

from newspaper import Article

url = 'https://elpais.com/elpais/2018/11/17/gastronotas_de_capel/1542444402_412360.html#comentarios'
url = 'https://elpais.com/economia/2019/01/23/actualidad/1548224324_644426.html#?ref=rss&format=simple&link=link'
url = 'https://www.abc.es/espana/casa-real/abci-reyes-inauguran-fitur-normalidad-habitual-y-acompanados-publico-201901231252_noticia.html'
url = 'https://www.efe.com/efe/espana/portada/sanchez-dice-a-guaido-que-unas-elecciones-son-la-salida-idonea-para-venezuela/10010-3876949'

article = Article(url)

article.download() # Descargo datos de la url

#print(article.html)

article.parse()

print('title:')
print(article.title)

print('article.summary:')
print(article.summary)

print('authors:')
print(article.authors)

print('publish_date:')
print(article.publish_date)

print('text:')
print(article.text)

print('top_image:')
print(article.top_image)

print('movies:')
print(article.movies)

