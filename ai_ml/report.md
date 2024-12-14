my colab notebook: https://colab.research.google.com/drive/1IihH68oFuQpoPaYBFPwwZ380gRJpHI-U?usp=sharing

dataset used: https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023/data

i tried cleaning and preprocessing the data, but later found that it only decreases my model performance as data was already clean so instead i used the raw data

results: using logistic regression

confusion matrix: [[55581  1169],[ 3336 53640]]

auc = 0.99

also performed shap analysis

fastapi implementation sumbmitted seperately

did not implement other algorithms except logistic regression and random forest due to time constraints
