# Project 3


### Contents:
- [Problem Statement](#Problem-Statement)
- [Data Dictionary](#Data-Dictionary)
- [Brief Summary of Analysis](#Brief-Summary-of-Analysis)
- [Abstract Summary](#Abstract-Summary)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)


## Problem Statement



## Why is this important?

The accurate determination of occupancy detection in buildings has been recently estimated to save energy in the order of 30 to 42% *[12–14]*. Experimental measurements reported that energy savings were 37% in *[15]* and between 29% and 80% *[16]* when occupancy data was used as an input for HVAC control algorithms. Nowadays, with the affordability of sensors increasing and becoming more ubiquitous, together with affordable computing power for automation systems it makes the determination of occupancy a very promising approach to lower energy consumption by appropriate control of HVAC and lighting systems in buildings. Other applications for occupancy detection include security and determination of building occupant behaviors. A system that could accurately detect the presence of the occupants without using a camera is very interesting due to privacy concerns.

## Data Dictionary

|Feature Name|Feature Description|Units of Measurement|
|---|---|---|
|date|time the observation was recorded|year-month-day hour:minute:second|
|temperature|temperature recorded|Celsius|
|humidity|relative humidity recorded|%|
|light|light recorded at time of observation|Lux|
|co2|CO2 measured at the time of observation|ppm, parts per million|
|humidity_ration|derived quantity from temperature and relative humidity|kgwater-vapor/kg-air|
|occupancy|status of room occupancy|0 for not occupied, 1 for occupied status|
|weekday|indicates if the timestamp is weekday or weekend| 1 for weekday, 0 for weekend|

## Brief Summary of Analysis


![Fig1]()

<div>
<img src="" width="400"/>
</div>

When comparing/evaluating models, we need to be familiar with a few metrics.  

**Sensitivity** measures the proportion of positives that are correctly identified.  
**Specificity** measures the proportion of negatives that are correctly identified.  
**Accuracy** tells us about the number of correctly classified data points with respect to the total data points. As the name suggests, accuracy talks about how close the predicted values are to the target values.  
**Precision** expresses the proportion of the data points our model says was relevant actually were relevant.

Below is a summary of scores for each of the models created for this purpose.

<br>

|Abbreviation|Meaning|
|---|---|

<br>

In our case, we are aiming to classify posts as accurately as possible, so we have chosen to optimize for accuracy. The best model in this case is the first model with highest accuracy of 93%.

The parameters used for our best model:  

|Parameter Name|Parameter Value|
|---|---|

<br>


## Abstract Summary

The accuracy of the prediction of occupancy in an office room using data from light, temperature, humidity and CO2 sensors has been evaluated with different statistical classification models using Python. Three data sets were used in this work, one for training, and two for testing the models considering the office door opened and closed during occupancy. The datasets were combined into one large dataset. The data was cleaned, and exploratory data analysis was performed on it. The models were trained on a split of 75% train to 25% test of the combined dataset. The data sets provided for testing, with door open and door closed, were used to generate predictions and further evaluate the models.

Typically the best accuracies (ranging from 95% to 99%) are obtained from training Linear Discriminant Analysis (LDA), Classification and Regression Trees (CART) and Random Forest (RF) models. The results show that a proper selection of features together with an appropriate classification model can have an important impact on the accuracy prediction. Information from the time stamp has been included in the models, and usually it increases the accuracy of the detection. Interestingly, using only one predictor (temperature) the LDA model was able to estimate the occupancy with accuracies of 85% and 83% in the two testing sets.


## Conclusions and Recommendations

**Conclusions:**  


**Next steps:**  


**Resources:**

(1) [Sensitivity and Specificity](https://en.wikipedia.org/wiki/Sensitivity_and_specificity)  
(2) [Accuracy](https://towardsdatascience.com/how-to-evaluate-machine-learning-model-performance-in-python-135b4ae27f7e)  
(3) [Precision](https://towardsdatascience.com/beyond-accuracy-precision-and-recall-3da06bea9f6c)  
(4) [Executive Summary](https://unilearning.uow.edu.au/report/4bi1.html)  
(5) [How to Predict Room Occupancy Based on Environmental Factors](https://machinelearningmastery.com/how-to-predict-room-occupancy-based-on-environmental-factors/)  
(6) [Technical Report and Project](https://github.com/CristinaSahoo/Capstone.git)  
(7) [Improving Prediction of Office Room Occupancy Through Random Sampling](https://www.datasciencecentral.com/m/blogpost?id=6448529%3ABlogPost%3A508623)  
(8) [Occupancy](https://www.scikit-yb.org/en/latest/api/datasets/occupancy.html)  
(9) [Room Occupancy Detection](http://www.renom.jp/notebooks/tutorial/clustering/occupancy-detection/notebook.html)  
(10) [Classroom Occupancy Project](https://www.slideshare.net/mobile/MengdiYue/classroom-occupancy-project)  
(11) [Accurate occupancy detection of an office room from light, temperature, humidity and CO2 measurements using statistical learning models. Luis M. Candanedo, VÃ©ronique Feldheim. Energy and Buildings. Volume 112, 15 January 2016, Pages 28-39.](https://drive.google.com/drive/folders/1tlRKY3LTSvG7gLD5eubW2i3sAtZtVfMh?usp=sharing)  
(12) [Calculate day in the past](https://www.calculator.net/day-of-the-week-calculator.html?today=02%2F07%2F2015&x=78&y=24)  
(13) [V.L.Erickson, M.Á.Carreira-Perpinán, A.E.Cerpa, OBSERVE:Occupancy-based system for efficient reduction of HVAC energy, in: Proceedings of the 10th International Conference on, IEEE, Information Processing in Sensor Networks (IPSN), Chicago, IL, 2011, pp. 258–269.](http://refhub.elsevier.com/S0378-7788(15)30435-7/sbref0200)  
(14) [V.L.Erickson, M.Á.Carreira-Perpinán, A.E.Cerpa,Occupancy modeling and prediction for building energy management, ACM Trans. Sensor Netw. (TOSN) 10 (3) (2014) 42.](http://refhub.elsevier.com/S0378-7788(15)30435-7/sbref0205)  
(14) Dong B., Andrews B., (2009). Sensor-based occupancy behavioral pattern recognition for energy and comfort management in intelligent buildings. Proceedings of Building Simulation.  
(15) [J. Brooks, S. Goyal, R. Subramany, Y. Lin, T. Middelkoop, L. Arpan, L. Carloni, P. Barooah, An experimental investigation of occupancy-based energy-efficient control of commercial building indoor climate, in: Proceeding of the IEEE 53rd Annual Conference on, IEEE, Decision and Control (CDC), Los Angeles, CA, 2014, pp. 5680–5685.](http://refhub.elsevier.com/S0378-7788(15)30435-7/sbref0215)  
(16) [J. Brooks, S. Kumar, S. Goyal, R. Subramany, P. Barooah, Energy-efficient control of under-actuated HVAC zones in commercial buildings, Energy Build. 93 (2015) 160–168.](http://refhub.elsevier.com/S0378-7788(15)30435-7/sbref0220)  


**Data Sources:**  

(1) [Occupancy Detection Dataset](http://archive.ics.uci.edu/ml/datasets/Occupancy+Detection+#)