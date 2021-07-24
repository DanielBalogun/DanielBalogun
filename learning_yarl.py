'''This will be used to the change url. Found it on Linkedin."

>>> from yarl import URL
>>> url = URL('https://www.spanishdict.com/conjugate/caer')
>>> new_url = url / "search" % 'verbs'
>>> new_url 
URL('https://www.spanishdict.com/conjugate/caer/search?verbs=')

>>> new_url.host
'www.spanishdict.com'

>>> new_url.path
'/conjugate/caer/search'

>>> new_url.query_string
'verbs='
