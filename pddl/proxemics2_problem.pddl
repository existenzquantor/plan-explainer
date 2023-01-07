(define (problem ProxemicsProblem)
    (:domain Proxemics)
    (:objects goal-destination)
    (:goal (and 
            (at goal)
            (not (violation))
           )
    )
)