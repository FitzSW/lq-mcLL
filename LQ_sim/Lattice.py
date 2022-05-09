import numpy as np


class Lattice:

    def __init__(self, size):

        self.x = np.empty(size, size, size)
        self.y = np.empty(size, size, size)
        self.z = np.empty(size, size, size)

        self.n = size



    def initialize(self, method):

        N = self.n
        if method == "random" or "Random":

            #initialize
            self.x = rng.standard_normal(size=(N, N, N))
            self.y = rng.standard_normal(size=(N, N, N))
            self.z = rng.standard_normal(size=(N, N, N))

            #normalize

            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        vec = np.array([self.x[i, j, k], self.y[i, j, k], self.z[i, j, k]])
                        norm = np.linalg.norm(vec)
                        self.x[i, j, k] /= norm
                        self.y[i, j, k] /= norm
                        self.z[i, j, k] /= norm

        if method == "uniform" or "Uniform":

            #direct in the z direction

            self.x = np.zeros((N,N,N))
            self.y = np.zeros((N,N,N))
            self.z = np.ones((N,N,N))


    def shift(self, pos, rng):
        '''Takes a lattice position and randomly reorients it in the unit sphere'''

        #generate random positions
        x_shift = rng.standard_normal()
        y_shift = rng.standard_normal()
        z_shift = rng.standard_normal()

        #normalize
        vec = np.array([x_shift, y_shift, z_shift])
        normal = np.linalg.norm(vec)

        x_shift /= normal
        y_shift /= normal
        z_shift /= normal

        #shift lattice vector
        self.x[pos] = x_shift
        self.y[pos] = y_shift
        self.z[pos] = z_shift


    def order(self):

        N = self.n

        Q = 0

        for i in range(N):
            for j in range(N):
                for k in range(N):

                    vec = np.array([self.x[i,j,k], self.y[i,j,k], self.z[i,j,k]])

                    #use Q tensor

                    Q += ((vec*(vec.T)) - ((1/3)*np.eye(3)))

        #average
        Q /= (N ** 3)

        #diagonalize
        eigenvalues = np.linalg.eigh(Q)[0]  # should be an array of REAL eigenvalues

        P2 = (3 / 2) * max(eigenvalues)

        return P2





