#lang racket
;;;; Student: Minh Pham
;;;; UTEID: mlp2279
;;;; CSID: minhpham
;;;; Section: TTh 5:30-6:00pm
;;;; TA: benself

;;;; Homework 2 - Extra Credit:
;;;; Implement the map function in terms of foldr and show that:
;;;; (map (lambda (x) (+ x 5)) List))
;;;; evaluates to '(6 7 8 9 10 11) when List is '(1 2 3 4 5 6).

;;; foldr implementation comes from Problem 5
(letrec ((foldr 
          (lambda (op val lst)
            (letrec ((foldr-rec
                      (lambda (op lst)
                        (if (null? (cdr lst))
                            (car lst)
                            (op (car lst) (foldr-rec op (cdr lst)))))))
              (op val (foldr-rec op lst))))))
  (letrec ((map (lambda (fn lst)
                  (if (null? (cdr lst))
                      (foldr cons (fn (car lst)) '(()))
                      (cons (fn (car lst)) (map fn (cdr lst)))))))
    (map (lambda (x) (+ x 5)) '(1 2 3 4 5 6))))
