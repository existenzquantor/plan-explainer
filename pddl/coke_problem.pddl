(define (problem CokeProblem)
    (:domain Coke)
    (:objects
        coke
    )
    (:init 
        (inFridge coke)
    )
    (:goal (and (served coke)
           (inFridge coke))
    )
)