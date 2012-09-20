#lang racket
;;;; Student: Minh Pham
;;;; UTEID: mlp2279
;;;; CSID: minhpham
;;;; Section: TTh 5:30-6:00pm
;;;; TA: benself

;;;; Homework 2 - Problem 1:
;;;; In the answer (p254) to Problem 59 (p158) in DeLong’s book, Howard gives the
;;;; functions for primitive recursive exponentiation.
;;;; Implement these functions in lisp in a manner similar to what’s on page 11
;;;; of the PLAI1 class notes for primitive recursive addition (i.e., f5).
;;;; In the let statement for the solution show that 2^10 = 1024.
;;;; Note: By the way, you should see that f9 is multiplication.

(let ((f1 (lambda (x) (+ 1 x)))
      (f2 (lambda (x) x))
      (f3 (lambda (x y z) y))
      (f4 (lambda (x y z) (f1 (f3 x y z)))))
  (letrec ((f5 (lambda (x y))
               (if 

