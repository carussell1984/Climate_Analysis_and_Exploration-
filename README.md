<section>
<div>
<hr1><Strong>Climate Analysis and Exploration Project Overview</Strong></hr1>

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.
</div>

</section>
<section>
<hr/>
<hr1><Strong>Resources for project</Strong></hr1>
<p>The resources folder in the this github repo contain two csv files and one sqlite file. The csv files a visual representation of what is in hawaii.sqlite file.</p>
<p>There is an identical hawaii.sqlite file in the Flask folder that the app.py file uses.</p>
</section>
<hr/>

<section>
<hr/>
<div>
 <hr1><Strong>Climate Analysis and Database Exploration</Strong></hr1>
<p>The following analysis was performed using jupyter notebook in the main in the file "climate_exploration.ipynb" A starter notebook was provided was a template and a guide, "climate_starter.ipynb"
</div>
<hr2><Strong>Step 1-Use Python and SQL Alchemy to do basic Climate Analysis and Database Exploration.</Strong></hr2>
  <br/>
  <p>Use the provided starter notebook and hawaii.sqlite files.</p>
  <p>Choose a start date and an end date for your trip, 3 - 15 days long.</p>
  <p>Use SQLAlchemy <code>create_engine</code>to connect to your sqlite database.</p>
  <p>Use SQLAlchemy <code>automap_base()</code> to reflect your tables into classes and save a reference to those classes called Station and     Measurement.</p>
</div> 
<div> 
<hr2><Strong>Step 2-Perform Precipitation Analaysis:</Strong></hr2>
 <br/>
 <p>Design a query to retrieve the last 12 months of precipitation data.</p>
 <p>Select only the date and prcp values.</p>
 <p>Load the query results into a Pandas DataFrame and set the index to the date column.</p>
 <p>Sort the DataFrame values by date.</p>
 <p>Plot the results using the DataFrame plot method.</p>
 <p>Use Pandas to perform statistical analysis on the precipitation data.</p>
 </div> 
 <div> 
 <hr2><Strong>Step 3-Station Analysis:</Strong></hr2>
  <br/>
  <p>Design a query to calculate the total number of stations.</p>
  <p>Design a query to find the most active stations.</p>
  <p>Design a query to retrieve the last 12 months of temperature observation data (tobs).</p>
 </div> 
 <div> 
 <hr2><Strong>Step 4-Daily Normals:</Strong></hr2>
 <p>Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.</p>
 <p>You are provided with a function called daily_normals that will calculate the daily normals for a specific date. This date string will be in the format %m-%d. Be sure to use all historic tobs that match that date string.</p>
<p>Create a list of dates for your trip in the format %m-%d. Use the daily_normals function to calculate the normals for each date string and append the results to a list.</p>
<p>Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.</p>
<p>Use Pandas to plot an area plot (stacked=False) for the daily normals.</p>
 </div>
 <div>
 <hr2><Strong>Step 5-Temperature Analysis - Daily Normals:</Strong></hr2> 
  <div>
  <strong>Part 1</strong>
  <p>Use the <code>calc_temps</code> to accept a start date and an end date in the format <code>%Y-%m-%d</code> and return the minimum, average, and maximum temperatures for that range of dates.</p>
  <p>use the <code>calc_temps</code> function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year.</p>
  <p>Plot the min, avg, max temperature from your previous query as a bar chart<br/>
        - Average temp will be the bar height<br/>
        - Yerr will be tmax-tmin</p>
 </div>
  <div>
  <strong>Part 2</strong>
   <p>Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?</p>
   <p>Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.</p>
   <p>Use the independant t-test to determine whether the difference in the means, if any, is statistically significant.</p>
  </div>
  </section>
 
 <section>
 <hr/>
 <div>
 <hr1><Strong>Climate API Routes Developed Via Flask</Strong></hr1>
  <p>The app.py file to run flask is in the Flask folder in this github repo.</p>
 </div>
 <div>
 <hr2><Strong>Routes for Climate API</Strong></hr2>
  <p><Strong> Route 1 - Home Page: </Strong>  ("/")
       <summary>
       The pages returns all routes available, search instructions, and what to expect with queries. </summary><p>
  <p><Strong> Route 2 - Precipitation Data: </Strong>("/api/v1.0/precipitation") 
       <summary>
       Converts the query results to a dictionary using the date as the key and the prcp as the value. </summary><p>
  <p><Strong> Route 3 - Data Collection Stations: </Strong> ("/api/v1.0/stations")
       <summary>
       Returns a JSON list of stations from the dataset. </summary><p>
  <p><Strong> Route 4 - Temperature Observations: </Strong>("/api/v1.0/tobs")
       <summary>
       Query the dates and temperatures observations from a year from the last data point. Return a JSON list of Temperature Observations for the previous year </summary><p>
   <p><Strong> Route 5 - Temperature Observations: </Strong> ("/api/v1.0/<start>")
      <p><summary>
      Return a JSON list of the minimum temperature, the average temerature, and the max temperature for a given start date. When give the start only the temp min, max, and average is returned for all dates greater then and equal to the start date </summary><p>
  <p><Strong> Route 6 - Temperature Observations: </Strong> ("/api/v1.0/<start>/<end>")
       <summary>
       Return a JSON list of the minimum temperature, the average temerature, and the max temperature for a given start date and end date, inclusive of the query dates. </summary><p>
   </div>
</section>









