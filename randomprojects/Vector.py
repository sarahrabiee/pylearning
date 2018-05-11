class Vector:
    def __init__(self, vec1):
        self.vector = vec1

    def __len__(self):
        return len(self.vector)

    def get_value(self, index):
        return self.vector[index]

    def set_value(self, index, value):
        self.vector[index] = value

    def add_value(self, value):
        self.vector.append(value)

    def vsum(self, vec2):
        sum = Vector([])
        if len(self) == len(vec2):
            for index in range(len(self)):
                sum.add_value(self.get_value(index) + vec2.get_value(index))
            return sum
        raise Exception('The size of vectors are not equal.')

    def vdot(self, vec2):
        result = 0
        if len(self) == len(vec2):
            for index in range(len(self)):
                result += self.get_value(index) * vec2.get_value(index)
            return result
        raise Exception('The size of vectors are not equal.')