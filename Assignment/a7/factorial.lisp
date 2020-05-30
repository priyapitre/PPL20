;;;;This is a program which consists of 2 functions to find factorial of number.
;;;;First of them uses recurrsion and second is simple iteration.

(defun factrec (n)
  (if (= n 0)
    1
    (* n (factrec(- n 1)))))

(defun factdi (n)
  (defvar i nil)
  (defvar m 1)
  (loop for i from 1 to n
	do(setq m (* m i)))
  m)

(format t "Enter number to find factorial ~%")
(defvar k (read))
(format t "Factorial using recurrsion is ~d ~%" (factrec k))
(defvar p (factdi k))
(format t "Factorial using looping is ~d ~%" p)
