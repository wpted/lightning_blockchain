from block import BlockChain
lighting_blockchain = BlockChain()


def main():
    print("Hello BlockChain\n")
    lighting_blockchain.add_block(616)
    lighting_blockchain.add_block(323)
    lighting_blockchain.add_block(502)

    for block in lighting_blockchain.chain:
        print(block.__dict__)


if __name__ == '__main__':
    main()
