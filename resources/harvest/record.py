def record_harvest(
    self,
    production_id,
    actual_yield_kg,
    quality_grade
):
    production = self.productions.get(
        production_id
    )

    if not production:
        raise ValueError(
            "Production not found"
        )

    production.actual_yield_kg = Decimal(
        str(actual_yield_kg)
    )

    production.quality_grade = quality_grade

    production.status = (
        ProductionStatus.PENDING_VERIFICATION
    )

    return production
