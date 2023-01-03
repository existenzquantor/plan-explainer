
(define (domain Coke)

    (:predicates
        (inFridge ?o)
        (served ?o)
    )

    (:action Serve
        :parameters (?drink)
        :precondition (inFridge ?drink)
        :effect (and (not (inFridge ?drink)) (served ?drink))
    )

    (:action RefillFridge
        :parameters (?drink)
        :precondition (not (inFridge ?drink))
        :effect (inFridge ?drink)
    )
)