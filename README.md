newspaper3k installation (only on Python 3):
https://newspaper.readthedocs.io/en/latest/

- Install ``pip3`` command needed to install ``newspaper3k`` package::

    $ sudo apt-get install python3-pip

- Install the distribution via pip::

    $ pip3 install newspaper3k

nltk error:
https://stackoverflow.com/questions/4867197/failed-loading-english-pickle-with-nltk-data-load

- Open a python shell and type:

	>>> import nltk
	>>> nltk.download()
	
Then an installation window appears. Go to the 'Models' tab and select 'punkt' from under the 'Identifier' column. Then click Download and it will install the necessary files. 