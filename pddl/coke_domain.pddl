
(define (domain Coke)

    (:action Serve
        :parameters (?drink - drink)
        :precondition (inFridge ?drink)
        :effect (and (not (inFridge ?drink)) (served ?drink))
    )

    (:action RefillFridge
        :parameters (?drink - drink)
        :precondition (not (inFridge ?drink))
        :effect (and (inFridge ?drink))
    )
)