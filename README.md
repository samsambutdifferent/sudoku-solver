# Sudoku Solver

## Overview

A program which solves a Sudoku puzzle.

## The Problem

Produce an algorithm which will complete a Sudoku. Sudokus are simple mathematical puzzles, the player is asked to fill in the blank squares with a number (from 1-9) following the rules of Sudoku:

<figure class="image">
    1) the number is unique along the row <br/>
    2) the number is unique along the column <br/>
    3) the number is unique in the 9x9 sub square <br/>
  <figcaption><i> 
    figure 1: the rules of sudoku
  </figcaption></i>
</figure>

<figure class="image">
  <img src="solved_blank_sudoku.png"
     alt="sudoku blank"
     style="" /> 
  <figcaption><i> 
    figure 2: a sudoku before and after completion <br/>
    Cburnett, Wikipedia 2017, Sudoku, viewed 18 May 2021, <https://en.wikipedia.org/wiki/Sudoku>. 
  </figcaption></i>
</figure>

## Algorithm

On a blank Sudoku there are 9<sup>81</sup> possible numbers for all of the squares as each could have any of 9 values, whilst most puzzles start with some of the squares filled in this is still far more than any brute force method could handle in a reasonable time frame. Therefore the algorithm will be implemented recursively using backtracking search. This applies a combination of a depth-first search and constraint propagation, which will dramatically reduce the number of values needing to be checked.


### Algorithm Overview

The high level view of the implemented algorithm, the following steps are demonstrated visually in <i>figure 3</i>

1) The algorithm finds an empty square and applies the first valid number (as per <i>figure 1</i> the rules of sudoku)
2) It moves on to the next empty spot and repeats
3) Process continues until it finds a spot which it is unable to place a number - in the case of <i>figure 3</i> this is 6 - 6 cannot be placed as it is already in the sub square
4) Backtracks through each of the previous steps trying each of the subsequent higher number - in the case of <i>figure 3</i> it will try 9 and then 8 before backtracking again until it places the 6 in the previous sub square 
5) Continues the process  - in <i>figure 3</i> the first line has been completed successfully and is in line with <i>figure 1</i> the rules of sudoku

<figure class="image">
  <img src="sudoku run through.png"
     alt="sudoku blank"
     style="" /> 
  <figcaption><i> 
    figure 3: algorithm overview<br/>
  </figcaption></i>
</figure>


## Further Optimisation

In <i>figure 3</i> the next empty space is chosen from left to right and top to bottom.

To achieve greater speed logic is applied to the selection of the next empty space. Rather than randomly selecting the next space, the space which has the lowest number of possible values is chosen this will reduce the number of times that the algorithm has to backtrack as it is more likely to be correct.

For instance a space with:

1 possible - has a 100% chance of being correct

2 possibilities - has a 50% chance of being correct etc.

By selecting spaces with higher probability of being correct the algorithm reduces the need to backtrack. For each recursion of the main function the possibilities are recalculated and lowered as more of the sudoku is filled in there are less possible options for the empty spaces. 

