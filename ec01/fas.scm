#lang racket

;; Turn a string in successor notation into a number
(define (num s)
  (if (equal? s "0")
      0
      (+ (num (substring s 0 (- (string-length s) 1))) 1)))

;; Turn a number into a string in successor notation
(define (sym n)
  (if (= n 0)
      "0"
      (string-append (sym (- n 1)) "'")))

;; Predecessor function
(define (pd sx)
  (sym (- (num sx) 1)))

;; Successor function
(define (sc lst)
  (sym (+ (num (third lst)) 1)))

;; Helper function: print add result
(define (addn x y)
  (add (sym x) (sym y)))

;; Primitive-recursive addition in successor notation
(define (add sx sy)
  (let ((expr (if (equal? sy "0")
                  sx
                  `(sc (add ,sx ,(pd sy))))))
    (let ((print `(,sx ,sy ,expr)))
      (let ((result `(,sx ,sy ,(eval expr))))
        (if (equal? print result)
            (let ()
              (display "\t")
              (display result)
              (display "\n"))
            (let ()
              (display "\t")
              (display print)
              (display "\n\t")
              (display result)
              (display "\n")))
        result))))

(define (mull x y)
  (mul (sym x) (sym y)))

;; Primitive-recursive multiplication
(define (mul sx sy)
  (let ((expr (if (equal? sy "0")
                  "0"
                  `(add (mul ,sx ,(pd sy)) ,sx))))
    (let ((eexpr (if (equal? sy "0")
                     "0"
                     `(third (add ,(third (mul sx (pd sy))) ,sx)))))
      (let ((print `(,sx ,sy ,expr)))
        (let ((result `(,sx ,sy ,(eval eexpr))))
          (if (equal? print result)
              (let ()
                (display result)
                (display "\n"))
              (let ()
                (display print)
                (display "\n")
                (display result)
                (display "\n")))
          result)))))