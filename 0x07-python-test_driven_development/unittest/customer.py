class Customer:
    """A sample customer class

    >>> customer_1 = Customer('Digho', 'Jordan', 2000)
    >>> customer_2 = Customer('Chidera', 'Bevanie', 1500)
    >>> customer_1.customer_mail
    'Digho.Jordan@email.com'
    >>> customer_2.customer_fullname
    'Chidera Bevanie'
    >>> customer_1.apply_discount()
    >>> customer_2.apply_discount()
    >>> customer_1.purchase
    1900
    >>> customer_2.purchase
    1425
    """

    discount = 0.95

    def __init__(self, first_name, last_name, purchase):
        self.first_name = first_name
        self.last_name = last_name
        self.purchase = purchase

    @property
    def customer_mail(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    @property
    def customer_fullname(self):
        return f'{self.first_name} {self.last_name}'

    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
