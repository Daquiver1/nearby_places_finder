# Nearby Places Finder

This Python project allows you to find nearby locations of a specific type (e.g., schools, restaurants) in a given location. It utilizes the Google Maps Places API to fetch relevant data and provides the results in either CSV or text format.

## Features

- **User-friendly interface:** Easy-to-use prompts guide you through the search process.
- **Multiple place types:** Search for a wide variety of places using Google Maps' place types.
- **Customizable output:** Choose between CSV or text format for the results.

## List of Supported Place Types

- accounting
- airport
- amusement_park
- aquarium
- art_gallery

  You'll find the complete list in the src/utils/places.py file.

## Requirements

- Python 3.x
- Install the required Python packages:

  ```bash
  pip install -r requirements.txt
  ```

## Environment Variables (`.env`)

Create a `.env` file in the project root directory and add the following:

- `GOOGLE_MAPS_API_KEY`: Your Google Maps Places API key. Obtain one from the [Google Cloud Console](https://console.cloud.google.com/google/maps-apis).

## Usage

1. **Obtain Google Maps API Key:** Get your API key from the Google Cloud Console.
2. **Set Environment Variables:** Create a `.env` file in the project root and add your API key.
3. **Run the script:**

   ```bash
   python main.py
   ```

4. **Follow the prompts:**
   - Enter the desired place type (or type "list" to see all options).
   - Enter the location.
   - Choose the output format (csv or text).

The script will create a file with the results in the `data` directory. The file name will include the place type and location for easy identification.

## Future Improvements

- Fuzzy matching for place type input
- Auto-complete for place types and locations
- Implement a GUI for a more interactive experience

## Conclusion

Feel free to reach out.
