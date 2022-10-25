class ListVec(list):

    def __init__(self, lista):
        assert isinstance(lista, list)
        self.e = lista
        self.dim = len(self.e)

    def vec_sum(self, vec):

        assert len(self.e) == len(vec.e)
        lista_nueva = []
        for i in range(len(self.e)):
            lista_nueva.append(self.e[i] + vec.e[i])

        return ListVec(lista_nueva)

    def scalar_mul(self, scalar):
        lista_nueva = []
        for e in self.e:
            lista_nueva.append(e * scalar)

        return ListVec(lista_nueva)

    def dot(self, vec):

        assert len(self) == len(vec)
        dot = 0
        for i in range(len(self.e)):
            dot += self.e[i] * vec.e[i]

        return dot

    def norm(self):
        sum = 0
        for e in self.e:
            sum += e**2

        return sum**(1/2)

    def similarity(self, b):

        assert len(self.e) == len(b.e)
        num = self.dot(b)
        f_den = b.dot(b)**(1/2)
        s_den = self.dot(self)**(1/2)
        return num/(f_den*s_den)

    def __str__(self):
        return str(self.e)
