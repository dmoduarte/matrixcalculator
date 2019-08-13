import json
import validator
from matrix import Matrix

#Matrix addition: adds m1 with m2 bot with dimension = mxn, resulting in matrix m3 with dimension = mxn
def add(m1, m2):
	#Alghorithm:
	#ensure dim(m1) == dim(m2) i,e if m1 is of size mXn then m2 should be mXn as well
	#then m3 = m1 + m2 results from m3ij = m1ij + m2ij where i and j are both coordinates from each matrix:
		#create a new Matrix m3
		#iterate over each element ij of m1
		 	#m3ij = m1ij + m2ij
	validator.checkMatrixValidity(m1);
	validator.checkMatrixValidity(m2);
	validator.checkEqualSize(m1, m2);

	m3 = Matrix({});

	for i, iCols in m1.items():
		for j, m1_ij in iCols.items():
			m3.setValueAt(i, j, m1_ij + m2.getValueAt(i, j))

	return m3;
#Scalar multiplication: multiplies a matrix m1, with dimension = mxn, with a scalar k, resulting in a matrix m2 with dimension = mxn
def multiplyWithScalar(m1, k):
	#Alghorithm:
	#iterate over each element ij of m1
		 	#m2ij = m1ij * k
	validator.checkMatrixValidity(m1);
		 	
	m2 = Matrix({});

	for i, iCols in m1.items():
		for j, m1_ij in iCols.items(): 	
			m2.setValueAt(i, j, m1_ij * k)

	return m2;

m1 = Matrix({'1':{'1':1,'2':3}, '2':{'1':3, '2':4}});
m2 = Matrix({'1':{'1':2,'2':3}, '2':{'1':4, '2':4}});

print(json.dumps(vars(m1) , indent=4))
print(json.dumps(vars(m2) , indent=4))
print(json.dumps(vars(add(m1, m2)) , indent=4))
print(json.dumps(vars(multiplyWithScalar(add(m1, m2), 2)) , indent=4))