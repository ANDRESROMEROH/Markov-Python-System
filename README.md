## Markov-Pytho-App
Python (**QT GUI**) application that can emulate and create output strings as result of the application of a series of rules and input strings based on the known "Markov algorithm".

In order to install the **PyQT** development tools you can follow:

**https://gist.github.com/ANDRESROMEROH/9d252fb502c841769877fc8cdbf6943d**

You can either run the **.EXE** file that is on the same project or run it directly using Python from your terminal:

**For Windows:**
-
Make sure you are running Python version 3.7 or higher, older versions could cause problem on the way the special characters are processed through UNICODE.

Python 3 Windows Download: 
**https://www.python.org/ftp/python/3.7.1/python-3.7.1.exe**

From your command line / integrated console, locate the project root folder and execute:

    python Markov.py

**For Linux/Unix:**
-
Just as in Windows you need to make sure you are running version 3.0.x of Python, some versions of Ubuntu comes with Python 2 by default which will cause issues with the GUI.

Python 3 Linux installation command:

    sudo apt-get install python3.6

To run the program from the bash console you will need to specify the Python version or it will run on Python 2 automatically, locate the project root folder and run:

    python3 Markov.py

It can be done this way or setting Python3 as the default for the intruction `python` using the command `python Markov.py` and then running `
source ~/.bash_aliases or source ~/.bashrc`

**How To**
-
Using the program is very simple, if you don't know anything about Markov Algorithms you can get started with this **Medium** post: 
**https://unnikked.ga/how-to-execute-a-markov-algorithm-7b59834eb2b5** 

Or the documentation available on Wikipedia which is pretty good:
**https://en.wikipedia.org/wiki/Markov_algorithm**

With that you should be all set, let's take a look into the user interface:

![enter image description here](https://lh3.googleusercontent.com/lXj1GKoQDjmLjePoNownuhiTk37GtiU0SQEYsgR8ODMPHG85kRjlSIqdUjBEOTOKj6y_8M7A5g9O "User Interface")

You can either work just typing your algorithms on the editor section or loading a predefined algorithm from a **.TXT** file, the algorithms will need to follow the convention shown as a water mark in the editor section, let's see 2 different examples to see its work:

**Algorithm #1:**

    "A" → "apple"
	"B" → "bag"
	"S" → "shop"
	"T" → "the"
Using the string :

> I bought a B of As from T S.

It will produce the Output: 

> I bought a bag of apples from the shop.


![enter image description here](https://lh3.googleusercontent.com/sXsOU8854VrUlgdJ2zs8BrvQ276vKAfEZ4Kxes4J8CoWNY_pk9jbC6fDexfVAgP02G9aQAmS5pmx)

You can also create and run more complex algorithms using aux variables, symbols, markers an different rules as can be observed on algorithm #2.

**Algorithm #2:**

Algorithm that duplicates a given string...

    #symbols abcdefghijklmnopqrstuvwxyz0123456789

	#vars xy

	#markers αβθμ

	P1:yxβ → xβy

	P2:θy → yβyθ

	P3:β → μ

	P4:μ → Λ

	P5:θ → Λ.

	P6:Λ → θ
Using the string:

> elephant

It will produce the output:

> elephantelephant

These are just 2 of the examples that can be executed within the app, development is still opened and there might be new algorithms which have not been tested.

Enjoy!...

**Support:**
-
andres.romero22@outlook.com

