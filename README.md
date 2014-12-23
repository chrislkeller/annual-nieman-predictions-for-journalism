Nieman Lab Predictions for Journalism 2015
==========================================

As has become tradition, Nieman Lab this year [posted predictions and thoughts](http://www.niemanlab.org/collection/predictions-2015/) from those in and around the news business in an attempt to foreshadown ways the way we report, deliver and present news will change in 2015.

In all, 65 different pieces were posted.

I wanted to read them all - eventually - but I did not want to open each link and save the article to [Instapaper](https://www.instapaper.com/). So I wrote a little program to pull the content down combine the articles into one HTML file that I could save for later.

It's not perfect - some accents in names and punctuation characters weren't deciphered - but the goal was to create an article filled with articles, not design an ebook - though the thought had crossed my mind. And if I were to do that, Calibre works well for creating ebooks from web content.

Anyway, for now the resulting HTML file is [here](https://github.com/chrislkeller/nieman-predictions-for-2015/blob/master/index.html), provided Nieman Lab doesn't get upset for me re-appropriating their content.

The [scraper](https://github.com/chrislkeller/nieman-predictions-for-2015/blob/master/scraper.py) is also here if you're interested in improving it for any reason.

**Usage**

Here's how I loaded the HTML file into Instapaper. Your mileage with other "read it later" services may vary.

* Save ```index.html``` to a location like your Desktop.
* On a *nix machine, open your command line program of choice and ```cd``` to the location where you saved the ```index.html``` file. In this example it would be ```cd ~/Desktop```
* Assuming you have Python installed, start the the local webserver by entering the following into the terminal: ```python -m SimpleHTTPServer 8880```
* Open a browser and navigate to ```http://127.0.0.1:8880/```.
* There you will find the article of articles. I used the Instapaper bookmarklet to pull the content down and save for later.

**Scraper**

* Clone or fork the repo.
* Run ```pip install -r requirements.txt``` from your command line program of choice.
* Run ```python scraper.py``` to run the scraper. Be kind when running. You'll be sending traffic to Nieman Lab.