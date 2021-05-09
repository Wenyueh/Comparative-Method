# Three Iterative Methods on Linear Systems

Jacobi Method

Gauss-Seidel Method

Successive over Relaxation Method

# Eight Types of Matrices

random matrix

band diagonal matrix

diagonal matrix 

symmetric definite

symmetric indefinite

diagonal dominant matrix

z-matrix

q-matrix

# Code
To generate convergence graphs of all methods with matrix type "random" with size 100 for example:

python all_methods.py --mtype random --size 100

The graph will be save as random_100.png

# Next
The relevant matrices and their convergence graphs are included in the convergence_graphs folder. All .mtx files are from Matrix Market https://math.nist.gov/MatrixMarket/searchtool.html

The all_methods.py file is the main file to run that takes in the arguments of the matrix type and size as well as running the 3 iterative methods on it. It also generates the appropriate convergence graphs for them.

The check_domimant.py file checks if the target matrix is diagonally dominant.

The generate_matrix.py file matches the input from all_methods.py to an appropriate preexisting .mtx matrix or generates a new random matrix based on the specifications if none exists.

# Required Python Library Imports
NumPy for Python
https://numpy.org/doc/stable/user/absolute_beginners.html

Matplotlib.pyplot for Python
https://matplotlib.org/stable/users/installing.html

Scipy.io for Python
https://www.scipy.org/install.html#pip-install