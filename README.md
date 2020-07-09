# indroid-python-requests

During an interview with Indroid, the technical interview was a homework. The original email was quite intimidating, "1. make a function that accepts a string and returns the Google-results using python and the results-module. 2. make a function that accepts a string and returns the google results using python and selenium. Selenium controls a browser and uses Firefox as default."

One of the first things I did was re-arrange the two part assignment into smaller pieces for better google-a-bility (yes, it's a word):

1. Make a function 
 	- accepts a string 
	- returns the Google-results 
	- use Python and the requests-module
2. make a function 
	- accepts a string 
	- returns the Google results 
	- use Python and Selenium
		- which controls a browser (default: Firefox). 

<h3>requests-simple.py</h3>
Scrape Google search results with the requests python module.

<h4>Dependencies</h4>
<ul><li>python 2.7</li></ul>

<h4>Installation</h4>
```shell
pip install requests
git clone https://github.com/rainsdance/indroid-python-requests
cd indroid-python-requests
```

<h4>Use</h4>
```shell
python requests-simple.py
```

Script prompts for a string (What would you like to search for?) and then an integer (How many results would you like to see?) and returns the unformatted google results.

<h3>selenium-complex.py</h3>
Scrape Google search results with Selenium based on https://github.com/DanMcInerney/search-google

<h4>Dependencies</h4>
<ul><li>python 2.7</li>
<li>Selenium</li></ul>

<h4>Installation</h4>
```shell
pip install selenium
git clone https://github.com/rainsdance/indroid-python-requests
cd indroid-python-requests
```

<h4>Use</h4>
```shell
python selenium-complex.py -s "foo bar test"
```

Will open the firefox browser, search for "foo bar test" on google.com and return one page of ten results with the title and url of each result.
