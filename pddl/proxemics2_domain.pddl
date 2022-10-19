
(define (domain Proxemics)

    (:predicates
        (at ?place)
        (violation)
    )

    (:action PassCloseBy
        :parameters ()
        :precondition ()
        :effect (and (at goal) (violation))
    )

    (:action SaySorry
        :parameters ()
        :precondition ()
        :effect (not (violation))
    )

)