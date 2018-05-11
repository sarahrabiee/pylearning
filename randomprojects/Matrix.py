class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_size(self):
        x = len(self.matrix)
        if x == 0:
            return [0, 0]
        y = len(self.matrix[0])
        for list in self.matrix:
          if len(list) != y:
              raise Exception('Your matrix is not complete!')
        return [x, y]

    def get_value(self, index):
        return self.matrix[index]

    def msum(self, mat2):
        matsum = []
        if self.get_size() != mat2.get_size():
            raise Exception('Oops! your matrices are not equal in size')
        for index in range(len(self.matrix)):
            list1 = self.get_value(index)
            list2 = mat2.get_value(index)
            result_list = []
            for item in range(len(list1)):
                result_list.append(list1[item] + list2[item])
            matsum.append(result_list)
        return Matrix(matsum)

    def matprint(self):
        for list in self.matrix:
            print list
        print

v = Matrix([[4, 5], [6, 7]])
w = Matrix([[7, 8], [8, 4]])

print v.msum(w).matprint()
