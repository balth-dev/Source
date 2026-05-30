from app.views.homepage import HomepageView
from app.repositories.building_repository import BuildingRepository

class HomepageController:
    def __init__(self, view: HomepageView, repository: BuildingRepository):
        self.view = view
        self.repository = repository
        self._initialize()
    
    
    def _initialize(self):
        buildings = self.repository.get_all_buildings()
        self.view.set_buildings(buildings)