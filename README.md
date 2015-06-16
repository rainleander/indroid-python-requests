# indroid-python-requests

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
<code>pip install requests
git clone https://github.com/rainsdance/indroid-python-requests
cd indroid-python-requests</code>

<h4>Use</h4>
<code>python requests-simple.py</code>

Script prompts for a string (What would you like to search for?) and then an integer (How many results would you like to see?) and returns the unformatted google results.

<h3>selenium-complex.py</h3>
Scrape Google search results with Selenium based on https://github.com/DanMcInerney/search-google

<h4>Dependencies</h4>
<ul><li>python 2.7</li>
<li>Selenium</li></ul>

<h4>Installation</h4>
<code>pip install selenium
git clone https://github.com/rainsdance/indroid-python-requests
cd indroid-python-requests</code>

<h4>Use</h4>
<code>python selenium-complex.py -s "foo bar test"</code>

Will open the firefox browser, search for "foo bar test" on google.com and return one page of ten results with the title and url of each result.
