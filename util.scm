#lang racket

;; foldr:
;; apply f to z and each element in the list
(define (ufoldr f z list)
  (if (null? list)
      z
      (f (car list) (ufoldr f z (cdr list)))))

;; foldl:
;; apply f to each element in the list and z
(define (ufoldl f z list)
  (if (null? list)
      z
      (ufoldl f (f (car list) z) (cdr list))))