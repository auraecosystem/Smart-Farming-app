class KAVP:

    def __init__(self):
        self.crops = {}
        self.farms = {}
        self.productions = {}
        self.arcs = {}

    def register_crop(self, crop):
        self.crops[crop.crop_id] = crop

    def register_farm(self, farm):
        self.farms[farm.farm_id] = farm

    def create_production(
        self,
        farm_id,
        crop_id,
        predicted_yield_kg
    ):
        if farm_id not in self.farms:
            raise ValueError("Farm not found")

        if crop_id not in self.crops:
            raise ValueError("Crop not found")

        production = Production(
            production_id=f"PROD-{uuid4().hex[:12].upper()}",
            farm_id=farm_id,
            crop_id=crop_id,
            predicted_yield_kg=Decimal(
                str(predicted_yield_kg)
            )
        )

        self.productions[
            production.production_id
        ] = production

        return production
