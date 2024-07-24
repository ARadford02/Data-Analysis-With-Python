import numpy as np

def calculate(x):
    if len(x)==9:
        x_array = np.array(x) #Turn list into np array
        matrix = x_array.reshape((3,3)) #3x3 matrix
    
        #Mean Calculations 
        mean0 = np.mean(matrix,axis=0).tolist()
        mean1 = np.mean(matrix,axis=1).tolist()
        mean2 = np.mean(x_array)
    
        #variance calculations
        var0 = np.var(matrix,axis=0).tolist()
        var1 = np.var(matrix,axis=1).tolist()
        var2 = np.var(x_array)    
    
        #standard deviation calculations
        std0 = np.std(matrix,axis=0).tolist()
        std1 = np.std(matrix,axis=1).tolist()
        std2 = np.std(x_array)
    
        #max
        max0 = np.max(matrix,axis=0).tolist()
        max1 = np.max(matrix,axis=1).tolist()
        max2 = np.max(x_array)
    
        #min
        min0 = np.min(matrix,axis=0).tolist() 
        min1 = np.min(matrix,axis=1).tolist()
        min2 = np.min(x_array)
    
        #sum 
        sum0 = np.sum(matrix,axis=0).tolist()
        sum1 = np.sum(matrix,axis=1).tolist()
        sum2 = np.sum(x_array)
    
        dictionary = {"mean": [mean0,mean1,mean2],
                  "variance": [var0,var1,var2],
                  "standard deviation": [std0,std1,std2],
                  "max": [max0,max1,max2],
                  "min": [min0,min1,min2],
                  "sum": [sum0,sum1,sum2]
                 } #This is the dictionary that will be returned as part of the function 
    else:
        raise ValueError("List must contain nine numbers.")#The error given if list is not 9 numbers long
        
    return dictionary