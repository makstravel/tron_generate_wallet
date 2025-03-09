from tronpy import Tron

def create_tron_wallet():

    tron = Tron(network='shasta')
    # Генерируем адрес и мнемоническую фразу
    wallet_address, mnemonic = tron.generate_address_with_mnemonic()
    return wallet_address['base58check_address'], mnemonic

