

def distance(a, b):
    if len(a) == len(b):
        x = 0
        for i in range(len(a)):
            # voir si les deux elements sont egaux
            if (a[i] != b[i]):
                x+=1
        # need to return x outside of the loop, or it will stop the loop the first time the condition is met
        return x
