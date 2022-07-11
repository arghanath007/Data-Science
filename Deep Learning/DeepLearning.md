***To Open Anaconda Navigator on Linux run 'anaconda-navigator' in the terminal.***

# Motto of Deep Learning or AI in general

> If in doubt, run the code.
## Explore and experiment

> Experiment, Experiment and lots of experiments.
> Visualize, Visualize and lots of visualizations.(Recreate things in ways we can understand them)
> Ask questions and ask lots of questions.(Even dumb questions)
> Share your work, and try explaining it to someone else.



## Why Deep Learning?

1) For a given complex problem, it is probably not possible to think of all the possible rules for it. 
    **Example**: When we are trying to teach a self-driving car to drive. We have to think of all the rules we have to code here for it to work.

**We can think of Logistic Regression as a simple single neuron.***
>The input parameter or the independent variable is called a feature in the Machine Learning terminology. 'Age' is the independent variable here.
		
>Dependent variable is if person will buy insurance or not.

*Dense Layer of Network* -> Every neuron is connected with every other neuron in the hidden layer.

model=keras.Sequential([
    keras.layers.Dense(10, input_shape=(784), activation='sigmoid')  
])
	-> '10' is the number/count of outputs we have, '784' is the number/count of inputs we have in this neural network. The activation function we are using here is the 'sigmoid' function.


>cm=tf.math.confusion_matrix(labels=y_test,predictions=y_predicted_labels) -> 'y_test' is the truth data, 'y_predicted_labels' is the predicted data.

>If we have value between +ve infinity to -ve infinity then it is hard to make a decision on the classification problem and if we have values between 0 and 1 then it is far more easier to make a decision on the classification problem. For this only, the 'sigmoid' function is called as the 'activation' function, which means it will decide wheather the neuron is firing or not firing. When the neuron is firing then it is saying that the person will buy the insurance. When the neuron is not firing then it is saying that the person will not buy the insurance. So we can see that having a 'sigmoid' or an activation function is helpful in the output layer.
	
>The complex problems cannot be solved by linear equations. The patterns we see in the universe cannot be explained by linear equations all the time, that's why we need non-linear equations and the 'activation' function will help us build that non-linear equation.


**GENERAL GUIDE LINE for ACTIVATION FUNCTIONS**  -> Use 'sigmoid' in output layer. All other places try to use 'tanh' if possible. 'tanh' will canculate a mean of '0' and it will center the data so it is useful.

## Issues with sigmoid and tanh:-

1)Vanishing Gradients(derivatives) -> (Gradient Descent Video)We need to calculate derivatives and back propagate the errors. If the derivates are closing too '0' or zero then the learning becomes extremely slow. This is called as the vanishing gradients problem. 
	For this reason, they came up with a new function called as 'ReLU'. If the value is less than zero, then the output is zero(0). If the value is more than zero, then the output is same as the value. Eg:- if we feed '2' as the input to the 'ReLU' function then we will get '2' as the output. If we feed '-1' as the input to the 'ReLU' function then we will get '0' as the output.


**GUIDELINES FOR HIDDEN LAYERS** -> For hidden says, if we are not sure which activation function to use, then just use 'ReLU' as the default choice. Expecially for hidden layers.

ReLU(z)=max(0,x).

*ReLU* -> It also have 'Vanishing Gradients' problem when the values are less than zero. For these there is another flavour of 'ReLU' which is called as the 'Leaky ReLU'. Leaky ReLU(z)= max(0.1x,x) ['x' is the input value.]

**Loss is used in neural network training.**

**Gradient Decent Function helps us to find the weights(Co-effecient) which are w1,w2 and bias(Intercept).**

## CHAIN RULE:
	
	In back propogation algorithms, there is a forward pass as well as a backward pass. In the forward pass we get the value of loss and when we get the loss we back propogate to adjust the weights.
    
 
>FOR THE DOG CLASS:(Where we were predicting which images are the images of the dog. We have 7 predictions for the dog class)

## PRECISION: 
    For example, we are using a Dog classification problem, where we are prediciting if the image is an image of a Dog or not.
        True Positive(TP)=4(This are the ones that the model predicted to be dog images and they were actually dog images i.e correct prediction by the model)
        
        False Positive(FP)=3(This are the ones that the model predicted to be dog images and they were not dog images i.e incorrect prediction by the model)
    
        Precision -> Precision is out of all the dog predictions, how many did the model got correct result?
        Precision=4/7=0.57
                 =TP/(TP+FP)
                 
         For precision, think about predictions as the base
                 
## RECALL:
    When we thing about Recall, we always think about truth as the baseline.
    
    Total Dog truth samples(FN)=6(This are the total count of dog images that were present in the dataset).
    
    Truth Positive(TP)=4(This are the ones that the model predicted to be dog images and they were actually dog images i.e correct prediction by the model)
    
    Recall -> Recall is out of all dog truth, how many you got it right.
    
    Recall=4/6=0.67
          =TP/(TP+FN)
          
    For recall, think about truth as the base  
    
    
FOR THE NOT DOG CLASS:(Where we were predicting which images are not the images of the dog. We had 3 predictions in the not dog class)

## NEURAL NETWORKS


Neural networks are used to handle the variety in your inputs, such that it can classify those variety of inputs in a generic way. Here, the first part where we use convolutional convolution operation is 'feature extraction' part and the second part, where we are using dense neural network is called 'classification' because the first part is detecting all the features ears nose eyes head and body etc. The second part is responsible for 'classification'.

Max pooling along with CNN helps with position invariant feature detection. Doesn't matter where the eyes or ears are in the image, it will detect that feature for us.

Max pooling is more generally used but sometimes people use average pooling.

The beauty of CNN is that, it will automatically detect the filters(Eye,Nose,ears) on its own and that is part of the training, so when the neural network(CNN) is training. We are supplying images,koala images here, and using that it will use back propagation and it will figure out the right amount of filters and it will figure out the values in these filters. This is all part of the learning or the back propagation.
    As a hyper-parameter we want to specify how many filters we want and what is the size of each of those filters, that's it. We do not specify the exact values within these filters, the network will learn those on it's own. 


## Difference between 'sparse_categorical_crossentropy' and 'categorical_crossentropy':-

>When we have 'y' values as 'one hot encoded vector', we will use 'categorical_crossentropy'.

>If we have 'y' directly as a value(y=8) then, we will use 'sparse_categorical_crossentropy'.


## Tensor

> It is a way to represent some sort of data in numerical form.


## Neural Network

**Typical Workflow in building a model**

> Build a model -> fit the model -> evaluate the model -> tweak the model -> fit it -> evaluate it ->  tweak it -> fit it -> evaluate it -> repeat...


### Building a model

> Experiment, Experiment, Experiment

### Model Training

#### Improving a model

> "Learning_rate" or 'lr' is potentially the most important hyper-parameter that we can change in the training of a neural network. It is the most important hyper-parameter of many different neural networks.


### Evaluating a model

> Visualize, Visualize, Visualize




# Tensorflow Certification Course

> 2. Deep Learning and TensorFlow Fundamentals(Completed)

> 3. Neural network regression with TensorFlow(Completed)

> 4. Neural network classification in TensorFlow

> Start from Video 2

