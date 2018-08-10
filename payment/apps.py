from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'
    verobose_name='Оплата'
    def ready(self):
        import payment.signals
