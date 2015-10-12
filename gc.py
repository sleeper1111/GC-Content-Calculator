# -*- coding: latin-1 -*-
import os
z=2
while z==2:
    
    id = raw_input('Please type the DNA/RNA/mRNA sequence ID:')
    file='GenBank/{0}.fasta'.format(id)

    if not os.path.exists(file):
        print "Error: Sequence not found \n"
    else:
        g,a,c,t=0,0,0,0
        with open(file,'r') as f:
            next(f)
            for line in f:
                for char in line.lower():
                    if char == 'g':
                        g+=1
                    if char == 'a':
                        a+=1
                    if char == 'c':
                        c+=1
                    if char == 't':
                        t+=1

        print "Guanine: " + str(g)
        print "Adenine: " + str(a)
        print "Cyrosine: " + str(c)
        print "Thymine: " + str(t)

        gc = (g+c+0.) / (a+t+c+g+0.)

        print "GC-Content: " + str(gc) + "\n"

raw_input("Press Enter to close")
