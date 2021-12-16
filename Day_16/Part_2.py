from math import prod

op_codes = {
    0: lambda p_list: sum(pack.value for pack in p_list.sub),
    1: lambda p_list: prod(pack.value for pack in p_list.sub),
    2: lambda p_list: min(pack.value for pack in p_list.sub),
    3: lambda p_list: max(pack.value for pack in p_list.sub),
    5: lambda p_list: 1 if p_list.sub[0].value > p_list.sub[1].value else 0,
    6: lambda p_list: 1 if p_list.sub[0].value < p_list.sub[1].value else 0,
    7: lambda p_list: 1 if p_list.sub[0].value == p_list.sub[1].value else 0

}


class Packet:
    def __init__(self):
        self.version = self.convert_bits(3)
        self.op_code = self.convert_bits(3)
        self.value = 0
        self.sub = []

        if self.op_code == 4:
            self.read_literal()
        else:
            self.read_sub()
            self.operation()


    def operation(self):
        self.value = op_codes[self.op_code](self)

    def convert_bits(self, n):
        global cur, data
        val = int(data[cur:cur + n], 2)
        cur += n
        return val

    def read_literal(self):
        while True:
            connection = self.convert_bits(1)
            self.value = (self.value << 4) + self.convert_bits(4)
            if not connection:
                break

    def read_sub(self):
        global cur
        length_type_id = self.convert_bits(1)
        if length_type_id == 0:
            sub_len = self.convert_bits(15)
            end = cur + sub_len
            while cur < end:
                self.sub.append(Packet())
        else:
            num_pack = self.convert_bits(11)
            for i in range(num_pack):
                self.sub.append(Packet())

    def version_sum(self):
        sum_of_sub = sum([sub.version_sum() for sub in self.sub])
        return self.version + sum_of_sub


with open("/Users/fabianbong/Documents/Advent_Of_Code/Day_16/input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

cur = 0
data = bin(int(lines[0], 16))[2:]
p = Packet()
print(p.value)

