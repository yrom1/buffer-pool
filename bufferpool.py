import os
import struct
from collections import OrderedDict


class LRUBufferPool:
    def __init__(self, capacity, block_size, file_name):
        self.capacity = capacity
        self.block_size = block_size
        self.file_name = file_name
        self.buffer_pool = OrderedDict()  # LRU cache

    def read(self, block_id):
        if block_id in self.buffer_pool:
            data, dirty_bit = self.buffer_pool.pop(block_id)
            self.buffer_pool[block_id] = (
                data,
                dirty_bit,
            )  # Move to the end (most recently used)
            return data
        else:
            return self.read_from_disk(block_id)

    def write(self, block_id, data):
        if block_id in self.buffer_pool:
            # Update data and set dirty bit
            self.buffer_pool.pop(block_id)
            self.buffer_pool[block_id] = (data, True)
        else:
            # Evict LRU block if necessary
            if len(self.buffer_pool) >= self.capacity:
                oldest_block_id, (
                    oldest_data,
                    oldest_dirty_bit,
                ) = self.buffer_pool.popitem(last=False)
                if oldest_dirty_bit:
                    self.write_to_disk(oldest_block_id, oldest_data)

            self.buffer_pool[block_id] = (data, True)

    def read_from_disk(self, block_id):
        offset = block_id * (
            self.block_size + 5
        )  # Calculate the offset based on block ID
        with open(self.file_name, "rb") as file:
            file.seek(offset)
            header = file.read(5)
            if header:
                _, dirty_bit = struct.unpack("<IB", header)
                data = file.read(self.block_size)
                self.buffer_pool[block_id] = (data, dirty_bit)
                return data
            else:
                # Handle missing block case
                return None

    def write_to_disk(self, block_id, data):
        # Implement actual writing to disk logic here
        print(f"Writing block {block_id} to disk...")
        offset = block_id * (
            self.block_size + 5
        )  # Calculate the offset based on block ID
        with open(self.file_name, "rb+") as file:
            file.seek(offset)
            header = struct.pack(
                "<IB", block_id, 1
            )  # Set dirty bit to 1 when writing to disk
            file.write(header)
            file.write(data)

    def print_bin_file_contents(self):
        print("Contents of the .bin file:")
        with open(self.file_name, "rb") as file:
            block_id = 0
            while True:
                header = file.read(5)
                if not header:
                    break
                _, dirty_bit = struct.unpack("<IB", header)
                data = file.read(self.block_size)
                print(f"Block ID: {block_id}, Dirty Bit: {dirty_bit}, Data: {data}")
                block_id += 1


# Usage
block_size = 512
file_name = "custom_blocks.bin"

# Initialize the custom file with empty blocks
with open(file_name, "wb") as file:
    for _ in range(10):
        header = struct.pack("<IB", 0, 0)
        file.write(header)
        file.write(b"\x00" * block_size)

buffer_pool = LRUBufferPool(capacity=3, block_size=block_size, file_name=file_name)

buffer_pool.write(1, b"Block 1 data")
buffer_pool.write(2, b"Block 2 data")
buffer_pool.write(3, b"Block 3 data")
buffer_pool.write(4, b"Block 4 data")  # This will evict Block 1 and write it to disk
buffer_pool.print_bin_file_contents()  # Print the contents of the .bin file

read_data = buffer_pool.read(1)  # Read Block 1 from disk
print(read_data)
