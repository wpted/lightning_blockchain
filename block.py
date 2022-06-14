import hashlib


class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data
        self.hash = hash
        self.last_hash = last_hash

    @classmethod
    def lighting_hash(cls, data):
        return hashlib.sha256(str(data).encode("utf-8")).hexdigest()


class BlockChain:
    GENESIS = Block("gen_data", "gen_hash", "gen_last_hash")

    def __init__(self):
        self.chain = [BlockChain.GENESIS]

    def __repr__(self):
        return f"BlockChain{self.chain}"


    def add_block(self, data):
        last_hash = self.chain[-1].hash
        hash = Block.lighting_hash(str(data) + last_hash)

        block = Block(data, hash, last_hash)
        self.chain.append(block)


if __name__ == '__main__':
    print(Block.lighting_hash("Victoria"))
    b = BlockChain()
    print(b)
