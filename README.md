# A Diabetes Diagonistic App Implemented Using Decision Tree Classifier.

## This made use of a collection of data obtained from the laboratory of Medical City Hospital  and the Specialist Center for Endocrinology and Diabetes-Al-Kindy Teaching Hospital,Iraq, spanning various column features<hr>

Below is a step-wise treatise on how a tactful feature engineering was carried out before relevant columns were selected such as age,urea level,creatinine ratio,cholesterol level,low density lipoprotein and body mass index:

Imported dependencies<br>
Imported dataset<br>
Visualized the first 5 rows to have an idea of the inherent features and inputs<br>
Generated an informative overview of the columns as well as data types<br>
Plotted a statistical analytics of the dataset<br>
Observed the components of the target features and modified the provisions into appropriate "diabetic", "non-diabetic" and "predicted diabetic" occurencies<br>
Dropped the insignificant ID column<br>
Checked for null values<br>
A link to the below analysis with visualization would be provided somewhere below as you read along<br>
Visualized the target "class" features to realise the inherent uneven diatribution of values<br>
Plotted "cholesterol" feature against "low density lipoprotein" and found that low density lipoprotein increased with cholesterol levels<br>
Split data into training and test datasets<br>
Installed the imblearn dependency to help strike some balance on the data set using the line: "pip install imblearn"<br>
Observed the balance established above<br>
Train the model - first, using the DecisionTreeClassifier algorithm<br>
Model produced some significantly impressive metric values<br>
Conducted cross validation of data through varying iterations on different portions of the dataset in order to put out biases<br>
Observed the performance at depth value of 16 as provided from the above cross validation<br>
Ultimately wrote a function which encapsulates the predictive system for ease of user reference on the client side<br>
Saved the model<br>
Built an API using python<br>
Built a front-end interface for easy dignosis of potential patients<br>
Deployed entire project to the public domain<br>
More detailed analysis with accomanying visuals can be accessed from the following link below:<br>
<a href="https://github.com/fredie7/diabetes_diagnostics_api/blob/main/Untitled.ipynb">https://github.com/fredie7/diabetes_diagnostics_api/blob/main/Untitled.ipynb</a>
Access the front end interface using the link below:<br>
<a href="https://master--majestic-chimera-35e6a4.netlify.app/">https://master--majestic-chimera-35e6a4.netlify.app/</a>
