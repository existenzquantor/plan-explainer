
(define (domain Proxemics)

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