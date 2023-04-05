# Overview

This work is part of the exam of *Human Computer Interaction* by Prof. *Andrew D. Bagdanov* in Laurea Magistrale in Ingegneria Informatica at University of Florence.
- Academic Year: 2021/2022
- Project Title: Conway's Game Of Life
- Student: Kevin Maggi
- CFUs: 9

> :warning: **Please attention**: as you can see this work is publicly available and anyone is obviously free of taking ideas from that. Anyway if it will be found that someone is copying the code (in the mean CTRL-C / CTRL-V) for its own project of the *same* exam, they will be reported to the Professor.

# Conway's Game Of Life

Conway's Game of Life implementation in Python following MVC pattern.

## Features

The program has the following features:

- base features:
  - **Board editor**: mouse editing;
  - **Simulation**: animation at **variable framerate** with **play/pause** controls;
  - **Next state calculation**;
- extra features:
  - **Save/Open** a board state;
  - **Variable board size**.
  - **Cell history**

## Dependencies

This program has the following dependencies:

- PyQt (tested with version 5.9.2)
- numpy (tested with version 1.21.2)
- scipy (tested with version 1.7.1)

## How to run

In order to run the program is sufficient to run the *main.py*

## Notes

All files are documented, with some indications on Model/View/Controller part in order to easily identify them.
