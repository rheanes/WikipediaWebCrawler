# WikipediaWebCrawler
This is a project that I created in Python for my Data Mining class. 
I created a web crawler using Scrapy to perform a bredth first search on 1000 wikipedia pages.
My starting page was the Computer science wikipedia page. The goal of th project was to extract the most important computer science topics. 
To process my data, I removed all leftover html elements, removed all stopwords from the NLTK stopwords library, tokenized my words, stemmed my words, and removed punctuation. 


-setting.py contains the setting that I used for my Web crawler.
-spider.py contains my web crawler and how it extracts the data from the web pages.
-DataAnaysisOfWikipedia.ipynb is the code that I used to process the data. This code was created in GoogleCollab. This file also contains the output for the program.
-CSWiki1000 contains a json file with the data that was retrieved from my web crawler. 
