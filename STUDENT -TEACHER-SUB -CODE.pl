takes(abhi, csa1704).
takes(bhargav, csa0753).
takes(smitha,csa1704).
takes(mahesh, csa0753).
classmates(X, Y) :- takes(X, Z), takes(Y, Z).
