(define (problem CokeProblem)
    (:domain Coke)
    (:objects
        coke - drink
    )
    (:init 
        (inFridge coke)
    )
    (:goal (and (served coke)
           (inFridge coke))
    )
)