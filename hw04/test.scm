(let ((H .001))
  (let ((f (lambda (x) (* x x x x))))
    (let ((d/dx
           (lambda (x) (/ ( (f (+ x H)) (f x)) H))))
      (d/dx 10))))

(let ((H .001)) H)

(let ((H .001)) (+ H 1))

(let ((x 1)) (let ((y 2)) (+ x y)))

(let ((H .001)) (let ((f (lambda (x) (* x x x x)))) (f H)))
