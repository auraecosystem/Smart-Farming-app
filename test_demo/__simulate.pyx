kavp = KAVP()

kavp.register_crop(
    Crop(
        crop_id="maize",
        name="Maize",
        category="cereal",
        season="kharif"
    )
)

kavp.register_farm(
    Farm(
        farm_id="FARM-001",
        owner_id="FARMER-001",
        name="Kubu Smart Farm",
        location="Nigeria",
        area_hectares=Decimal("2.5")
    )
)

production = kavp.create_production(
    farm_id="FARM-001",
    crop_id="maize",
    predicted_yield_kg=4500
)

kavp.record_harvest(
    production_id=production.production_id,
    actual_yield_kg=4300,
    quality_grade="A"
)

kavp.verify_production(
    production.production_id
)

arc = kavp.issue_arc(
    production.production_id,
    market_price_per_kg=500
)

print(arc)
