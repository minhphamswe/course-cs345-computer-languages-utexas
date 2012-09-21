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

;;; Function is implemented recursively
;;; Could also be done tail-recursively, but done this way for variety
;;; Since we are not emphasizing efficiency in this homework.
(letrec ((foldr 
          (lambda (op val lst)
            (letrec ((foldr-rec
                      (lambda (op lst)
                        (if (null? (cdr lst))
                            (car lst)
                            (op (car lst) (foldr-rec op (cdr lst)))))))
              (op val (foldr-rec op lst))))))
  (foldr + 1 '(1 2 3 4 5 6))
  ;(foldr cons 0 '(1 2 3 4 5 6))
  )
