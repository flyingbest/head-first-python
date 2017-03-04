# Putting it all together

# It's good to share.
# You can put your program on the Web.
# If you develop your program as a Web-based application (or webapp, for short), your program is:
#		Available to everyone who can get to your website
#		In one place on your web server
#		Easy to update as new functionality is needed

# Webapps up Close
# web request, web response, Common Gateway Interface(CGI)

# Design your webapp with MVC(Model-View-Controller)

"""
Now that you have an idea of the pages your webapp needs to provide, your next question should be: what's the best way to build this thing?
Despite this, the general consensus is that great webapps conform to the Model-View-Controller pattern which helps you segment your webapp's code
into easily manageable functional chunks (or components):
	The Model: The code to store(and sometiems process) your webapp's data
	The View: The code to format and display your webapp's user interface(s)
	The Controller: The code to glue your webapp together and provide its business logic

By following the MVC pattern, you build your webapp in such as way as to enable your webapp to grow as new requirements dictate.
You also open up the possibility of splitting the workload among a number of people, one for each component.
"""

# Model your data 
# make a athletemodel.py file.

# View your interface
# YATE folder download. and checking code.

# Control your code
# download webapp folder.
# CGI lets your web server run programs.
# Display the list of athletes.
"""
Recall that all of your CGI scripts nees to reside in the cgi-bin folder on your web server.
creating generate_list.py CGI script sends its data to another program called:
"""

# Test
# $ python3 simple_httpd.py
# check the url in http://localhost:8080

# The dreaded 404 error!
# The 404 error is exactly what you would expect to be displayed in this situation, so your generate_list.py CGI is working fine.
# What's needed is the code to the other CGI script.

# Create another CGI script
# create generate_timing_data.py CGI script

# Enable CGI tracking to help with errors
# import cgitb
# cgitb.enable()

# A small change can make all the difference
# @property - This decorator allows you to access the data returned by "top3()" as if it were a class attribute.
# It's a small change, but it's an important one.
"""
when a change is made to the way a class is used, you need to be careful to consider what impact the change has on existing programs,
both yours ans those written by others.

At the moment, you are the only one using the AthleteList class, so it's not a big deal to fix this.
But imagine if thousands of programmers were using and relying on your code...
"""

# By conforming to the MVC pattern and using CGI, you've built a webapp in such a way that it's easy to extend as new requirements are identified.

