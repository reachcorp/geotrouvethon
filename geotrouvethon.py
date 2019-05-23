from flask import Flask
from flask import jsonify
from geopy import geocoders

geotrouvethon_port = 9966

app = Flask(__name__)

resolved_locations = {}

@app.route('/locate/<location_name>', methods=['GET'])
def get_location(location_name):
    try:
        # check if location already resolved
        if location_name in resolved_locations:
            loc = resolved_locations.get(location_name, "none")
        else:
            g = geocoders.Nominatim(user_agent="dummy")
            loc = g.geocode(location_name, timeout=10)
            # store location and coord
            resolved_locations[location_name] = loc

        return jsonify(loc.latitude, loc.longitude)

    except:
        return jsonify(-99,99)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=geotrouvethon_port)
