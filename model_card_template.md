# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a Logistic Regression classifier built by using scikit-learn.
It is trained to predict whether an individual's income exceeds $50,000 per year based
on census demographic data. The model uses one-hot encoding for categorical variables
and was trained using a processed version of UCI Census dataset.
## Intended Use
This model is intended for educational uses to demonstrate how to build, train,
and deploy a machine learning model using a full pipeline. It can be used to
predict income classification based on demographic information. It is not
intended for real-world decision making.
## Training Data
The model was trained on the UCI Census Income dataset. The dataset includes
demographic and employment attributes like age, workclass, education, and more.
## Evaluation Data
The dataset was split into training and testing sets using a train-test split.
The dataset was used to evaluate model performance after training.
## Metrics
_Please include the metrics used and your model's performance on those metrics._
The model was evaluated using the following metrics:\
-Precision: 0.73333\
-Recall: 0.5652\
-F1 Score: 0.6384\
These metrics imply that the model performs moderately well,
with better precision than recall.
## Ethical Considerations
The dataset includes sensitive attributes such as sex, race,
and marital status. These features in a predictive model can potentially
reinforce existing inequalities. Care should be taken when interpreting such
models.
## Caveats and Recommendations
This model is relatively simple and may not capture complex relationships in the data.\
Performance could possibly be improved with feature scaling and hyperparameter tuning.