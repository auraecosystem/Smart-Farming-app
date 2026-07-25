@dataclass
class Production:
    production_id: str
    farm_id: str
    farmer_id: str
    crop_id: str

    planted_area_hectares: Decimal
    predicted_yield_kg: Decimal

    actual_yield_kg: Decimal | None = None
    quality_grade: str | None = None

    verification_score: Decimal = Decimal("0")
    status: str = "pending"
