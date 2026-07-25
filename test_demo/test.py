ledger = KIBSLedger()

wallet = ledger.create_wallet(
    owner_id="FARMER-001"
)

transaction = ledger.record_arc_issuance(
    wallet_id=wallet.wallet_id,
    arc_id=arc.receipt_id,
    quantity=arc.verified_quantity_kg
)
