(define (problem CokeProblem)
    (:domain Coke)
    (:init 
        (inFridge coke)
    )
    (:goal (and (served coke)
           (inFridge coke))
    )
)