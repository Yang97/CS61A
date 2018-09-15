;; Extra Scheme Questions ;;


; Q5
(define lst
  'YOUR-CODE-HERE
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (filter (lambda (x) (not (= x item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (cond ((or (= a 0)
             (= b 0)) (max a b))
        ((= (remainder (max a b) (min a b)) 0)
        	(min a b))
        (else (gcd (min a b)
      	   		(remainder (max a b) (min a b))))
  )
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  'YOUR-CODE-HERE
)

; Q10
(define (substitute s old new)
  (define (flatten nest_pair nest_deepth)
    (if (pair? (car nest_pair))
        (flatten (car nest_pair) (+ nest_deepth 1))
    	(cons (car nest_pair) (+ nest_deepth 1))))
  (define (nest acc deepth)
    (if (= deepth 0)
        acc
        (nest (list acc) (- deepth 1))))
  (define (reverse lst acc)
    (cond ((null? lst) acc)
          (else (reverse (cdr lst) (append acc (list (car lst)))))))
  (define (reverse lst)
    (if (null? lst)
        lst
        (reverse (cdr lst) (list (car lst)))))
  (define (deal-with-nest-pair lst old new)
    (if (eq? (car (flatten lst 0)) old)
        (nest new (cdr (flatten lst 0)))
        (nest (car (flatten lst 0)) (cdr (flatten lst 0)))))
  (define (substitute lst old new acc)
    (cond ((null? lst) (reverse acc))
          ((pair? (car lst))
           (if (> (length (car lst)) 1)
               (substitute (cdr lst) old new (substitute (car lst) old new ()))
               (substitute (cdr lst) old new (list acc (deal-with-nest-pair (car lst) old new))))
          ((eq? (car lst) old) (substitute (cdr lst) old new (cons new acc)))
          (else (substitute (cdr lst) old new acc)))))
  (substitute s old new ())
)


; Q11
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)