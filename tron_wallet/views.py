from django.shortcuts import render
from .models import TronWallet
from .services.qrcode_service import generate_qr_code
from .services.tron_service import create_tron_wallet

def index(request):
    """
    Представление для главной страницы, которое создает новый Tron-кошелек,
    сохраняет его в базе данных и передает данные в шаблон.
    """

    # создает новый Tron-кошелек (получаем адрес и мнемоническую фразу)
    address, mnemonic = create_tron_wallet()

    # cохраняем кошелек в базе данных
    TronWallet.objects.create(
        address=address,
        mnemonic=mnemonic
    )

    #данные в шаблон с кошельком и QR-кодом
    data = {
        "address": address,
        "mnemonic": mnemonic,
        "qr_code": generate_qr_code(address)
    }

   # HTML-шаблон и передаем в него данные
    return render(request, 'index.html', {'data': data})

