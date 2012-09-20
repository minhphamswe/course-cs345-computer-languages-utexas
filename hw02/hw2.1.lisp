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

(let ((f1 (lambda (x) (+ 1 x)))   ; add one (successor)
      (f2 (lambda (x) x))         ; identity (= x + 0)
      (f3 (lambda (x y z) y)))    ; 2nd identity
  (let ((f4 (lambda (x y z) (f1 (f3 x y z)))))   ; y + 1 (successor of 2nd id)
    (letrec ((f5 (lambda (x y) (if (= 0 x)
                                   (f2 y)
                                   (f4 (- x 1) (f5 (- x 1) y) y)))))  ; (+ x y)
      (let ((f6 (lambda (x y z) z)))   ; 3rd identity
        (let ((f7 (lambda (x y z) (f5 (f3 x y z) (f6 x y z))))   ; (+ y z)
              (f8 (lambda (x) 0)))     ; 0 (= x * 0)
          (letrec ((f9 (lambda (x y) (if (= 0 x)
                                         (f8 x)
                                         (f7 x (f9 (- x 1) y) y)))))   ; (* x y)
            (let ((f10 (lambda (x y z) (f9 (f3 x y z) (f6 x y z))))    ; (* y z)
                  (f11 (lambda (x) 1)))   ; 1 (= x^0)
              (letrec ((f12 (lambda (x y) (if (= 0 x)
                                              (f11 y)
                                              (f10 x (f12 (- x 1) y) y)))))
                ; f12 is y raised to the power of x
                (f12 10 2)))))))))
  

