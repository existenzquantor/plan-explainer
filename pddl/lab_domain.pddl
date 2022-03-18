
(define (domain goToLab)

    (:action askHumanToOpenDoor
        :parameters ()
        :precondition ()
        :effect (and (open door) (not (soundProtected office)))
    )

    (:action askHumanToCloseDoor
        :parameters ()
        :precondition ()
        :effect (and (not (open door)) (soundProtected office))
    )

    (:action moveIntoLab
        :parameters ()
        :precondition (and (open door) (in office))
        :effect (and (not (in office)) (in lab))
    )
)