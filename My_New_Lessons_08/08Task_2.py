class DivisionByNull:
    def __init__(self, my_number, zero_num):
        self.my_number = my_number
        self.zero_num = zero_num

    @staticmethod
    def num_by_zero(my_number, zero_num):
        try:
            return (my_number / zero_num)
        except:
            return (f'На ноль делить нельзя')


div = DivisionByNull(10, 0)
print(DivisionByNull.num_by_zero(10, 0))
print(DivisionByNull.num_by_zero(10, 7))
print(div.num_by_zero(100, 0))