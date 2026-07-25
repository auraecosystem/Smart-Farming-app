def issue_arc(
    self,
    production_id,
    market_price_per_kg
):
    production = self.productions.get(
        production_id
    )

    if not production:
        raise ValueError(
            "Production not found"
        )

    if (
        production.status
        != ProductionStatus.VERIFIED
    ):
        raise ValueError(
            "Production is not verified"
        )

    reference_value = (
        production.actual_yield_kg
        * Decimal(str(market_price_per_kg))
    )

    arc = ARC(
        receipt_id=(
            f"ARC-{uuid4().hex[:12].upper()}"
        ),
        production_id=production.production_id,
        farm_id=production.farm_id,
        crop_id=production.crop_id,
        verified_quantity_kg=(
            production.actual_yield_kg
        ),
        reference_value=reference_value
    )

    self.arcs[
        arc.receipt_id
    ] = arc

    return arc
