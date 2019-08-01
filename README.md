# Climate_Analysis_and_Exploration

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.
<div> 
<hr2><Strong>Step 1: Use Python and SQL Alchemy to do basic Climate Analysis and Database Exploration.</Strong></hr2>
  <p>Use the provided starter notebook and hawaii.sqlite files.</p>
  <p>Choose a start date and an end date for your trip, 3 - 15 days long.</p>
  <p>Use SQLAlchemy <code>create_engine</code>to connect to your sqlite database.</p>
  <p>Use SQLAlchemy <code>automap_base()</code> to reflect your tables into classes and save a reference to those classes called Station and     Measurement.</p>
</div> 
<div> 
<hr2><Strong>Step 2: Perform Precipitation Analaysis</Strong></hr2>
 <p>Design a query to retrieve the last 12 months of precipitation data.</p>
 <p>Select only the date and prcp values.</p>
 <p>Load the query results into a Pandas DataFrame and set the index to the date column.</p>
 <p>Sort the DataFrame values by date.</p>
 <p>Plot the results using the DataFrame plot method.</p>
 <p>Use Pandas to perform statistical analysis on the precipitation data.</p>
 </div> 
 <div> 
 <hr2><Strong>Step 3: Station Analysis:</Strong></hr2>
  * Design a query to calculate the total number of stations.
  * Design a query to find the most active stations.
  * Design a query to retrieve the last 12 months of temperature observation data (tobs)
 </div> 
 <div> 
 <hr2><Strong>Step 4: Daily Normals</Strong></hr2>
 </div> 
 <hr2><Strong>Step 5: Temperature Analysis - Daily Normals</Strong></hr2> 
  <div>
  <strong>Part 1</strong>
  * use the <code>calc_temps</code> to accept a start date and an end date in the format <code>%Y-%m-%d</code> and return the minimum, average, and maximum temperatures for that range of dates
  * use the <code>calc_temps</code> function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year
  * Plot the min, avg, max temperature from your previous query as a bar chart
        - Average temp will be the bar height
        - Yerr will be tmax-tmin
 </div>
  <div>
  <strong>Part 2</strong>
   * Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
   * Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.
   * Use the independant t-test to determine whether the difference in the means, if any, is statistically significant.
  </div>

 
