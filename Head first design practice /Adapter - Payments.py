


from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


class StripePaymentProcessor:
    def make_payment(self, amount: float) -> None:
        print(f"Processing payment of ${amount} through Stripe.")


class PayPalPaymentProcessor:
    def send_payment(self, amount: float) -> None:
        print(f"Processing payment of ${amount} through PayPal.")


class RazorpayPaymentProcessor:
    def execute_payment(self, amount: float) -> None:
        print(f"Processing payment of ${amount} through Razorpay.")


class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_processor: StripePaymentProcessor) -> None:
        self.stripe_processor = stripe_processor

    def process_payment(self, amount: float) -> None:
        self.stripe_processor.make_payment(amount)

class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal_processor: PayPalPaymentProcessor) -> None:
        self.paypal_processor = paypal_processor

    def process_payment(self, amount: float) -> None:
        self.paypal_processor.send_payment(amount)

class RazorpayAdapter(PaymentProcessor):
    def __init__(self, razorpay_processor: RazorpayPaymentProcessor) -> None:
        self.razorpay_processor = razorpay_processor

    def process_payment(self, amount: float) -> None:
        self.razorpay_processor.execute_payment(amount)


# Client code
def process_order(payment_processor: PaymentProcessor, amount: float) -> None:
    payment_processor.process_payment(amount)

# Usage
stripe_processor = StripePaymentProcessor()
paypal_processor = PayPalPaymentProcessor()
razorpay_processor = RazorpayPaymentProcessor()

stripe_adapter = StripeAdapter(stripe_processor)
paypal_adapter = PayPalAdapter(paypal_processor)
razorpay_adapter = RazorpayAdapter(razorpay_processor)

process_order(stripe_adapter, 100.0)   # Processing payment of $100.0 through Stripe.
process_order(paypal_adapter, 200.0)
# Processing payment of $200.
