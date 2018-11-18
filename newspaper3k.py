# https://newspaper.readthedocs.io/en/latest/

from newspaper import Article

url = 'https://elpais.com/elpais/2018/11/17/gastronotas_de_capel/1542444402_412360.html#comentarios'

article = Article(url)

article.download() # Descargo datos de la url

#print(article.html)

article.parse()

print('title:')
print(article.title)

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

