
(define (domain Proxemics)

    (:predicates
        (at ?place)
        (noViolation)
    )

    (:action PassCloseBy
        :parameters ()
        :precondition ()
        :effect (and (at goal) (not (noViolation)))
    )

    (:action SaySorry
        :parameters ()
        :precondition ()
        :effect (noViolation)
    )

)