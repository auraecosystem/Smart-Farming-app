def verify_production(self, production_id):

    production = self.productions.get(
        production_id
    )

    if not production:
        raise ValueError(
            "Production not found"
        )

    if not production.actual_yield_kg:
        raise ValueError(
            "Harvest has not been recorded"
        )

    # Initial MVP verification rule.
    # Later this becomes a multi-source
    # verification engine.
    maximum_expected = (
        production.predicted_yield_kg
        * Decimal("1.5")
    )

    if (
        production.actual_yield_kg
        > maximum_expected
    ):
        production.status = (
            ProductionStatus.REJECTED
        )
        return production

    production.status = (
        ProductionStatus.VERIFIED
    )

    return production
