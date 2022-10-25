class ListVec(list):

    def __init__(self, lista):
        assert isinstance(lista, list)
        self.e = lista
        self.dim = len(self.e)

    def vec_sum(self, vec):

        assert len(self) == len(vec)
        lista_nueva = []
        for i in range(len(self)):
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
        for i in range(len(self)):
            dot += self.e[i] * vec.e[i]

        return dot

    def norm(self):
        sum = 0
        for e in self.e:
            norma += e**2

        return sum**(1/2)

    def similarity(self, b):

        assert len(self) == len(b)
        for i in range(len(self)):
            if self.e[i] == b.e[i]:
                pass
            else:
                return False

        return True

    def __str__(self):
        return str(self.e)
