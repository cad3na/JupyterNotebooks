MODULE MainModule
	PERS tooldata tool0 := [ TRUE, [[0, 0, 0], [1, 0, 0, 0]], [0.001, [0, 0, 0.001], [1, 0, 0, 0], 0, 0, 0]];
	CONST robtarget p01 := [ [515.0, 0.0, 712.0], [1, 0, 0, 0], [0, 0, 0, 0], [ 9E9, 9E9, 9E9, 9E9, 9E9, 9E9] ];
	CONST robtarget p02 := [ [515.0, 0.0, 812.0], [1, 0, 0, 0], [0, 0, 0, 0], [ 9E9, 9E9, 9E9, 9E9, 9E9, 9E9] ];
	CONST robtarget p03 := [ [515.0, 100.0, 812.0], [1, 0, 0, 0], [0, 0, 0, 0], [ 9E9, 9E9, 9E9, 9E9, 9E9, 9E9] ];
	CONST robtarget p04 := [ [515.0, 100.0, 712.0], [1, 0, 0, 0], [0, 0, 0, 0], [ 9E9, 9E9, 9E9, 9E9, 9E9, 9E9] ];
	CONST robtarget p05 := [ [515.0, 0.0, 712.0], [1, 0, 0, 0], [0, 0, 0, 0], [ 9E9, 9E9, 9E9, 9E9, 9E9, 9E9] ];
	PROC main()
		MoveL p01, v200, z20, tool0;
		MoveL p02, v200, z20, tool0;
		MoveL p03, v200, z20, tool0;
		MoveL p04, v200, z20, tool0;
		MoveL p05, v200, z20, tool0;
	ENDPROC
ENDMODULE
