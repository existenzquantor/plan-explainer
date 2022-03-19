(define (problem ProxemicsProblem)
    (:domain Proxemics)
    (:init 
        (noViolation)
    )
    (:goal (and (at goal)
           (noViolation))
    )
)