(let ((H .001))
  (let ((f (lambda (x) (* x x x x))))
    (let ((d/dx
           (lambda (x) (/ ( (f (+ x H)) (f x)) H))))
      (d/dx 10))))
