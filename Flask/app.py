##################################################
# import dependancies
##################################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

from datetime import datetime, timedelta

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

@app.route("/api/v1.0/<start>")
def date(start):

    start_date = datetime.strptime(start, "%Y-%m-%d")
    year_before = start_date-timedelta(days=365)

    if start_date <= datetime(2017, 8, 23) or start_date >= datetime(2011, 1, 1):
        str_yago = year_before.strftime("%Y-%m-%d")

        session = Session(engine)
        date_temp_date = session.query(Measurement.date, Measurement.tobs, Measurement.station).\
            filter(Measurement.date.between(str_yago, start)).all()
   
        all_temp = []
        for date, tobs, station in date_temp_date:
            temp_dict = {}
            temp_dict["Date"] = date
            temp_dict["Temp (*F)"] = tobs
            temp_dict["Station"] = station

            all_temp.append(temp_dict)

        return jsonify(all_temp)
    
    elif start_date > datetime(2017, 8, 23):
        return f"start date be between '2011-01-01'and '2017-08-23'"

    elif year_before < datetime(2011, 1, 1):
        return f"start date be between '2011-01-01'and '2017-08-23'"
    
    


@app.route("/api/v1.0/<start>/<end>")
def datebetween(start, end):
#    session = Session(engine)
    return "This is in progress start, end"
if __name__ == '__main__':
    app.run(debug=True)
        