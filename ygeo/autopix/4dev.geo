base 4

gsave
newpath Corners 0 GoToPoint moveto
[8 9 1 2] {/j exch def
  Corners j get 0 get Corners j get 1 get lineto
  } forall
.3 setgray fill
newpath Corners 0 GoToPoint moveto
[2 3 4 5] {/j exch def
  Corners j get 0 get Corners j get 1 get lineto
  } forall
1 setgray fill
grestore

NewCenters 0 1 MyArc
