# BreastCancer-ClassifierAnalysis
This repository contains the Jupyter Notebook and document for my Bachelor's Thesis, which presents a comparative analysis of base and ensemble classifiers for breast cancer detection. The classifiers analyze fine needle aspiration biopsy results to classify samples as benign or malignant, leveraging the power of Artificial Intelligence (AI) and eXplainable AI (XAI).

## Project Overview

### Classifier Development and Optimization

The initial phase involves constructing and optimizing various classifier models. These classifiers analyze biopsy results and classify samples as benign or malignant. The performance of each classifier is compared using metrics such as the F1 score and recall to identify the most effective model.

### Explainable AI with SHAP

Once the best classifier is identified, we use SHAP (SHapley Additive exPlanations) to interpret its decisions. SHAP allows us to understand the importance of each feature and how they contribute to the model's final decision. This insight is crucial for advancing the understanding and trust in AI models for medical applications.

## Web Application for Results

To display the results from the classifiers and the XAI analysis, a web application is developed. This application features:
- **Project Slideshow:** An informative slideshow on the homepage that provides an overview of the project and its key findings.
- **Classifier Comparison Tool:** An interactive feature that allows you to compare different classifiers side by side.
- **Classifier Metrics:** A comprehensive comparison of the performance metrics for all the classifiers tested.
- **Global Feature Analysis:** Insights from the XAI analysis, showcasing how different features influence the model's predictions.
- **Prediction Examples:** Detailed examples of individual predictions, highlighting how each feature contributed to the final decision.

You can explore the website here [Breast Cancer Classification Web](https://breastcancerclassifiers.up.railway.app/) (if it doesn't load due to free hosting, the repo with the website is available [here](https://github.com/LittleHaku/breast-cancer-classification-web))

## Repository Content

- **Jupyter Notebook**: this file `BreastCancer_Classifier_Comparison.ipynb` contains all the code used to train, optimize and evaluate the classifiers and then apply SHAP on all of them.
- **Thesis Document**: found in `tfg_ivan.pdf`, it contains my Thesis. If you want to see how the LaTeX document is organized and compiled check the directory `latex_document` there is a `makefile` that I'm sure can be useful for many students which have problems compiling the document with the bibliography to use it do:
```bash
make clean && make
```

