# A Diabetes Diagonistic App Implemented Using Decision Tree Classifier.

## This made use of a collection of data obtained from the laboratory of Medical City Hospital  and the Specialist Center for Endocrinology and Diabetes-Al-Kindy Teaching Hospital,Iraq, spanning various column features

Below is a step-wise treatise on how a tactful feature engineering was carried out before relevant columns were selected such as age,urea level,creatinine ratio,cholesterol level,low density lipoprotein and body mass index:

*Imported dependencies
*Imported dataset
*Visualized the first 5 rows to have an idea of the inherent features and inputs
*Generated an informative overview of the columns as well as data types
*Plotted a statistical analytics of the dataset
*Observed the components of the target features and modified the provisions into appropriate "diabetic", "non-diabetic" and "predicted diabetic" occurencies
*Dropped the insignificant ID column
*Checked for null values
*A link to the below analysis with visualization would be provided somewhere below as you read along
*Visualized the target "class" features to realise the inherent uneven diatribution of values
*Plotted "cholesterol" feature against "low density lipoprotein" and found that low density lipoprotein increased with cholesterol levels
*Split data into training and test datasets
*Installed the imblearn dependency to help strike some balance on the data set using the line: "pip install imblearn"
*Observed the balance established above
*Train the model - first, using the DecisionTreeClassifier algorithm
*Model produced some significantly impressive metric values
*Conducted cross validation of data through varying iterations on different portions of the dataset in order to put out biases
*Observed the performance at depth value of 16 as provided from the above cross validation
* Ultimately wrote a function which encapsulates the predictive system for ease of user reference on the client side
*Saved the model
*Built an API using python
*Built a front-end interface for easy dignosis of potential patients
*Deployed entire project to the public domain
*More detailed analysis with accomanying visuals can be accessed from the following link below:
<a href="https://github.com/fredie7/diabetes_diagnostics_api/blob/main/Untitled.ipynb">https://github.com/fredie7/diabetes_diagnostics_api/blob/main/Untitled.ipynb</a>
*Access the front end interface using the link below:
<a href="https://master--majestic-chimera-35e6a4.netlify.app/">https://master--majestic-chimera-35e6a4.netlify.app/</a>
