import datetime

class FintechCompliance:
    """
    Class representing the compliance checks for Fintech companies in Nigeria.
    This covers regulatory compliance, data privacy laws, and transaction verifications.
    """

    def __init__(self, company_name, registration_number, is_licensed, registration_date):
        """
        Initialize the Fintech compliance class.
        :param company_name: Name of the Fintech company
        :param registration_number: Registration number with the Corporate Affairs Commission
        :param is_licensed: Boolean indicating if the company is licensed by Central Bank of Nigeria
        :param registration_date: Date of the company's incorporation
        """
        self.company_name = company_name
        self.registration_number = registration_number
        self.is_licensed = is_licensed
        self.registration_date = registration_date
        self.nigeria_regulations = {
            'Central Bank of Nigeria (CBN)': 'Payment System Regulation',
            'Nigeria data Protection Commission (NDPC)': 'Nigeria Data Protection Act',
            'Nigerian Communications Commission (NCC)': 'Telecommunications Regulation'
        }

    def verify_compliance(self):
        """
        Verifies if the Fintech company is compliant with Nigerian regulations.
        """
        today = datetime.datetime.today().date()
        if not self.is_licensed:
            print(f"{self.company_name} is not licensed by the Corporate Affairs Commission.")
            return False
        if today < self.registration_date:
            print(f"Registration date of {self.company_name} is not valid yet.")
            return False
        print(f"{self.company_name} is compliant with the regulatory frameworks in Nigeria.")
        return True

    def get_regulatory_info(self):
        """
        Returns details of the regulatory frameworks the company must comply with.
        """
        return self.nigeria_regulations

    def print_compliance_details(self):
        """
        Prints all compliance information for the Fintech company.
        """
        print(f"\nCompliance Details for {self.company_name}:")
        print(f"Registration Number: {self.registration_number}")
        print(f"Registered on: {self.registration_date}")
        print("Regulatory Compliance Requirements:")
        for agency, regulation in self.nigeria_regulations.items():
            print(f"- {agency}: {regulation}")
        print(f"Licensed: {'Yes' if self.is_licensed else 'No'}")


class Transaction:
    """
    Class for managing and verifying transactions for legality based on Nigerian financial laws.
    """
    def __init__(self, transaction_id, sender_account, receiver_account, amount, date, is_legal=True):
        """
        Initialize a financial transaction.
        :param transaction_id: Unique ID for the transaction
        :param sender_account: Account ID of the sender
        :param receiver_account: Account ID of the receiver
        :param amount: Transaction amount
        :param date: Date of the transaction
        :param is_legal: Boolean indicating whether the transaction is legal or flagged (default True)
        """
        self.transaction_id = transaction_id
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.amount = amount
        self.date = date
        self.is_legal = is_legal

    def verify_transaction(self):
        """
        Verifies if the transaction complies with Nigerian financial laws (e.g., Banks and Other Financial Institutions Act, 2020; Money Laundering (Prohibition) Act (MLPA) of 2011)The Money Laundering (Prevention and Prohibition) Act, 2022 (MLA 2022).
        """
        if self.is_legal:
            print(f"Transaction {self.transaction_id} is verified and compliant with Nigerian laws.")
            return True
        else:
            print(f"Transaction {self.transaction_id} is flagged as suspicious. Further investigation required.")
            return False

    def check_anti_money_laundering(self):
        """
        Simulates anti-money laundering (AML) checks on the transaction.
        """
        # Example: Transactions above 10 million Naira require an AML check in Nigeria
        if self.amount > 10000000:
            print(f"Transaction {self.transaction_id} requires Anti-Money Laundering (AML) checks.")
            return False
        return True

    def print_transaction_details(self):
        """
        Print details of the transaction.
        """
        print(f"\nTransaction Details (ID: {self.transaction_id}):")
        print(f"Sender: {self.sender_account}")
        print(f"Receiver: {self.receiver_account}")
        print(f"Amount: {self.amount} Naira")
        print(f"Date: {self.date}")
        print(f"Legality: {'Legal' if self.is_legal else 'Illegal'}")


# Example usage
if __name__ == "__main__":
    # Create Fintech company instance
    fintech_company = FintechCompliance(
        company_name="FinDoor AfriQor",
        registration_number="RC98765",
        is_licensed=True,
        registration_date=datetime.date(2024, 7, 7)
    )

    # Verify the Fintech company's compliance with Nigerian regulations
    fintech_company.verify_compliance()
    fintech_company.print_compliance_details()

    # Create a legal transaction
    transaction1 = Transaction(
        transaction_id="TXN001",
        sender_account="ACC1001",
        receiver_account="ACC2002",
        amount=5000000,  # Amount in Naira
        date=datetime.date(2025, 1, 27),
        is_legal=True
    )
    
    # Verify the transaction
    transaction1.verify_transaction()
    transaction1.check_anti_money_laundering()
    transaction1.print_transaction_details()

    # Create an illegal transaction (e.g., amount above the legal limit)
    transaction2 = Transaction(
        transaction_id="TXN002",
        sender_account="ACC3001",
        receiver_account="ACC4002",
        amount=15000000,  # Amount in Naira
        date=datetime.date(2025, 1, 27),
        is_legal=False
    )
    
    # Verify the illegal transaction
    transaction2.verify_transaction()
    transaction2.check_anti_money_laundering()
    transaction2.print_transaction_details()
