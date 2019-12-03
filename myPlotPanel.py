import statsmodels.api as sm

def plotPanel(data,ax,trialCondition,label_all=False):
    # Extract the subset of the data corresponding to vestibular-only stimulation
    # and recordings from V1
    dataSubset = data.loc[(data["Trial Condition"]==trialCondition) & (data["Region"]=="V1"),:]

    # Plot the spikes counts in Bin(i) as a function of the absolute value of
    # the stimulation speed
    ax.scatter(x=abs(dataSubset["Speed"]), y=dataSubset["Bin(i)"], c="lightgray")
    ax.set_title(trialCondition)

    # Estimate the regression line
    regressors = sm.add_constant(abs(dataSubset["Speed"]))
    # fit.params contains the regression coefficients
    # fit.pvalues contains the regression coefficients pvalues
    fit = sm.OLS(endog=dataSubset["Bin(i)"], exog=regressors).fit()

    # Plot the regression line
    legend = "p={:.4f}".format(fit.pvalues[1])
    ax.plot(abs(dataSubset["Speed"]), fit.params[0]+abs(dataSubset["Speed"])*fit.params[1], color="red", label=legend)
    ax.legend(loc="upper left")

    ax.set_title(trialCondition)
    if label_all:
        ax.set_xlabel("Abs(Speed)")
        ax.set_ylabel("Spike Count")