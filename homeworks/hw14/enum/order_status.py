from enum import Enum


class OrderStatus(Enum):
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN_PROGRESS'
    READY = 'READY'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class Order:
    def __init__(self, order_id, status=OrderStatus.PENDING):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def display_status(self):
        return f'Order {self.order_id}: {self.status.value}'
