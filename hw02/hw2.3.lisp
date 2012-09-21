#lang racket
;;;; Student: Minh Pham
;;;; UTEID: mlp2279
;;;; CSID: minhpham
;;;; Section: TTh 5:30-6:00pm
;;;; TA: benself

;;;; Homework 2 - Problem 3:
;;;; In a manner similar to problem 2, implement the functions for primitive
;;;; recursive “less than” and in the let statement for the solution build a
;;;; list that shows that 11 < 12, 11 !< 11, and 12 !< 11. i.e., the let should
;;;; return '(0 1 1).
;;;; Hint – see DeLong problem number 60.

(letrec (; (pred x) returns 0 if x = 0, x-1 if x > 0
         (pred (lambda (x) (if (= x 0) 0 (- x 1))))
         ; (dot-minus x y) returns 0 if x <= y, x-y if x > y
         (dot-minus (lambda (x y) (if (= 0 y)
                                      x
                                      (pred (dot-minus x (pred y))))))
         ; (signum x) returns 0 if x = 0, 1 if x > 0
         (signum (lambda (x) (if (= x 0) 0 1))))
  (let ((lt (lambda (x y) (if (= (signum (dot-minus y x)) 1) 0 1))))
    (cons (lt 11 12)
          (cons (lt 11 11)
                (cons (lt 12 11) '())))))
         