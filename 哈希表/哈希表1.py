# my_dict = {"Kanye":"come to life"}
#
# print(my_dict["Kanye"])
# print(my_dict.get("Drake","无此人"))
#

# 创建哈希表
class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*size
    # 哈希函数，用于返回键的真正索引地址
    def _hash(self,key):
        return ord(key[0])%self.size
    def set(self,key,value):
        hash_index = self._hash(key)
        self.table[hash_index] = (key,value)
    def get(self,key):
        hash_index = self._hash(key)
        if self.table[hash_index] is not None:
            return self.table[hash_index]
        raise KeyError(f"Key{key} not found")
    def remove(self,key):
        hash_index = self._hash(key)
        if self.table[hash_index] is not None:
            self.table[hash_index] = None
        else:
            raise KeyError(f"Key{key} not found")


if __name__ == "__main__":
    hash_table = HashTable(10)

    hash_table.set("Kanye","come to life")
    hash_table.set("XXXtentaction","Moonlight")

    print(hash_table.get("XXXtentaction"))
    hash_table.remove("XXXtentaction")
    # print(hash_table.get("XXXtentaction"))



