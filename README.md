vanhackaton-split-replace-machine-learning
===================

This project was created fo Vanhackathon 2017. It is a machine learning code to segment and uppercase unknown words

----------

Usage
-------------

Before execute for the first time, install the nltk package: 

LINUX: sudo pip install -U nltk
WINDOWS: pip install nltk 

After this, in the code, uncomment the line 6 nltk.download('punkt') and execute the code, it will download the dictionary for english language

When the code finish executin, comment the line 6 again, the dictionary will be installed in your computer 

In line 77 you can test different texts as you want:

segmentedList = segment(PUT HERE YOUR TEXT IN STRING FORMAT)

Have Fun!

Pre-requisites
=======
 - Python 2.7 or above
 
Todo
====

Put the unknow words to be uppercase