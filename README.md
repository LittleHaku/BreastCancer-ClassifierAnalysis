# BreastCancer-ClassifierAnalysis
This Bachelor thesis presents a comparative analysis of base and ensemble classifiers for breast cancer detection. The classifiers are used to analyze the results from fine needle aspiration biopsies and classify the samples as benign or malignant. The use of Artificial Intelligence (AI) is crucial in this process. A specific type of AI, known as eXplainable AI (XAI), is employed to interpret the results.

The initial phase involves constructing and optimizing the classifier models. These classifiers will analyze the results from fine needle biopsy aspirations and classify the samples as benign or malignant. Following this, a performance comparison is conducted using metrics such as the F1 score and recall. The aim is to identify the best classifier based on these metrics.

Once the best classifier model is found, we dive deeper into it to understand how it works. For this, we will use SHAP (SHapley Additive exPlanations), a method of XAI that allows us to see the importance of each feature and how they contribute to the final decision of the model. This will allow us to not only classify the samples but also to understand why the model has made that decision, which can be a step forward in understanding AI models for medical purposes.

Lastly, to display all the results from the classifiers and the XAI analysis, a web application is developed. This application will contain the resulting metrics from the classifiers as well as examples of how each classifier made some of its decisions and which features were the most important.

[Breast Cancer Classification Web](https://breastcancerclassifiers.up.railway.app/) (if it doesn't load due to free hosting, the repo with the website is available [here](https://github.com/LittleHaku/breast-cancer-classification-web))
