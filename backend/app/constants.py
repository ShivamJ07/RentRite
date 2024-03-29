from enum import Enum

class TableHeaders(Enum):
    BUILDING = 'Building'
    NEIGHBOURHOOD = 'Neighbourhood'
    ADDRESS = 'Address'
    CITY = 'City'
    LISTING = 'Listing'
    BED = 'Bed'
    BATH = 'Bath'
    SQFT = 'SqFt'
    PRICE = 'Price'
    UNIT_AMENITIES = 'Unit Amenities'
    BUILDING_AMENITIES =  'Building Amenities'
    PETS = 'Pets'
    LAT = 'Latitude'
    LON = 'Longitude'
    DATE = 'Date'

class UnitAmenities(Enum):
    BALCONY = 'Balcony'
    IN_UNIT_LAUNDRY = 'In Unit Laundry'
    AIR_CONDITIONING = 'Air Conditioning' 
    HIGH_CEILINGS = 'High Ceilings'
    FURNISHED = 'Furnished'
    HARDWOOD_FLOOR = 'Hardwood Floor'

class BuildingAmenities(Enum):
    CONTROLLED_ACCESS = 'Controlled Access'
    FITNESS_CENTER = 'Fitness Center'
    SWIMMING_POOL = 'Swimming Pool'
    ROOF_DECK = 'Roof Deck'
    STORAGE = 'Storage'
    RESIDENTS_LOUNGE = 'Residents Lounge'
    OUTDOOR_SPACE = 'Outdoor Space'


UnitAmenitiesDict = {
    UnitAmenities.BALCONY.value: 0,
    UnitAmenities.IN_UNIT_LAUNDRY.value: 0,
    UnitAmenities.AIR_CONDITIONING.value: 0,
    UnitAmenities.HIGH_CEILINGS.value: 0,
    UnitAmenities.FURNISHED.value: 0,
    UnitAmenities.HARDWOOD_FLOOR.value: 0
}

BuildingAmenitiesDict = {
    BuildingAmenities.CONTROLLED_ACCESS.value: 0,
    BuildingAmenities.FITNESS_CENTER.value: 0,
    BuildingAmenities.SWIMMING_POOL.value: 0,
    BuildingAmenities.ROOF_DECK.value: 0,
    BuildingAmenities.STORAGE.value: 0,
    BuildingAmenities.RESIDENTS_LOUNGE.value: 0,
    BuildingAmenities.OUTDOOR_SPACE.value: 0
}

locations = [
    {
        'location': 'Downtown Core',
        'bounding_box': {
            'southwest': {'lon': '-79.398', 'lat': '43.643'},
            'northeast': {'lon': '-79.3762', 'lat': '43.66'}
        }
    },
    {
        'location': 'Midtown',
        'bounding_box': {
            'southwest': {'lon': '-79.4165', 'lat': '43.67'},
            'northeast': {'lon': '-79.388', 'lat': '43.7'}
        }
    },
    {
        'location': 'West End',
        'bounding_box': {
            'southwest': {'lon': '-79.449', 'lat': '43.628'},
            'northeast': {'lon': '-79.402', 'lat': '43.65'}
        }
    },
    {
        'location': 'East End',
        'bounding_box': {
            'southwest': {'lon': '-79.36', 'lat': '43.65'},
            'northeast': {'lon': '-79.315', 'lat': '43.685'}
        }
    },
    {
        'location': 'North Toronto',
        'bounding_box': {
            'southwest': {'lon': '-79.425', 'lat': '43.7'},
            'northeast': {'lon': '-79.383', 'lat': '43.73'}
        }
    },
    {
        'location': 'University Area',
        'bounding_box': {
            'southwest': {'lon': '-79.4042', 'lat': '43.6572'},
            'northeast': {'lon': '-79.39', 'lat': '43.6675'}
        }
    },
    {
        'location': 'Scarborough',
        'bounding_box': {
            'southwest': {'lon': '-79.21498455469643', 'lat': '43.74522758306715'},
            'northeast': {'lon': '-79.17281544530357', 'lat': '43.78977241693285'}
        }
    },
    {
        'location': 'Etobicoke',
        'bounding_box': {
            'southwest': {'lon': '-79.57890339741783', 'lat': '43.6379061704074'},
            'northeast': {'lon': '-79.53609660258218', 'lat': '43.682093829592596'}
        }
    }
]

table_columns = [table_header.value for table_header in TableHeaders]