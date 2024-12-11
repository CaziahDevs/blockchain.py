class Transaction(object):
    def __init__(self, sender: str, receipient: str, amount: int):
        """
        Initializes a new Transaction object.

        Parameters:
        sender (str): The sender's address.
        receipient (str): The recipient's address.
        amount (int): The amount of currency transferred.

        Returns:
        None
        """
        self.sender = sender
        self.receipient = receipient
        self.amount = amount