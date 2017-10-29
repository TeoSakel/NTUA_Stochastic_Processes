# Stochastic Processes - Computational Exercises

This repository hosts the exercises for the course of Stochastic Processes
taught by [Dr. Michail Loulakis](www.math.ntua.gr/~loulakis/info/Home.html) 
and Dr. Aristides Doumas at the National Technical University of Athens.

The main site of the course, where you can find the book together with other 
relevant material can be found
[here](http://mycourses.ntua.gr/course_description/index.php?cidReq=SEMFE1120)
For a Greek version of the instruction guide check out [Odigies.pdf](Odigies.pdf).
For an English version of the lab, **replace** the notebooks in the main directory 
with those in the `English_version` directory.

## Contents

* [Getting Started](#Getting Started)
  * [Installation Instructions](#Installation Instructions)
* [Python](#Python)
* [Markdown](#Markdown)
* [Jupyter Notebook](#Jupyter Notebook)
  * [Launching a Notebook](#Launching a Notebook)
* [Working on Exercises](#Working on Exercises)

---

## Getting Started

To complete the exercises you need to install [Python](https://www.python.org)
version 3 together with a few non-standard libraries and the
[Jupyter Notebook](https://jupyter.org) app.

Below are some simple instruction on how to install all of them.


### Installation Instructions

The **recommended** and easiest way to install everything at once is through
[Anaconda](https://www.continuum.io/downloads).
Anaconda is a cross-platform (Windows, Mac, GNU/Linux)
python distribution tailored for data science.

To install Anaconda just follow the [link](https://www.continuum.io/downloads)
provided and select the **Python 3** installer that corresponds to your OS.

If for some reason you don't want to install Anaconda, then you must
first install Python 3, either from the [official repository](https://www.python.org) 
or your OS package manager. If you are using `OSX` or `GNU/Linux` then you probably
have Python pre-installed. **However**, you must make sure that you have
Python **3** not 2.

Then you have to install the required packages
specified in [requirements.txt](requirements.txt).
The most sane approach to do this is though your OS package manager. 
If for some reason you cannot use a native package manager, 
then you should use Python's package manager 
[pip](https://docs.python.org/3/installing/).
To install pip (you need to install Python first) check out this
[link](https://pip.pypa.io/en/stable/installing/).

To install everything through pip run one of the following commands in your terminal:

``` shell
# if you only have python 3 you can just write python
python3 -m pip install -r requirements.txt
# or if you don't have admin rights
python3 -m pip install --user -r requirements.txt
```

---

## Python

The language of choice for these exercises is [Python](https://www.python.org/).
Do not be dishearten if you are not familiar with it!
Python's greatest advantage is that it easy to learn and read.
For these exercises, we will make use of Python's most basic scientific libraries:

1. [Numpy](http://www.numpy.org/) for numerical programming
2. [Matplotlib](http://matplotlib.org/) for visualization

other libraries may be used for some exercises but only
to enhance the learning experience and you won't have to interact with them
(unless you want to!).

If you are not familiar with Python or with any of these 2 libraries,
you can get started by completing the first 2 (freely available) courses
provided by [DataCamp](https://www.datacamp.com):

1. [Intro to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science)
2. [Intermediate Python](https://www.datacamp.com/courses/intermediate-python-for-data-science)

Python is an interpreted language, so you can fire-up its terminal and start
giving commands to the computer. This can be useful to experiment with code but
in order to submit the exercises you need to write code the *code cell* of a Jupyter
notebook (see [Jupyter Notebook](#Jupyter Notebook)). If you want to experiment with the terminal,
we suggest you use the [IPython](https://ipython.org/) terminal or qtconsole
(both installed with Anaconda).


## Markdown

The exercises do not only require you to code but also explain what you are doing
and answers some question in free-form text. To do so you have to write regular
text not only comments. To format your text properly you must learn
the markdown syntax. Again, no need to be overwhelmed, this is by far the
easiest syntax you will ever have to learn! 

A brief overview of all the relevant features can be found 
[here](https://goo.gl/PTQn6). For extra examples you can look
[here](https://guides.github.com/features/mastering-markdown/) and
[here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
Also if you click `Enter` on any "markdown-cell" of the provided notebooks, you can
see the source code an get an idea of how it is working.


## Jupyter Notebooks

The exercises are organized in *Jupyter Notebooks*. The notebook is:

> a web application that allows you to create and share documents
> that contain live code, equations, visualizations and explanatory text

For an introductory video about working with *Jupyter Notebooks* follow
this [link](https://youtu.be/HW29067qVWk).

A *Jupyter Notebook* is organized in *cells*. Every cell is either a *code-cell*
or a *markdown-cell*. In the code-cells you write pure Python code (no adjustments needed)
that executes and the output (if visible) is displayed below the cell.
In the markdown-cells you write plain-text following the markdown syntax that will
then be rendered as a rich-format text. In short, it brings together [Python](#Python) and
[Markdown](#Markdown) in order to produce self-contained reports.

### Launching a Notebook

To view and interact with the notebook first you need to install `jupyter` and launch
a notebook from inside the main folder of this repository. To do that:

* Via **terminal**:
  1. Start a new terminal (in Windows with Anaconda use the *"Anaconda prompt"*)
  2. navigate the repository folder (`cd path/to/folder`)
  3. issue the command `jupyter notebook`
* Via **Anaconda Navigator**:
  1. Launch the Anaconda navigator.
  2. Select and launch the *Jupyter Notebook* app.
  3. Navigate to the repository folder.
* For **Windows** with Anaconda:
  1. Make a shortcut of the *Jupyter Notebook* app to your desktop
  (copy from Start-up menu)
  2. Right-click on the new launcher and change the “Start in” field
  by pasting the full path of the repository folder.
  3. Double-click on the *Jupyter Notebook* desktop launcher
  to start the Jupyter Notebook App (note that a terminal will also open).

In all cases, a new page or tab will open in the browser.
If this doesn't happen, or you accidentally close the window,
you can navigate there manually by typing the following address:
[http://localhost:8888/](http://localhost:8888/)

---

## Working on Exercises

To work on the exercises you need to download (and unzip) this repository and
*launch* the `jupyter notebook` from inside the main folder.

Once the main page opens in the browser you can select the exercise you want
to work on and start working. Once you open the `.ipynb` file a new tab or page
will open where a problem is described and (usually) a sample code is given.
Your task is to answer the given question via text and/or code.

Once your are satisfied with your answer convert your notebook to `HTML` 
(`File > Download as... > HTML`) and email the html file to 
[Prof Loulakis](www.math.ntua.gr/~loulakis/info/Home.html).

--- 

