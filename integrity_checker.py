def checkEqualSize(m1, m2):
	if not areEqualSize(m1, m2):
		raise ValueError("m1 and m2 do not have the same dimension");

#checks if m1 and m2 have the same dimension
def areEqualSize(m1, m2):
	m1Dim = m1.dim();
	m2Dim = m2.dim();
	return m1Dim['m'] == m2Dim['m'] and m1Dim['n'] == m2Dim['n'];