# This is a plan for the environmental monitoring of the Warm Emanation System
# with the goal of mitigating gain shift in the data and better our analysis.
# 
# This monitoring will be used to monitor the change in gain in relation to the
# change in temperature and relative humidity, as well as monitor the
# if the changes we make are effective
#
# Joseph ordered a Metro M7 microcontroller and a DHT20 Temperature Sensor
# for this purpose. These electronics support the CircuitPython language.
#
# The sensor will record tempearature and rel. humidity near the WES detector,
# as the environmental data gathered from the Tabletop System has been 
# determined to be less than ideal for our purposes. The data from this sensor
# will be continuous over the length of all emanation runs, unlike the TT data
# and will not suffer from the sunlight issue the TT Temperature sensors 
# suffered from, or the dependency upon the air coming from the Rn clean room
# that the TT RH sensors suffered from.
#
# The sensor will likely be located near the detector or near the cables, where
# It could be sensitive to any ambient heat propagating from the Rn Mitigation
# room, or the computer, or the environment.
#
# The python code will later display the graphs of the temperature against the
# gain shift, as well as the analyses of these graphs.
