'Implement a bitarray using a bytearray as the underlying storage'

class BitArray:

    def __init__(self, numbits):
        self.numbits = numbits
        numbytes = (numbits + 7) // 8
        self.array = bytearray(numbytes)

    def __setitem__(self, index, value):
        if index >= self.numbits:
            raise IndexError
        bytepos, bitpos = divmod(index, 8)
        if value:
            self.array[bytepos] |= 1 << bitpos
        else:
            self.array[bytepos] &= ~(1 << bitpos)

    def __getitem__(self, index):
        if index >= self.numbits:
            raise IndexError
        bytepos, bitpos = divmod(index, 8)
        return (self.array[bytepos] >> bitpos) & 1

    def __len__(self):
        return self.numbits
        

    
