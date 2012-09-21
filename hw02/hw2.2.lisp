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

(letrec (; (pred x) returns 0 if x == 0, the predecessor of x if x > 0
         (pred (lambda (x) (if (= x 0)
                               0
                               (- x 1))))
         ; (dot-minus x y) returns 0 if x <= y, x-y if x > y
         (dot-minus (lambda (x y) (if (= y 0)
                                    x
                                    (pred (dot-minus x (pred y))))))
         ; (abs-minus x y) returns the absolute value of x-y
         (abs-minus (lambda (x y) (+ (dot-minus x y) (dot-minus y x))))
         ; (signum x) returns 0 if x == 0, 1 otherwise
         (signum (lambda (x) (if (= x 0) 0 1))))
  (let ((equal? (lambda (x y) (if (= (signum (abs-minus x y)) 0) 0 1))))
    (cons (equal? 11 11)
          (cons (equal? 11 12)
                (cons (equal? 12 11) '())))))
         
         
                 
         
  
              

