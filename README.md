# Words to learn.

Website: http://coursework.pythonanywhere.com/

Presentation of the resault on youtube: https://youtu.be/6rsad4LrfI8

Author: Danylo Sahaidak <sahaidak@ucu.edu.ua>

Project to learn English language. 
Sometimes limited vocabulary becomes an obstacle to studying English. People are trying to learn some words, but they don't use them, and forget quickly. This project was written to create a list of the word which person will find useful, as they are from the feald the peson is interested about.

The main goal of the project is to create a dynamical English thematic dictionary baced on New Yourk Times articles. NYT is great source for learning English lenguage. Articles are updeting frequently so dictionaries as well.

Dictionary is created from words that meets most often in the article, but all must-know words are deleting.
It is parsing NYT articles and getting from it words to work with. There are avaliable 26 themes on which user can create a dictionary, which will be displayed on separate html page.

For saving the dictionary was created new class WordsDict that is the self-sorted dictionary. (classes/dict_class.py)

Also was created the database of around 4000 words that are the most frequently seen in arcticles. It's quite accurate but contains some words used only in NYT arcticles (line New, Yourk, Times, Ads...) All that words are excluded from the final dictionary.

The creation of dictionary on 1 arcticle takes less than 2 seconds for 5 arcticles it's around 10 seconds (on hosting it's faster than on my pc) and for 10 arcticles around 30 seconds.

The documentation is in docs folder.
