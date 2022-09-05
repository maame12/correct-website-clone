import random 
from os import urandom

import random
import math
import timeit
import pandas as pd
from matplotlib import pyplot as plt
import seaborn
import matplotlib.lines as lines



secret_key = random.randint(4567894589246385, 9999018934567935)
#secret_key = random.randbytes(16)

class ShamirSecret:
    """
    Encode and share a secret based on Shamir's Secret Sharing algorithm.

    Attributes
    ----------
    secret: int
        Stores the original secret
    shares: int
        Number of shares to be generated
    threshold: int
        Minimum number of shares required to reconstruct the secret
    generated_shares: list
        Contains pairwise tuples of shares generated from the secret

    """

    def __init__(self, **kwargs) -> None:
        """
        Construct a ShamirSecret object.

        Parameters
        ----------
        kwargs: dict
            Contains the mandatory keyword arguments:
            secret: int
                The secret to be shared
            shares: int
                Number of shares to be generated
            threshold: int
                Minimum number of shares required to reconstruct the secret

        Example
        -------
        >>> s = ShamirSecret(secret=1234, shares=4, threshold=2)

        """
        self.secret = secret_key
        self.shares = kwargs.get('shares')
        self.threshold = kwargs.get('threshold')
        self.generated_shares = list()

    def __str__(self) -> str:
        return f'ShamirSecret(secret={self.secret}, shares={self.shares}, threshold={self.threshold})'

    def generate_shares(self):
        """
        Generate the specified number of shares for the secret.

        Example
        -------
        >>> s.generate_shares()
        >>> print(*s.get_shares(), sep='\\n')
        (1, 1310)
        (2, 1386)
        (3, 1462)
        (4, 1538)
        ...

        """
        # random coefficients of the polynomial
        coefficients = tuple(random.randrange(1, self.secret// 2) for _ in range(self.threshold - 1))

        def construct_poly(s, k, a, x):
            # f(x) = a0 + a1 * x + a2 * (x ^ 2) + .... + a(k-1) * (x ^ k-1)
            # constructing the polynomial for each value of x,
            # with s as a0 and other coefficients in tuple a
            f = s
            for i, pw in zip(a, tuple(range(1, k))):
                f += i * x ** pw

            return f

        for x in range(1, self.shares + 1):
            fx = construct_poly(self.secret, self.threshold, coefficients, x)
            self.generated_shares.append((x, fx))

    def get_shares(self):
        """Returns the generated shares."""
        return self.generated_shares

    def random_shares(self):
        """
        Select random threshold number of shares from the list of generated_shares.

        Returns
        -------
        : tuple
            Contains the pairwise tuples of shares.

        Example
        -------
        >>> s.random_shares()
        ((2, 1734), (4, 2234))

        """
        return tuple(random.sample(self.generated_shares, k=self.threshold))

    def reconstruct(self, rand_shares) -> int:
        """
        Reconstruct the secret with random shares and a prime.

        Parameters
        ----------
        rand_shares: tuple
            Containing pairwise tuples of random shares.

        Returns
        -------
        sigma: int
            The reconstructed secret

        Example
        -------
        >>> s.reconstruct(s.random_shares())
        1234

        """
        l = len(rand_shares)  # length: number of random shares
        x_s = tuple(map(lambda x: x[0], rand_shares))  # x values of shares
        y_s = tuple(map(lambda x: x[1], rand_shares))  # y values of shares

        def PI(vars):  # product of inputs (PI)
            acc = 1
            for v in vars:
                acc *= v

            return acc

        nume = tuple()
        deno = tuple()
        for j in range(l):
            nume += (PI(x_s[m] for m in range(l) if m != j), )
            deno += (PI(x_s[m] - x_s[j] for m in range(l) if m != j), )

        sigma = round(sum(y_s[i] * nume[i] / deno[i] for i in range(l)))

        return sigma
    
    
#secret=9535243680040594279


if __name__ == '__main__':
    s = ShamirSecret(secret_key=random.randint(4567894589246385, 9999018934567935), shares=2, threshold=2)
    print(s)
    s.generate_shares()
    print('\nShares:', *s.get_shares(), sep='\n')
    print('\nReconstructed Secret:', s.reconstruct(s.random_shares()))
    print(timeit.repeat('s.generate_shares()', repeat=7, number=20 , globals=globals()))
    y = (timeit.repeat('s.get_shares()',repeat=7, number=20 , globals=globals()))
    
   
plt.style.use('seaborn')   
x = [0, 1, 2, 3, 4, 5, 6]
plt.plot(x, y, 'ro-')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
seaborn.despine()
plt.show()