##################################################
# import dependancies
##################################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


###################################################
# Database Setup
###################################################

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)



#Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


#Create our session (link) from Python to the DB

###################################################

#Flask Setup
app = Flask(__name__)

###################################################
# Flask Routes
###################################################

@app.route("/")
def home():
   return (
                f"Available Routes:<br/>"
                f"<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp/api/v1.0/precipitation:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp-Will return the date and the preciption values.<br/>"
                f"<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp/api/v1.0/stations:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp-Will provide a list of stations from the dataset.<br/>"
                "<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp/api/v1.0/&ltstart&gt:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp-Query for the dates and temperature observations from a year from the last data point.<br/>"
                "<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp/api/v1.0/&ltstart&gt/&ltend&gt:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp-Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.<br/>")


@app.route("/api/v1.0/precipitation")
def prcp(): 
    
    # Query all dates and precipitation
    session = Session(engine)
    prcp_data = session.query(Measurement.date, Measurement.station, Measurement.prcp).all()

    #create a dictionary from the new raw data and append to a list of prcp, with, station, and date values

    all_prcp = []
    for date, station, prcp in prcp_data:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Station"] = station
        prcp_dict["Precipitation"] = prcp

        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)

@app.route("/api/v1.0/stations")
def stations():
    # Query all dates and precipitation
    session = Session(engine)
    stations = session.query(Station.station).all()

    list_stations = list(np.ravel(stations))

    return jsonify(list_stations)


        


if __name__ == '__main__':
    app.run(debug=True)
        