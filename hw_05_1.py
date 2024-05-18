class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return True
        return False

# Приклад використання
hash_table = HashTable(10)
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")

# Пошук значення за ключем "key1"
print("Value before delete:", hash_table.search("key1"))  # Виведе 'value1'

# Видалення ключа "key1"
delete_result = hash_table.delete("key1")
print("Delete result:", delete_result)  # Виведе True

# Пошук значення за ключем "key1" після видалення
print("Value after delete:", hash_table.search("key1"))  # Виведе None, оскільки ключ видалено
