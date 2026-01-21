# class MyHashMap:
#
#     def __init__(self):
#         self.dict = []
#
#     def put(self, key: int, value: int) -> None:
#         for i in range(len(self.dict)):
#             if self.dict[i][0] == key:
#                 self.dict[i][1] = value
#                 return
#         self.dict.append([key, value])
#
#     def get(self, key: int) -> int:
#         for k, v in self.dict:
#             if k == key:
#                 return v
#
#         return -1
#
#     def remove(self, key: int) -> None:
#         for k, v in self.dict:
#             if k == key:
#                 self.dict.remove([k,v])



class MyHashMap:

    def __init__(self):
        self.data = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        val = self.data[key]
        return val if val is not None else -1


    def remove(self, key: int) -> None:
        self.data[key] = None
