from flask import Flask, render_template, request, redirect, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Replace the following URI with your MongoDB Atlas connection string
app.config["MONGO_URI"] = "mongodb+srv://harshal:Harshal2022@cluster0.u5i2m.mongodb.net/form?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

# Route for rendering the form
@app.route('/')
def index():
    return render_template('form.html')

# Route for handling form submissions
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Extract form data
        form_data = {
            "model": request.form.get('model'),
            "color": request.form.get('color'),
            "safety_glass": request.form.get('safety_glass'),
            "back_cover": request.form.get('back_cover'),
            "ram": request.form.get('ram'),
            "internal_memory": request.form.get('internal_memory'),
            "camera_specs": request.form.get('camera_specs'),
            "cameras_check": request.form.get('cameras_check'),
            "battery_percentage": request.form.get('battery_percentage'),
            "sim_slots": request.form.get('sim_slots'),
            "sim_provider": request.form.get('sim_provider'),
            "wifi_connected": request.form.get('wifi_connected'),
            "bluetooth_status": request.form.get('bluetooth_status'),
            "sd_card": request.form.get('sd_card'),
            "sd_capacity": request.form.get('sd_capacity'),
            "mobile_uptime": request.form.get('mobile_uptime'),
            "time_zone": request.form.get('time_zone'),
            "language": request.form.get('language'),
            "installed_apps": request.form.get('installed_apps'),
            "geo_location": request.form.get('geo_location'),
            "build_no": request.form.get('build_no'),
            "kernel_version": request.form.get('kernel_version'),
            "iccid": request.form.get('iccid'),
            "imsi": request.form.get('imsi'),
            "meid": request.form.get('meid'),
            "airplane_mode": request.form.get('airplane_mode')
        }
        
        # Insert data into MongoDB
        mongo.db.device_info.insert_one(form_data)

        return redirect('/')

# API route to create a new entry (equivalent to form submission)
@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.json
    if data:
        mongo.db.device_info.insert_one(data)
        return jsonify({"message": "Data added successfully"}), 201
    return jsonify({"error": "No data provided"}), 400

# API route to retrieve data by ID
@app.route('/api/data/<id>', methods=['GET'])
def get_data(id):
    try:
        data = mongo.db.device_info.find_one({"_id": ObjectId(id)})
        if data:
            data['_id'] = str(data['_id'])  # Convert ObjectId to string
            return jsonify(data), 200
        return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API route to update data by ID
@app.route('/api/data/<id>', methods=['PUT'])
def update_data(id):
    data = request.json
    if data:
        try:
            result = mongo.db.device_info.update_one({"_id": ObjectId(id)}, {"$set": data})
            if result.matched_count:
                return jsonify({"message": "Data updated successfully"}), 200
            return jsonify({"error": "Data not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    return jsonify({"error": "No data provided"}), 400

# API route to delete data by ID
@app.route('/api/data/<id>', methods=['DELETE'])
def delete_data(id):
    try:
        result = mongo.db.device_info.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"message": "Data deleted successfully"}), 200
        return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
