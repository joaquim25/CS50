# Sorting Algorithm Identification
## Getting Started
Provided to you are three already-compiled C programs, sort1, sort2, and sort3. Each of these programs implements a different sorting algorithm: selection sort, bubble sort, or merge sort (though not necessarily in that order!). To assess which sort implements which algorithm, run the sorts on different lists of values.

Multiple .txt files are provided to you. These files contain n lines of values, either reversed, shuffled, or sorted. For example, reversed10000.txt contains 10000 lines of numbers that are reversed from 10000, while random10000.txt contains 10000 lines of numbers that are in random order.

To run the sorts on the text files, in the terminal, run ./[program_name] [text_file.txt]. Make sure you have made use of cd to move into the sort directory!

For example, to sort reversed10000.txt with sort1, run ./sort1 reversed10000.txt.

You may find it helpful to time your sorts. To do so, run time ./[sort_file] [text_file.txt]. For example, you could run time ./sort1 reversed10000.txt to run sort1 on 10,000 reversed numbers. At the end of your terminal’s output, you can look at the real time to see how much time actually elapsed while running the program.

Background
This program was completed as part of the CS50 course offered by Harvard University. The goal of this program is to identify which sorting algorithm is used by each of the provided programs: sort1, sort2, and sort3.

Implementation Details
sort1 uses the Bubble Sort algorithm
sort2 uses the Merge Sort algorithm
sort3 uses the Selection Sort algorithm

Example Usage
To run sort1 on random50000.txt:
```
./sort1 random50000.txt
```
To time the execution of sort1 on random50000.txt:

```
time ./sort1 random50000.txt
```

### Author
Joaquim Luzia

### Acknowledgments
This program was completed as part of the CS50 course offered by Harvard University.
