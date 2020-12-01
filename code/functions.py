import string
from sklearn import metrics
from sklearn.metrics import confusion_matrix, plot_confusion_matrix

def to_snake_case(name):
    if name == name.upper():
        name = name.lower()
        return name
    if name[0] in string.ascii_uppercase:
        name = name.replace(name[0], name[0].lower())
    for letter in name:
        if letter in string.ascii_uppercase:
            name = name.replace(letter, '_' + letter.lower())
    return name

def get_scores(gs, X_train, y_train, X_test, y_test):
    best_score = gs.best_score_
    train_score = gs.score(X_train, y_train)
    test_score = gs.score(X_test, y_test)
    preds = gs.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(y_test, preds).ravel()
    # Sensitivity
    sensitivity = tp / (tp+fn)
    # Specificity
    specificity = tn / (tn+fp)
    # Precision
    precision = tp / (tp+fp)
    precision = metrics.precision_score(y_test, preds)
    # Accuracy
    accuracy = (tp + tn) / (tn + fp + fn + tp)
    accuracy = metrics.accuracy_score(y_test, preds)
    f1_score = metrics.f1_score(y_test, preds)
    scores_list = [
               round(best_score, 4), 
               round(train_score, 4), 
               round(test_score, 4), 
               round(sensitivity, 4), 
               round(specificity, 4), 
               round(precision, 4), 
               round(accuracy, 4),
               round(f1_score, 4)
              ]
    return scores_list