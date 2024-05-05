def model_predict_proba(data_asarray):
    data_asframe = pd.DataFrame(data_asarray, columns=X_train.columns)
    proba = lr_pipeline.predict_proba(data_asframe)
    return proba[:, 1]

explainer = shap.Explainer(model_predict_proba, X_train)
shap_values = explainer.shap_values(X_test)
explainer_x_test = explainer(X_test)