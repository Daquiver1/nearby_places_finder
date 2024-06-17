"""IO Service module."""

import csv


class IOService:
    """Service class for handling input/output operations."""

    def write_to_csv(self, schools: list[dict], file_path: str) -> None:
        """Write the search results to a CSV file."""
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Index", "Name", "Address"])  # Header row for CSV
            for idx, school in enumerate(schools, 1):
                writer.writerow([idx, school["name"], school["address"]])

    def write_to_text(self, schools: list[dict], file_path: str) -> None:
        """Write the search results to a text file."""
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            for idx, school in enumerate(schools, 1):
                f.write(f"{idx}. {school['name']} - {school['address']}\n")

    def create_file_path(self, place_type: str, location: str, file_type: str) -> str:
        """Create a file name based on the place type and location."""
        file_extension = ".csv" if file_type == "csv" else ".txt"
        return f"data/search_results_{place_type}_{location.replace(' ', '_').replace(',','_')}{file_extension}"
