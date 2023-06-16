class FSLA:
    def __init__(self, length):
        self.length = length
        self.array = [None] * length

    def __getitem__(self, index):
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        return self.array[index]

    def __setitem__(self, index, value):
        if index >= self.length or index < 0:
            raise IndexError("Index out of range")
        self.array[index] = value

    def concat(self, other):
        if len(self.array) != len(other.array):
            raise ValueError("Arrays must have the same length")
        result = FSLA(self.length)
        for i in range(self.length):
            result[i] = self[i] + other[i]
        return result

    def merge(self, other):
        result = FSLA(self.length + other.length)
        for i in range(self.length):
            result[i] = self[i]
        for i in range(other.length):
            if other[i] not in self.array:
                result[self.length + i] = other[i]
        return result

    def print_elem(self, index):
        print(self[index])
    
    def print_array(self):
        for i in range(self.length):
            print(self[i])

if __name__=="__main__":
    
    # создание массива
    array1 = FSLA(3)
    array1[0] = "bus"
    array1[1] = "PC"
    array1[2] = "mouse"

    # обращение к элементу массива
    print(array1[1])

    print("\n\n") # для увеличения читабельности кода

    # выполнение операции поэлементного сцепления
    array2 = FSLA(3)
    array2[0] = "keyboard"
    array2[1] = "CPU"
    array2[2] = "GPU"
    array3 = array1.concat(array2)
    array3.print_array()

    print("\n\n")# для увеличения читабельности кода

    # выполнение операции слияния
    arr4 = FSLA(3)
    arr4[0] = "MHA"
    arr4[1] = "Atack of the Titan"
    arr4[2] = "Kimetsu no Yaiba"
    arr5 = array1.merge(arr4)

    print(arr5[2])
    print("\n") # для увеличения читабельности кода
    arr5.print_array()