
(define (domain Coke)

    (:action ServeCoke
        :parameters ()
        :precondition (inFridge coke)
        :effect (and (not (inFridge coke)) (served coke))
    )

    (:action RefillFridge
        :parameters ()
        :precondition (not (inFridge coke))
        :effect (and (inFridge coke))
    )
)