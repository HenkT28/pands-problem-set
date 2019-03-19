# Problem Set Solutions 2019 - Programming and Scripting

This document contains the ten problems for Problem Set Solutions 2019, for Programming and Scripting module (GMIT  H.Dip Data Analytics  Academic Year 2018 - 2019).

## Getting Started - how to download the repository

1. Go to Github - User Account: HenkT28
2. Click on the download button, and copy/paste the link:
https://github.com/HenkT28/pands-problem-set.git

### Prerequisites - how to run the code

1. Make sure you have Python installed, or Cmder software for running the python scripts:
https://www.python.org/downloads/

https://cmder.net/


2. Also I recommend you to download and install Anaconda:
(https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))

Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing.
Anaconda Navigator is a desktop graphical user interface (GUI) included in Anaconda distribution that allows users to launch applications and manage conda packages, environments and channels without using command-line commands.

### Running the python scripts.

Python can be run in two different ways: in interactive mode or in script mode.

https://docs.python.org/3/tutorial/interpreter.html

https://en.wikibooks.org/wiki/Python_Programming/Interactive_mode

http://www.pybloggers.com/2017/10/coding-in-interactive-mode-vs-script-mode/

The normal mode, the script mode, is the mode where the scripted and finished .py files are run in the Python interpreter. Instead of having to run one line or block of code at a time (interactive mode), you can run all the code at once. 

As this problem set contains all completed .py scripts, I suggest you run the scripts in normal mode. 

For example, from cmder go to the directory containing the .py scripts, by using cd command, and run the programs as follows:
python <script_name>.py

## Below are the ten problems, and what each script does

1. sumupto.py:

This program asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

For example:
$ python sumupto.py

Please enter a positive integer: 10
55

2. begins-with-t.py:

This program outputs whether or not today is a day that begins with the letter T. 
An example of running this program on a Thursday is as follows:
$ python begins-with-t.py

Yes - today begins with a T.

An example of running it on a Wednesday is as follows:
$ python begins-with-t.py

No - today does not begin with a T.

3. divisors.py:

A program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

$ python divisors.py

1002
1014
1026
etc
9990

4. collatz.py:

This program asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

$ python collatz.py

Please enter a positive integer: 10
10 5 16 8 4 2 1

5. primes.py:

This program asks the user to input a positive integer and tells the user whether or not the number is a prime.

$ python primes.py

Please enter a positive integer: 19
That is a prime.

6. secondstring.py:

This program takes a user input string and outputs every second word.

$ python secondstring.py

Please enter a sentence: The quick brown fox jumps over the lazy dog.
The brown jumps the dog

7. squareroot.py:

This program takes a positive floating point number as input and outputs an approximation of its square root.

$ python squareroot.py:

Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

8. python date_time.py:

Write a program that outputs today’s date and time in the format ”Monday, January 10th 2019 at 1:15pm”.

$ python date_time.py
Monday, January 10th 2019 at 1:15pm

9. second.py:

This program reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

$ python second.py moby-dick.txt

Title: Moby Dick; or The Whale
CHAPTER 1
Call me Ishmael. Some years ago--never mind how long particular to interest me on shore, I thought I would sail about a ...

10. functions.py:

Write a program that displays a plot of the functions x, x2 and 2x in the range [0, 4]. The plots of the functions x, 2x and x2, are displayed in the same graph.

$ python functions.py

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

