(define (domain GoToLab)
    (:action AskHumanToOpenDoor
        :parameters ()
        :precondition ()
        :effect (and (open door) (not (soundProtected office)))
    )

    (:action AskHumanToCloseDoor
        :parameters ()
        :precondition ()
        :effect (and (not (open door)) (soundProtected office))
    )

    (:action Move
        :parameters (?roomA ?roomB)
        :precondition (and (open door) (in ?roomA))
        :effect (and (not (in ?roomA)) (in ?roomB))
    )
)