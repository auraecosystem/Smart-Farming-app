from dataclasses import dataclass, field
from decimal import Decimal
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class Wallet:
    wallet_id: str
    owner_id: str
    arc_balance: Decimal = Decimal("0")
    agc_balance: Decimal = Decimal("0")
