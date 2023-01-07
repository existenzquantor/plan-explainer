(define (problem ProxemicsProblem)
    (:domain Proxemics)

    (:objects goal-destination)
    (:init 
        (noViolation)
    )
    (:goal (and (at goal)
           (noViolation))
    )
)