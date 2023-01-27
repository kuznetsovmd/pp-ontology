

def make(onto, entity, evidence="Not defined", parents=(), children=()):

    cls_ = getattr(onto, entity)
    evidence_ = getattr(onto, "Evidence")
    individual = cls_()

    e = evidence_()
    e.evidenceContent = evidence
    
    individual.hasEvidence.append(e)

    for property, v in parents:
        getattr(individual, property).append(v)

    for property, v in children:
        getattr(individual, property).append(v)

    return individual
    