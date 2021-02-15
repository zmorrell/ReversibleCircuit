import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

class Circuit:
    def __init__(self,n):
        self.n = n
        self.wires = [Wire(k) for k in range(n)]
        self.gates = []
        
    def addGate(self,g):
        self.gates.append(g)
        for bit in g.bits:
            self.wires[bit].addGate(g)
    
    def __str__(self):
        string = ""
        for gate in self.gates:
            string = string + str(gate)
            
        return string
        
    def hamiltonian(self):
        ham = None
        for gate in self.gates:
            if ham == None:
                ham = gate.hamiltonian(self.n)
            else:
                ham = np.dot(gate.hamiltonian(self.n) * ham)
    
    
    def printWires(self):
        for wire in self.wires:
            print(wire)
        
class Wire:
    def __init__(self,k):
        self.k = k
        self.gates = []
    
    def addGate(self,g):
        self.gates.append(g)
    
    def removeLastGate(self):
        return self.gates.pop()
    
    def __str__(self):
        string = f"[{self.k}]:"
        for gate in self.gates:
            string += str(gate)
        return string

class Gate:
    gatecount = 0

    def __init__(self,matrix,bits):
        assert(matrix.shape == (2**len(bits),2**len(bits)))
        self.matrix = matrix
        self.bits = bits
        self.id = Gate.gatecount
        Gate.gatecount += 1
        
    def __str__(self):
        return f"-g{self.id}-"
    
    def hamiltonian(self,n):
        #first construct hamiltonian operating on first len(bits) qubits, then swap
        ham = mat
        for i in range(1 - len(self.bits)):
            ham = np.kron([[1,0],[0,1]],mat)
