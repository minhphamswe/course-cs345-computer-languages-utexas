#lang racket
;;;; Student: Minh Pham
;;;; UTEID: mlp2279
;;;; CSID: minhpham
;;;; Section: TTh 5:30-6:00pm
;;;; TA: benself

;;;; Homework 4 - Problem 1:
;;;; Write the differentiation function found in the PLAI book in
;;;; Section 6.5.2 in scheme using lets and lambdas instead of defines.
;;;; It should have 3 lets, one for H, one for the function being
;;;; differentiated and one for d/dx.
;;;; Rewrite this expression as just function applications as shown in
;;;; PLAI 3 & HLL 3, page 3. Put both of these expressions in the
;;;; HW4.csm file.

;;;; PLAI implementation of numeric differentiation
;; (define H 0.0001)
;;
;; (define (d/dx f )
;;     (lambda (x)
;;       (/ (- (f (+ x H)) (f x))
;;          H)))

;; Implementation using lets
(let ((H 0.0001))
  (let ((func (lambda (x) (* x x))))
    (let ((d/dx (lambda (f)
                  (lambda (x)
                    (/ (- (f (+ x H)) (f x)) H)))))
      ((d/dx func) 7))))

;; Implementation using lambda
;; Conversion: (let ((A B)) C) <=> ((lambda (A) C) B)
(((lambda (H)
   ((lambda (func)
      ((lambda (d/dx)
         (d/dx func))
       (lambda (f)  ; bind d/dx
         (lambda (x)
           (/ (- (f (+ x H)) (f x)) H)))))
    (lambda (x)     ; bind func
      (* x x))))
 0.0001)            ; bind H
 7)
 