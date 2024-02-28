def simple_hash(string):
    """
    This function takes a string as input and returns an integer hash value.

    Args:
        string: The string to be hashed.

    Returns:
        An integer representing the hash value of the input string.
    """

    # Initialize an empty variable to store the hash value
    hash_value = 0

    # Iterate over each character in the string
    for char in string:
        # Convert the character to its ASCII code
        ascii_code = ord(char)

        # Add the ASCII code to the current hash value
        hash_value += ascii_code

    # Return the final hash value
    return hash_value


# Example usage
name = "Luna1234567$"
hash_value = simple_hash(name)

print(f"Hash value for '{name}': {hash_value}")


class Node:
    """
    Node class for storing key-value pairs in a linked list.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    Simple hash table implementation with separate chaining for collision resolution.
    """

    def __init__(self, size):
        self.array = [None] * size  # Array to store linked lists
        self.size = size

    def hash(self, key):
        """
        Hash function using sum of ASCII codes.
        """
        hash_value = hash(key) % self.size
        return hash_value

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.
        """
        hash_value = self.hash(key)
        head = self.array[hash_value]

        # Create a new node
        new_node = Node(key, value)

        # If no collision, insert at the head of the linked list
        if head is None:
            self.array[hash_value] = new_node
            return

        # Otherwise, traverse the linked list and insert at the end
        current_node = head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def lookup(self, key):
        """
        Looks up a value in the hash table for a given key.

        Args:
            key: The key to search for.

        Returns:
            The value associated with the key, or None if not found.
        """
        hash_value = self.hash(key)
        current_node = self.array[hash_value]

        # Traverse the linked list at the index
        while current_node is not None:
            if current_node.key == key:
                return current_node.value  # Key found, return the value
            current_node = current_node.next

        # Key not found in the linked list at the index
        return None


# Example usage
hash_table = HashTable(5)
hash_table.insert("Alice", 25)
hash_table.insert("Bob", 30)
hash_table.insert("Charlie", 35)

value = hash_table.lookup("Alice")
print(f"Value for 'Alice': {value}")  # Output: Value for 'Alice': 25

value = hash_table.lookup("David")
print(f"Value for 'David': {value}")  # Output: Value for 'David': None (not found)
