# Projects with Web Server Framework Django
*(some with JS and Python, some with just one or the other)*

## Note On "logic.py" and Breaking Out The Data Transformations
**You will see that we were taught to break out our data transformations from our views creation.  I was later informed this is more of a standard for larger projects and that in a traditional Model-View-Controller layout, the code I store in logic.py would be incorporated into my views.py.  Our instructor most recently worked at Yelp! so this style probably came out of on the job practice.**

* [Multi-Madlib](multi_madlib)
  * Pair Project with Matthew K.
  * However, we had not yet learned about storing one's SECRET_KEY locally and not pushing it to GitHub.  Not learned until Ally_Finder below.
  * Specifically instructed to use the HTTP responses
  * Earliest Django project and were instructed to keep all Views coding in views.py
  * Partner and I agreed we wanted to spend our time learning how to write this correctly, and chose to repeat the same madlib rather than spend precious time jointly creating new ones.
* [Book Stats](book_stats.py)
  * Extended what we learned in [Word Count](early_python/word_count.py)
  * I have a habit of placing child functions ABOVE their parent functions in my Python modules.  
  * Still one HTML page, so no real use of urls.py or views.py, but logic.py is used
  * As with Word Count, I could definitely play with this one more, adding little additional options for how someone could play with the data.  I loved these kinds of problems - take data input, fiddle with the data in myriad of ways based on user choices.
* [Jokes](jokes.py)
* Flutter
* [Ally_Finder](https://github.com/shedwyn/bias-tracker)
  * Final capstone project
  * Link takes you to the GitHub code respository itself
  * Project is fully deployed (and still being developed and changed) on Heroku and best accessed from my profile website www.foughfibre.org due to notes on Mac OS issues with security and the need to have a pass code and user name in order to use the features.
* Ignored
  * *Both Polls and ToDo projects were shared projects done on someone else's
  machine entirely, and before I learned how to pull or clone a respository.
  Until pulling those reaches the top of my priority list, I am not sure all
  code was copied over correctly from my partners.*
