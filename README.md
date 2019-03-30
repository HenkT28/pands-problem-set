# Problem Set Solutions 2019 - Programming and Scripting

This readme contains the 10 problems, and script solutions for Problem Set Assessment 2019, for Programming and Scripting module (GMIT H.Dip Data Analytics - Academic Year 2019 - 2020).

## Getting Started - how to download the repository

1. Go to Github - User Account: HenkT28
2. Click on the download button, and copy/paste the link:

https://github.com/HenkT28/pands-problem-set.git

### Prerequisites - how to run the code

1. Make sure you have Python installed, or Anaconda: 

[a] https://www.python.org/downloads/

Python is developed under an OSI-approved open source license, making it freely usable and distributable, even for commercial use. 

[b] Anaconda:

(https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))

Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing.
Anaconda Navigator is a desktop graphical user interface (GUI) included in Anaconda distribution that allows users to launch applications and manage conda packages, environments and channels without using command-line commands.

2. Also install Cmder software for running the python scripts, from command line:

https://cmder.net/

### Running the python scripts.

Python can be run in two different ways: 

[a] interactive mode

[b] script mode

https://docs.python.org/3/tutorial/interpreter.html

https://en.wikibooks.org/wiki/Python_Programming/Interactive_mode

http://www.pybloggers.com/2017/10/coding-in-interactive-mode-vs-script-mode/

The normal mode, the script mode, is the mode where the scripted and finished .py files are run in the Python interpreter. Instead of having to run one line or block of code at a time (interactive mode), you can run all the code at once. 

As this problem set contains all completed .py scripts, I suggest you run the scripts in normal mode. 

For example, from cmder go to the directory containing the .py scripts, by using cd command, and run the programs as follows:

python <script_name>.py

## Below are the ten problems, and what each script does

1. [sumupto.py]:

This program asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

For example:
$ python sumupto.py

Please enter a positive integer: 10

55


2. [begins-with-t.py]:

This program outputs whether or not today is a day that begins with the letter T. 
An example of running this program on a Thursday is as follows:

$ python begins-with-t.py

Yes - today begins with a T.

An example of running it on a Wednesday is as follows:

$ python begins-with-t.py

No - today does not begin with a T.


3. [divisors.py]:

A program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

$ python divisors.py

1002

1014

1026

etc

9990


4. [collatz.py]:

This program asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1


5. [primes.py]:

This program asks the user to input a positive integer and tells the user whether or not the number is a prime.

$ python primes.py

Please enter a positive integer: 19

That is a prime.


6. [secondstring.py]:

This program takes a user input string and outputs every second word.

$ python secondstring.py

Please enter a sentence: The quick brown fox jumps over the lazy dog.

The brown jumps the dog


7. [squareroot.py]:

This program takes a positive floating point number as input and outputs an approximation of its square root.

$ python squareroot.py

Please enter a positive number: 14.5

The square root of 14.5 is approx. 3.8.


8. [date_time.py]:

Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

$ python date_time.py

Monday, January 10th 2019 at 1:15pm


9. [second.py]:

* This program reads in a text file and outputs every second line. 

* The program should take the filename from an argument on the command line.

$ python second.py moby-dick.txt

Title: Moby Dick; or The Whale

CHAPTER 1

Call me Ishmael. Some years ago--never mind how long particular to interest me on shore, I thought I would sail about a ...

[I will only cover, Title: Moby Dick; or The Whale, CHAPTER 1, as example]


10. [functions.py]:

Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4]. 

$ python functions.py


NOTE:

The plots of the functions x, 2x and x2, are displayed in the same graph.


## Break down into end to end tests

I recommend you run the python scripts from command line, from cmder for example, but make sure you go to the right directory first containing the .py scripts, by using cd command, and then run the script as follows:

python <script_name>.py

There is no need to type in full script name, just by using the tab key on your keyboard it will auto-complete the script name automatically, from the folder location.

## Deployment

First of all I recommend you to go to the official Python website:

https://www.python.org/downloads/release/python-372/

As of now, 19/03/19. Python 3.7.2 is the latest version available for download and can be deployed on Windows, Linux/Unix, MacOS, and other operating systems.

I would suggest you consult the documentation carefully, and follow below links:

https://www.python.org/downloads/

https://docs.python.org/3.7/whatsnew/changelog.html#python-3-7-2-final

Alternatvely install the full Anaconda package which has Python functionality included.

## Built With

* [Python](https://www.python.org/downloads/) - The official Python website
* [cmder](https://cmder.net/) - Official cmder website
* [Anaconda](https://www.anaconda.com/distribution/) - The open-source Anaconda Distribution is the easiest way to perform Python/R data science and machine learning on Linux, Windows, and Mac OS X.

## References

[1] Software Freedom Conservancy. Git.
https://git-scm.com/

[2] Inc. GitHub. Github.

https://github.com/.
[3] GMIT. Quality assurance framework.

https://www.gmit.ie/general/quality-assurance-framework.

[4] [Ian McLoughlin] - I used some test examples explained by Ian McLoughlin, during the Programming and Scripting course, as template in writing up script solutions.

[5] [Stack overflow](https://stackoverflow.com/) - I used Stack Overflow in several of my solutions, as commented in the code.

[6] [Other web sites] - I also used some other web sites as reference. Again they have been mentioned in the comments section of each of the scripts. 

[7] Also referenced official Python websites such as:

* https://www.pythonprogramming.in/

* https://www.pythoncentral.io/

* https://docs.python.org/

* https://realpython.com/

* https://www.tutorialspoint.com/


[8] [Github testing repository] - Finally I've created another repository on GitHub, that I not only used for storing handy and relevant Python scripts, but also to test some solutions for this assessment:

https://github.com/HenkT28/GMIT_Programming_Scripting.git





