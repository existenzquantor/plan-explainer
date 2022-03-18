
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

    (:action MoveIntoLab
        :parameters ()
        :precondition (and (open door) (in office))
        :effect (and (not (in office)) (in lab))
    )
)