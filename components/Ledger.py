class KIBSLedger:

    def __init__(self):
        self.wallets = {}
        self.transactions = {}
        self.asset_owners = {}

    def create_wallet(self, owner_id):
        wallet = Wallet(
            wallet_id=f"WALLET-{uuid4().hex[:12].upper()}",
            owner_id=owner_id
        )

        self.wallets[wallet.wallet_id] = wallet

        return wallet

    def record_arc_issuance(
        self,
        wallet_id,
        arc_id,
        quantity
    ):
        if wallet_id not in self.wallets:
            raise ValueError("Wallet not found")

        if arc_id in self.asset_owners:
            raise ValueError(
                "ARC has already been issued"
            )

        transaction = LedgerTransaction(
            transaction_id=(
                f"TX-{uuid4().hex[:12].upper()}"
            ),
            transaction_type="ARC_ISSUANCE",
            from_wallet=None,
            to_wallet=wallet_id,
            asset_id=arc_id,
            quantity=Decimal(str(quantity))
        )

        self.transactions[
            transaction.transaction_id
        ] = transaction

        self.asset_owners[
            arc_id
        ] = wallet_id

        return transaction
