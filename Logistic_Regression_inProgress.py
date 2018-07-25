import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import random



def generate_data():
    '''This function generates data by drawing an image that is made of two classes of objects "ash" and "not-ash" and returns the pixel values in array X and the labels for the pixel values in array y'''
    
    #Draws image with colors for non-ash objects
    img = Image.new('RGB', (50, 50), color = (random.randint(0,256), random.randint(0,256), random.randint(0,256)))
    d = ImageDraw.Draw(img)
    
    #Intialize counter variables
    count =0
    countx=0
    county=0
   
    #Load image
    pixy = img.load()
   
    #Intialize arrays
    nonash_pixel_array = np.array([])
    ash_pixel_array = np.array([])
    
    #Draw ash
    for count in range(10):
        xS = random.randint(0,50)
        xE = random.randint(0,50)
        yS = random.randint(0,50)
        yE = random.randint(0,50)
        gray = random.randint(100,255)
        while(xE<=xS):
            if (countx>50):
                xE = random.randint(0,50)
                countx=0
            xS = random.randint(0,50)
            countx+=1
        while(yE<=yS):
            if (county>50):
                yE = random.randint(0,50)
                county=0
            county+=1    
            yS = random.randint(0,50) 
        for x in range(xS,xE,20):
            for y in range (yS,yE,20):
                pixy[x,y]= (gray,gray,gray)
                ash_pixel= np.array(pixy[x,y])
                ash_pixel_array = np.append(ash_pixel_array, ash_pixel)
    
    #Reformat non- ash pixels 
    ash_array  = np.delete(ash_pixel_array, slice(None,None,3))
    ash_array = np.delete(ash_pixel_array,np.arange(0,ash_pixel_array.size,3))  
    ash_array  = ash_array.reshape(-1, 2)
    
    #Record values of all pixels 
    for x in range(0,50,20):
        for y in range (0,50,20):
            nonash_pixel  = np.array(pixy[x,y])
            nonash_pixel_array  = np.append(nonash_pixel_array,nonash_pixel)
            
    #Reformat non-ash pixels
    nonash_array = np.delete(nonash_pixel_array, slice(None,None,3))
    nonash_array = np.delete(nonash_pixel_array,np.arange(0,nonash_pixel_array.size,3))  
    nonash_array =  nonash_array.reshape(-1, 2)
   
    #Create Labels 
    nonash_labels = [1] * len(nonash_array)
    nonash_labels = np.array(nonash_labels)
    ash_labels = [0] * len(ash_array)
    ash_labels = np.array(ash_labels)
    
    #Concatenate arrays into an array for pixels and an array for labels
    X_before = np.concatenate((ash_array, nonash_array), axis=0)
    X = X_before/255
    y = np.concatenate((ash_labels,nonash_labels),axis=0)
    print(X)
    print(y)
    


    return X, y


def visualize(X, y, clf):
    plt.scatter(X[:, 0], X[:, 1], s=40, c=y, cmap=plt.cm.Spectral)
    plt.show()
    plot_decision_boundary(lambda x: clf.predict(x), X, y)
    plt.title("Logistic Regression")
    

def plot_decision_boundary(pred_func, X, y):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole gid
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    plt.show()


def classify(X, y):
    #Use a logistic regression model to classify data
    clf = linear_model.LogisticRegressionCV()
    clf.fit(X, y)
    return clf

def predict(X,y):
    ''' This function returns a predicted value for a given data point where [0] corresponds to red and [1] corresponds to blue'''
    clf = linear_model.LogisticRegressionCV()
    clf.fit(X, y)
    #Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
    data = np.array([.6,.5])
    data = data.reshape(1, -1) 
    prediction = clf.predict(data)
    return p 

def main():
    prediction_list = []
    X, y = generate_data()
    for i in range(0,1,10):
        clf = classify(X, y)
        visualize(X, y, clf)
        predict = predict(X,y)
        prediction_list =[predict] + prediction_list
        print(prediction_list)
    return prediction_list
        
    

if __name__ == "__main__":
   main() 
