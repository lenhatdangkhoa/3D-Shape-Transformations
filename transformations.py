def translate(Tx, Ty, Tz):
    return [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [Tx,Ty,Tz,1]]