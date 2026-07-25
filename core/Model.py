from dataclasses import dataclass
from decimal import Decimal
from enum import Enum
from uuid import uuid4


class ProductionStatus(str, Enum):
    ACTIVE = "active"
    PENDING_VERIFICATION = "pending_verification"
    VERIFIED = "verified"
    REJECTED = "rejected"


@dataclass
class Crop:
    crop_id: str
    name: str
    category: str
    season: str


@dataclass
class Farm:
    farm_id: str
    owner_id: str
    name: str
    location: str
    area_hectares: Decimal


@dataclass
class Production:
    production_id: str
    farm_id: str
    crop_id: str
    predicted_yield_kg: Decimal
    actual_yield_kg: Decimal | None = None
    quality_grade: str | None = None
    status: ProductionStatus = ProductionStatus.ACTIVE


@dataclass
class ARC:
    receipt_id: str
    production_id: str
    farm_id: str
    crop_id: str
    verified_quantity_kg: Decimal
    reference_value: Decimal
    status: str = "active"
