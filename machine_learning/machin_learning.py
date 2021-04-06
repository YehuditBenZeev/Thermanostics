from sklearn.metrics import confusion_matrix
from sklearn.metrics import auc
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt


class Machine:
    def __init__(self, array_image):
        self.array_image = array_image
        self.array_l = []  # array of label
        self.array_p = []  # array of prediction

    def array_label(self):
        latter = "S"
        for word in self.array_image:
            if latter in word:
                self.array_l.append("sick")
            else:
                self.array_l.append("healthy")

    def array_predict(self, value_model):
        i = 0
        num_of_hotpoint = [7, 9, 20]
        for word in self.array_image:
            # num_of_hotpoint = 11 # "num_hotpoint": we need to write function that return for all picture how much point black
            if num_of_hotpoint[
                i] > value_model:  # I predict that if there are more than value_model hot spots then the person is sick - positive
                i += 1
                self.array_p.append("sick")
            else:
                self.array_p.append("healthy")

    def conf_matrix(self):
        print(self.array_l, self.array_p)
        tn, fp, fn, tp = confusion_matrix(self.array_l, self.array_p, labels=["sick", "healthy"]).ravel()
        print(tn, fp, fn, tp)
        score = np.array([0.3, 0.2, 0.4])
        fpr, tpr, threshold = metrics.roc_curve(self.array_l, score, pos_label="sick")
        print(fpr, tpr, threshold)
        auc(fpr, tpr)
        plt.figure()
        plt.plot(fpr, tpr, color='r')
        plt.plot(fpr, tpr, 'bo')  # Highlights the dots in blue
        plt.xlabel("---")
        plt.ylabel("---")
        plt.show()
    # def div_train_test(self):
    #     x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)