;; Scheme ;;

; Q2
(define (over-or-under x y)
  (cond ((= x y) 0)
  		((> x y) 1)
  		((< x y) -1) 
  	)
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

; Q3
(define (filter f lst)
  (define (filter f lst acc)
  		  (cond ((null? lst) 
  		  			acc)
  		  		 ((f (car lst)) 
  		  		 	(if (null? acc)
  		  		 		(filter f (cdr lst) 
  		  		 				  (list (car lst)))
  		  		 		)
  		  		 		(filter f (cdr lst) 
  		  		 				  (append acc (list (car lst)))
  		  		 		)		
  		  		 	)
  		  		 (else 
  		  		 	(filter f (cdr lst) acc))
  		  ))
  (filter f lst ())
) 


;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

; Q4
(define (make-adder num)
  (lambda (x) (+ x num))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13