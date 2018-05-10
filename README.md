# Movie Trailer Website Project

## Intro

The main idea of the project is to write server-side **Python** code to store 
a list of my favorite movies, including box art imagery and a movie trailer URL. 
The code is then used to generate a static web page allowing visitors to browse 
the movies and watch the trailers.

## Implementation of the project

- `media.py` contains the class *Movie* with the method *show_trailer* defined;
- `entertainment_center.py` contains the information about the movies (objects 
  of the class *Movie*), the list of these movies, and the call of the function
  that generates and opens the webpage;
- `fresh_tomatoes.py` (source - https://github.com/udacity/ud036_StarterCode) 
  contains the styles and scripting for the webpage as well as the functions to 
  generate and open it.

## Dependencies (built with) 

- [Python 2.7.14](https://www.python.org/downloads/)
- [HTML](https://www.w3.org/html/)
- [CSS](https://www.w3.org/Style/CSS/)
- [Bootstrap 3](http://getbootstrap.com/docs/3.3/)
- [Javascript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
- [JQuery](http://jquery.com/)

## How to run it

- download the files;
- make sure they are stored in the same folder;
- make sure your browser is up to date;
- make sure **Python** is installed on your computer. Otherwise, download and 
  install *Python 2.7.14* from the download page (see Dependencies above);
- run `python entertainment_center.py` from the command line. It should generate and
  open the webpage with the movies in your default browser;
- click on the movie to watch its trailer.

## Outro: comments

For more information on the implementation of the class and objects, the logic 
of functions and events explore the comments to the `media.py`, 
`entertainment_center.py`, and `fresh_tomatoes.py`.
