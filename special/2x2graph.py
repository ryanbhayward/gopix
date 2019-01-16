import math
#  create eps with all 57 legal 2x2 Go positions well-placed 
#    for transition graph (adjacent iff legal move from one to other)
#  using cyclic board indices   1  2 
#                               0  3
#  RBH 2019

nodes = [
'....', #0
'x...', '.x..', '..x.', '...x', 'o...', '.o..', '..o.', '...o', # 1 .. 8
'xx..', '.xx.', '..xx', 'x..x', 'x.x.', '.x.x',                 # 9 .. 16
'oo..', '.oo.', '..oo', 'o..o', 'o.o.', '.o.o',                 #17 .. 20
'xo..', '.xo.', '..xo', 'o..x',                                 #21 .. 24
'ox..', '.ox.', '..ox', 'x..o',                                 #25 .. 28
'x.o.', '.x.o', 'o.x.', '.o.x',                                 #29 .. 32
'xxx.', '.xxx', 'x.xx', 'xxx.', 'ooo.', '.ooo', 'o.oo', 'oo.o', #33 .. 40
'xxo.', '.xxo', 'o.xx', 'xo.x', 'xx.o', 'oxx.', '.oxx', 'x.ox', #41 .. 48
'oox.', '.oox', 'x.oo', 'ox.o', 'oo.x', 'xoo.', '.xoo', 'o.xo'  #49 .. 56
]

def emit(x,y,L,j):
  outstr = str(x) + ' ' + str(y) + ' Board '
  if L[j][0]=='x': outstr += '1 1 B '
  if L[j][0]=='o': outstr += '1 1 W '
  if L[j][1]=='x': outstr += '1 2 B '
  if L[j][1]=='o': outstr += '1 2 W '
  if L[j][2]=='x': outstr += '2 2 B '
  if L[j][2]=='o': outstr += '2 2 W '
  if L[j][3]=='x': outstr += '2 1 B '
  if L[j][3]=='o': outstr += '2 1 W '
  print(outstr)

def printHead():
  print('%!PS-Adobe-3.0')
  print('%%BoundingBox: -160 -160 230 230')
  print('%%Pages: 0')
  print('%%EndComments')

def printBody():
  f = open('2x2nodes.epsbody','r')
  for line in f: print(line, end = '')

def printTail():
  f = open('2x2nodes.epsbody','r')
  for line in f: print(line)

def printTail():
  def do_ring(ring, radius):
    for j in range(len(ring)):
      emit(str.format('{0:.3f}',radius*math.sin(math.pi*2*j/len(ring))), 
           str.format('{0:.3f}',radius*math.cos(math.pi*2*j/len(ring))), 
         nodes, 
         ring[j])

  ring1 = [ 1, 29, 7, 21,  2, 30,  8, 23,  3, 31,  5, 24,  4, 32,  6, 21]
  ring2 = [18, 15, 9, 28, 19, 21, 10, 25, 20, 16, 11, 26, 17, 20, 12, 27]
  print('gsave')
  emit( 0, 0, nodes,0)
  do_ring(ring1, 3.0)
  do_ring(ring2, 5.0)
  #for j in range(len(ring1)):
  #  emit(str.format('{0:.3f}',3.0*math.sin(math.pi*2*j/len(ring1))), 
  #       str.format('{0:.3f}',3.0*math.cos(math.pi*2*j/len(ring1))), 
  #       nodes, 
  #       ring1[j])
  #for j in range(1,len(nodes)):
  #  emit((j+7)%8, (j+7)//8, nodes, j)
  print('grestore')
  print('showpage')

printHead()
printBody()
printTail()

