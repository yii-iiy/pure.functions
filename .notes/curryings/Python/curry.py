fixedpoint = lambda f: (lambda x: x(x)) (lambda y: f(lambda *args: y (y) (*args))) ;

curry = lambda func: fixedpoint (lambda curried: 
	lambda *args: (lambda x: curried (* (args + (x,)))) if 
	(len (args) != func.__code__.co_argcount) else 
	func (*args)) ;

