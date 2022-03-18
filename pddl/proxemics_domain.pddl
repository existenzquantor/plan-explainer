
(define (domain Proxemics)

    (:action PassCloseBy
        :parameters ()
        :precondition ()
        :effect (and (at goal) (not (violation none)))
    )

    (:action SaySorry
        :parameters ()
        :precondition ()
        :effect (violation none)
    )
    
)