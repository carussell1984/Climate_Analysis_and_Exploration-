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
                f"<strong>Available Routes:</strong><br/>"
                f"<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp<strong>(i)</strong> /api/v1.0/precipitation:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspWill return the date and the preciption values.<br/>"
                f"<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp<strong>(ii)</strong> /api/v1.0/stations:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspWill provide a list of stations from the dataset.<br/>"
                "<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp<strong>(iii)</strong> /api/v1.0/tobs:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspWill return the dates and temperature observations within a year from the last data point.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp<strong>(iv)</strong> /api/v1.0/&ltstart&gt:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspWill return the minumum temperature, maximum temperature, and the average temperature for dates equal to and greater than the search query<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp(up until 2017-08-23).<br/>"
                f"<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp<strong>(v)</strong> /api/v1.0/&ltstart&gt/&ltend&gt:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspWill return the minimum temperature, the average temperature, and the max temperature between and including the dates provided.<br/><br/>"
                f"Please refer to the set of instructions below when performing temperature data queries by start date or by start/end date:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.<br/><br/>")


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

@app.route("/api/v1.0/tobs")
def tobs():



    session = Session(engine)

    tobs_data = session.query(Measurement.date, Measurement.tobs, Measurement.station).\
            filter(Measurement.date >= "2016-08-23").all()

    all_tobs = []
    for date, tobs, station in tobs_data:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Temp Obs"] = tobs
        tobs_dict["Station"] = station

        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def above_date(start):
    
    try:    
        
        query_date =  datetime.strptime(start,"%Y-%m-%d").date()
    
    except ValueError:
        return (f"Your entry failed to return a search. Please check your entry and try again.<br/>"
                f"Please refer to the set of instructions below:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.<br/><br/>"
                f"To receive a list of stations the route is: /api/v1.0/stations<br/>"
                f"To receive a precipation data the route is: /api/v1.0/precipitation<br/>")

        
    if query_date >= datetime.strptime("2017-08-24","%Y-%m-%d").date():
        return (f"Your entry failed to return a search. Please check your entry and try again.<br/>"
                f"Please refer to the set of instructions below:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.")
        
    elif query_date <= datetime.strptime("2009-12-31","%Y-%m-%d").date():
        return (f"Your entry failed to return a search. Please check your entry and try again.<br/>"
                f"Please refer to the set of instructions below:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.")
        
        
    else: 
        query_date =  datetime.strptime(start,"%Y-%m-%d").date()
        session = Session(engine)
        sel = [func.max(Measurement.tobs), func.avg(Measurement.tobs), func.min(Measurement.tobs)]
        temp_post_date = session.query(*sel).filter(Measurement.date >= query_date).all()


        temp_data_post = []
        for tmax, tavg, tmin in temp_post_date:
            temp_dict = {}
            temp_dict["Temp (max)"] = tmax
            temp_dict["Temp (avg)"] = tavg
            temp_dict["Temp (min)"] = tmin

            temp_data_post.append(temp_dict)

        return jsonify(temp_data_post)
    


@app.route("/api/v1.0/<start>/<end>")
def tempbetweendates(start, end):

    try:    
        start_dt = datetime.strptime(start, "%Y-%m-%d").date()
        end_dt = datetime.strptime(end, "%Y-%m-%d").date()
    
    except ValueError:
        return (f"Your entry failed to return a search. Please check your entry and try again.<br/>"
                f"Please refer to the set of instructions below:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date and end between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.<br/><br/>")
                

    if start_dt > end_dt:
        return (f"start date must be earlier than end date"
                f"Please refer to the set of instructions below:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date and end between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.<br/><br/>")

    elif start_dt >= datetime.strptime("2017-08-24","%Y-%m-%d").date():
        return (f"Your entry failed to return a search. Please check your entry and try again.<br/>"
                f"Please refer to the set of instructions below:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.")
        
    elif start_dt <= datetime.strptime("2009-12-31","%Y-%m-%d").date():
        return (f"Your entry failed to return a search. Please check your entry and try again.<br/>"
                f"Please refer to the set of instructions below:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.")

    elif end_dt >= datetime.strptime("2017-08-24","%Y-%m-%d").date():
        return (f"Your entry failed to return a search. Please check your entry and try again.<br/>"
                f"Please refer to the set of instructions below:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.")
        
    elif end_dt <= datetime.strptime("2009-12-31","%Y-%m-%d").date():
        return (f"Your entry failed to return a search. Please check your entry and try again.<br/>"
                f"Please refer to the set of instructions below:<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Enter a start date between the dates of '2010-01-01' and '2017-08-23'.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Dates must be in YYYY-MM-DD format.<br/>"
                f"&nbsp&nbsp&nbsp&nbsp&nbsp* Do not preceed or end the date with either  '  or  '""' symbols.")
    
    else:
        
        session = Session(engine)
    
        temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
             filter(Measurement.date >= start_dt).\
             filter(Measurement.date <= end_dt).all()

        temp_data_between = []
        for tmax, tavg, tmin in temp_data:
            temp_dict_2 = {}
            temp_dict_2["Temp (max)"] = tmax
            temp_dict_2["Temp (avg)"] = tavg
            temp_dict_2["Temp (min)"] = tmin

            temp_data_between.append(temp_dict_2)

        return jsonify(temp_data_between)


    
if __name__ == '__main__':
    app.run(debug=True)
        