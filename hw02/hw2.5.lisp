#lang racket
;;;; Student: Minh Pham
;;;; UTEID: mlp2279
;;;; CSID: minhpham
;;;; Section: TTh 5:30-6:00pm
;;;; TA: benself

;;;; Homework 2 - Problem 5:
;;;; Using just lambda, if, car, cdr, and cons, add a foldr function to the list
;;;; of functions defined in the let statement an page 32 of the PLAI1 class
;;;; notes. You can think of the foldr function as doing the following to the
;;;; list ‘(1 2 3 4 5 6) if it is applied with the “+” function and v = 0:
;;;;
;;;; v + (1 + (2 + (3 + (4 + (5 + 6)))))
;;;;
;;;; i.e., (foldr + 0 List) evaluates to 21.