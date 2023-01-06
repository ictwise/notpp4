from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_event_intent_suceeded(self, event):
        """
        Handle intent_suceeded webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_event_payment_failed(self, event):
        """
        Handle payment_failed webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)