#lang racket
;;;; Student: Minh Pham
;;;; UTEID: mlp2279
;;;; CSID: minhpham
;;;; Section: TTh 5:30-6:00pm
;;;; TA: benself

;;;; Homework 2 - Problem 2:
;;;; On pages 158 and 159 in DeLong’s book, Howard gives the functions for
;;;; primitive recursive equality. Implement these functions in lisp in a
;;;; manner similar to problem 1 above. In the let statement for the solutions
;;;; build a list that shows that 11 = 11, 11 != 12, and 12 != 11. i.e., the
;;;; let should return '(0 1 1).