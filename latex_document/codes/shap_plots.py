shap.initjs()

# global feature importance
shap.plots.bar(explainer_x_test, max_display=25)
shap.plots.beeswarm(explainer_x_test, max_display=30, alpha=0.75)

# single feature importance
shap.dependence_plot(feature, shap_values, X_test, alpha=0.65, show=False)
ax = plt.gca()
x = ax.collections[0].get_offsets()[:, 0]
y = ax.collections[0].get_offsets()[:, 1]
regression_model = LinearRegression().fit(x.reshape(-1, 1), y)
x_range = np.linspace(x.min(), x.max(), 100)
y_range = regression_model.predict(x_range.reshape(-1, 1))
plt.plot(x_range, y_range, color='red')

# prediction explanation
shap.plots.waterfall(explainers_x_test[prob][idx], show=False)