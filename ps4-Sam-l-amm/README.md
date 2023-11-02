[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/uUCihEYT)
# Problem Set 4
#### CMSI 1010: Computer Programming and Lab

## Important Dates

 - Released: 2023-10-11 at 12:00 am [PT]
 - Deadline: 2023-10-19 at 11:59 pm [PT]

## Reading
All readings are from the [_Think Python_ textbook](http://greenteapress.com/thinkpython2/thinkpython2.pdf):
* *Good time to review (or get caught up!):* Sections 1.4–1.5 and 2.5
* Sections 5.1–5.3 and 6.1–6.4
* Chapter 10

Take notes from **Chapter 10 _only_** and submit them in the given `ps4_notes.md` file (new notes for the review sections are permitted but will not be included in the grade). Files that end in `.md` look best when written in [GitHub Markdown](https://guides.github.com/features/mastering-markdown/)!

## Programming
**Q2) Middle of a List**—`midpoint.py`

Write a function that returns the value that’s at the middle of a list (_Hint:_ Use `int()` to convert decimal numbers to integer indices). Test your function on several lists (e.g., lists that have two or three elements).

**Q3) Not equal** - not_equal.py

Imagine that the `!=` operator for numbers has suddenly been removed from the Python programming language. We need to find a way to replace it with the remaining operators in the language. Remember that before it went missing, the `!=` operator took two numbers, and returned `True` if they were not equal to one another, and `False` otherwise.

In `not_equal.py`, write a function `not_equal`.  We still have the `not` operator (which can be applied to booleans) and the `==` operator, which can be applied to numbers.

Now let’s try and test our new function. In the main body of your program, make four variables `a`, `b`, `c`, and `d`, such that `a` and `b` have the same value, and `c` and `d` are different from one another.

Now call your `not_equal` function, first passing it `a` and `b`, and assign its return value to a variable `not_equal_test1`. Then print out the values of `a` and `b`, as well as `not_equal_test1`.  This tests whether your function does the right thing when the two values are equal. 

Finally, test that your function works when the parameters are not equal, by passing it `c` and `d`.  Assign the return value to a variable `not_equal_test2`, and print out the values.

**Q4) Mouse Input**—`mousepoint.py`

In this exercise, we’ll experiment with a different type of user input: the mouse pointer. You can find all the documentation for the `graphics` module here: https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf.

The code in this file shows you how to retrieve the coordinates of the mouse pointer when the user clicks. Run the program and make sure you can see the mouse coordinates printed to the terminal. You should only draw the window once, but you should get new mouse coordinates every time you click the window.

Draw a blue square on the screen. Modify the code so that when the user clicks inside the square, then the square changes to green, and when the user clicks outside the square, it becomes red.

**Q5) Movie Mixup**

We would like you to practice using the command line to navigate, move, and copy files.

##### Background
Since you live in LA, you decide to look up which films would be good to check out and who the star performers were in each movie, browsing their photos so you can match names to faces.

Fortunately you aren’t starting from scratch and your LMU film and television friends have provided you with some favorite films and performers, some of whom are LMU alums! (can you tell which ones?—don't worry, that isn't part of the grade) Unfortunately, some of the files have gotten mixed up…

Not to worry! With the *command line*, you'll have them fixed in no time! 😁

##### Task
Make sure every movie in the _movies_ folder of your repository is in the correct genre folder (note: there might be multiple genres that fit, so feel free to make copies of some movies and put them into multiple genre folders) and that each movie folder has the right actor inside. Be careful or you might end up watching _E.T._ looking for Harrison Ford! If you’re unsure what items go where, feel free to use your favorite search engine or movie website to look them up!

You can start by using the GUI (i.e., you can move documents around by clicking and dragging from one folder to another), but once you’re comfortable, you should face this challenge straight from the command line.

In `movie_mixup.md`, **write down the sequence of commands** you used to organize at least one of the files. Don’t worry about efficiency—you should feel free to explore! Include commands such as `ls` or `pwd` that helped you to keep track of where you were in the command sequence or where things were located.

## How to get started
First, navigate to your repository folder by typing the following commmand—make sure to _adjust the `cd` destination_ depending on where you plan to clone the repository on your own system. For example:

    cd Desktop/cmsi1010

Once here, issue the command:

    git clone YOUR_REPOSITORY_URL
    
…where `YOUR_REPOSITORY_URL` is the URL that you were given upon setting up the assignment with GitHub Classroom. If you are asked for a password, supply the Personal Access Token that you acquired when we first started.

## Unit Testing
We have provided a `ps4_unit_tests.py` file that you can use to test your code. If you have python installed as `python3`, you can run the tests by typing the following command in the Terminal (within your repository clone folder):

    python3 ps4_unit_tests.py

## What to turn in
1. Submit the electronic copy of any files that you created/modified on your clone. In the Terminal (within your repository clone folder), type these commands. Note that you may repeat these add-commit-push sequences as frequently as you like, based on your progress:
    ```bash
    git add ps4_notes.md
    git add midpoint.py
    git add not_equal.py
    git add mousepoint.py
    git add movie_mixup.md
    git commit -m "adding files for ps4" # Ideally, personalize this!
    git push
    ```

2. Edit this _README.md_ file to include your answers to the following questions:
    * **Number of hours spent** working on this pset: 3
    * (Optional) Feel free to let us know what you liked/disliked about this pset, what you learned, etc:

## Points breakdown
| Question | Points |
| -------- | -----: |
| Q1 Reading | 10 points |
| Q2  | 20 points |
| Q3  | 20 points |
| Q4  | 25 points |
| Q5  | 25 points |
| **Total** | 100 points |

If you need to request an extension on this assignment please complete this form at least 12 hours prior to the original assignment due date. Submitting the form after this deadline might lead to the denial of your request. The course instructor will review your request, and if it's approved, your late submission will be evaluated without incurring any late penalties.
* https://mylmu.co1.qualtrics.com/jfe/form/SV_0PKIqDj8a2lSGIm



  


