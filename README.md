## How did the students do?

****
**A short explanation:**

I had to work for the past two weeks. So, I had to begin this task later. It took me a couple of hours to write the main.py and utils.py.
But the unit test (_test_utils.py_) took me longer than I thought it would. Because I am new to unit testing, and it was the first time I did unit testing for pandas (Honestly, I don't think I did a good job).
I have tried the given examples (Example1 and Example2), but I created two other sets of example files. All were working fine.

Although the task is simple, there are some improvements that can be done. For example, the _check_weights()_ method, can be done inside the calculations.
Right nwo, a part of the calculation is redundant and have happened earlier.

Another thing that should be done is benchmarking with a huge workload. I am not sure how big of a workload can a school grading system be, but faster is always better.
****
**Why pandas?**

I benefited from the vectorized calculation of Pandas to make things faster than loops. Of course, I had the option to use Numpy as well.
However, Pandas seemed a better choice as it had SQL-like functionalities.

****
**How to Run?**

- First, you need to have a pair of running shoes :D

- Then, you need to open the terminal and enter the following command:

`python [path to main.py] [path to courses.csv] [path to students.csv] [path to tests.csv] [path to marks.csv] [path to output.json]
`

_[path to output.json]_ is where you like your output to be saved.

**Requirements:**

The only packages you need for running the program are _sys_, _pandas_, and _json_.
****
