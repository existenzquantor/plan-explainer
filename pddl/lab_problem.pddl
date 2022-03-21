(define (problem GoToLabProblem)
    (:domain GoToLab)
    (:objects
        office
        lab
        door
    )
    (:init 
        (in office)
        (soundProtected office)
    )
    (:goal (and (in lab)
           (soundProtected office))
    )
)