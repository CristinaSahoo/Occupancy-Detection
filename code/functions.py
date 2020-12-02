import string
import numpy as np
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

def round_up_time(timestamp):
    if ':59:59' in timestamp:
        hour = np.str(np.int(timestamp[11:13]) + 1)
        if len(hour) == 1:
            timestamp = timestamp[0:11] + '0' + hour + ':00:00'
        if len(hour) == 2:
            timestamp = timestamp[0:11] + hour[0] + hour[1] + ':00:00'
        return timestamp
    elif ':59' in timestamp[16:]:
        minutes = np.str(np.int(timestamp[14:16]) + 1)
        if len(minutes) == 1:
            timestamp = timestamp[0:14] + '0' + minutes + ':00'
        if len(minutes) == 2:
            timestamp = timestamp[0:14] + minutes[0] + minutes[1] + ':00'
        return timestamp
    return timestamp