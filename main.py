"""Main file"""

from src.services.gmap_service import GoogleMapsClient, NoPlacesFoundError
from src.services.io import IOService
from src.utils.io import get_file_type
from src.utils.valid_place import get_valid_place_type


def main(maps_service: GoogleMapsClient, io_service: IOService) -> None:
    """Main function for the script."""
    place_type = get_valid_place_type()
    location = input("Enter the location: ")
    file_type = get_file_type()

    try:
        places = maps_service.get_places_in_vicinity(location, place_type)
        if not places:
            print(f"No {place_type} found in the {location} vicinity")
            exit()

        file_path = io_service.create_file_path(place_type, location, file_type)
        (
            io_service.write_to_csv(places, file_path)
            if file_type == "csv"
            else io_service.write_to_text(places, file_path)
        )
        print(f"Results written to {file_path}")
    except NoPlacesFoundError:
        print(f"No {place_type} found in the {location} vicinity.")


if __name__ == "__main__":
    google_maps_service = GoogleMapsClient()
    io_service = IOService()
    main(google_maps_service, io_service)
