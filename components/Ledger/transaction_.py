@dataclass
class LedgerTransaction:
    transaction_id: str
    transaction_type: str
    from_wallet: str | None
    to_wallet: str | None
    asset_id: str
    quantity: Decimal
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
