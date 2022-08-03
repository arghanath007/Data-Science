# Deep Learning

***To Open Anaconda Navigator on Linux run 'anaconda-navigator' in the terminal.***

## Why Deep Learning?

1) For a given complex problem, it is probably not possible to think of all the possible rules for it. 
    **Example**: When we are trying to teach a self-driving car to drive. We have to think of all the rules we have to code here for it to work.

## Motto of Deep Learning or AI in general

> If in doubt, run the code.

### Explore and experiment

> Experiment, Experiment and lots of experiments.
> Visualize, Visualize and lots of visualizations.(Recreate things in ways we can understand them)
> Ask questions and ask lots of questions.(Even dumb questions)
> Share your work, and try explaining it to someone else.





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


**GENERAL GUIDE LINE for ACTIVATION FUNCTIONS**  

>Use 'sigmoid' in output layer. All other places try to use 'tanh' if possible. 'tanh' will calculate a *mean* of '0' and it will center the data so it is useful.

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
    
 
*FOR THE DOG CLASS*:
>(Where we were predicting which images are the images of the dog. We have 7 predictions for the dog class)

# NEURAL NETWORKS

## Tensor

> It is a way to represent some sort of data in numerical form.

## Building a model

**Typical Workflow in building a model**

> Build a model -> fit the model -> evaluate the model -> tweak the model -> fit it -> evaluate it ->  tweak it -> fit it -> evaluate it -> repeat...


### Steps to build a model

> Experiment, Experiment, Experiment

### Model Training

#### Improving a model

> "Learning_rate" or 'lr' is potentially the most important hyper-parameter that we can change in the training of a neural network. It is the most important hyper-parameter of many different neural networks.


### Evaluating a model

> Visualize, Visualize, Visualize

**Neural Network** 

> Link(1) -> https://www.youtube.com/watch?v=aircAruvnKk

> Gradient Descent(2) -> https://www.youtube.com/watch?v=IHZwWFHWa-w

> Back-propagation(3) -> https://www.youtube.com/watch?v=Ilg3gGewQ5U

Neural networks are used to handle the variety in your inputs, such that it can classify those variety of inputs in a generic way. Here, the first part where we use convolutional convolution operation is 'feature extraction' part and the second part, where we are using dense neural network is called 'classification' because the first part is detecting all the features ears nose eyes head and body etc. The second part is responsible for 'classification'.

Max pooling along with CNN helps with position invariant feature detection. Doesn't matter where the eyes or ears are in the image, it will detect that feature for us.

Max pooling is more generally used but sometimes people use average pooling.

The beauty of CNN is that, it will automatically detect the filters(Eye,Nose,ears) on its own and that is part of the training, so when the neural network(CNN) is training. We are supplying images,koala images here, and using that it will use back propagation and it will figure out the right amount of filters and it will figure out the values in these filters. This is all part of the learning or the back propagation.
    As a hyper-parameter we want to specify how many filters we want and what is the size of each of those filters, that's it. We do not specify the exact values within these filters, the network will learn those on it's own.



## Weights and Biases

> Weights and biases are present within the layers of the neural network.

### Weights

> It tells us what pixel pattern the neuron on the next layer is picking up.

### Biases

> It tells us how high the weighted sum needs to be before the neuron starts getting meaningfully active.



## Back-propagation

> It is the algorithm for determining how a single training example would like to nudge the weights and biases of the neural network.




# Classification Problem

**Important**

> There evaluation metrics such as *precision*, *recall*, *accuracy*, *f1-score*, *Confusion matrix*, *classification report* are the evaluation metrics of a classification problem.

## PRECISION: 
    For example, we are using a Dog classification problem, where we are predicting if the image is an image of a Dog or not.
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
    
    
*FOR THE NOT DOG CLASS*:

>(Where we were predicting which images are not the images of the dog. We had 3 predictions in the not dog class)


## Precision/recall tradeoff

> We can't have both precision and recall high. If we *increase precision*, it will *reduce recall* and vice versa. This is called the precision/recall tradeoff.

## Difference between 'sparse_categorical_crossentropy' and 'categorical_crossentropy':-

>When we have 'y' or *labels* values as *one hot encoded vector*, we will use 'categorical_crossentropy'.

>If we have 'y' or *labels* directly as a value(y=8) in *integer* format then, we will use 'sparse_categorical_crossentropy'.


**IMPORTANT**

> We have to use *SparseCategoricalCrossentropy()* as the loss function instead of *CategoricalCrossentropy* because the labels(y values) are in *integer* format and not *one-hot-encoded*. 

> If the labels were *one-hot-encoded* then we could have used the *CategoricalCrossentropy* as the loss function here.



# Regression Problem









# Computer Vision

## Definition

> It is the practice of writing algorithms which can discover patterns in visual data. Such as the camera of a self-driving car recognizing the car in front.

### Example

> Teaching Computers to see. Data from a *webcam* or *camera* from a car or a *security camera*.

## Computer Vision Problem

> Anywhere we want a computer to figure out something or understand what's going on a visual scene.

## Convolutional Neural Network (CNN)

> Link -> https://poloclub.github.io/cnn-explainer/


# Transfer Learning

> It is taking what one model had learned in a similar domain in which we are working and apply to our specific use case/need.

> It is leveraging a working model's existing architecture and learned patters for out problem.


## Types Of Transfer Learning

> **"As is" transfer learning** is when you take a pretrained model as it is and apply it to your task without any changes.

    For example, many computer vision models are pretrained on the ImageNet dataset which contains 1000 different classes of images. This means passing a single image to this model will produce 1000 different prediction probability values (1 for each class).

    This is helpful if you have 1000 classes of image you'd like to classify and they're all the same as the ImageNet classes, however, it's not helpful if you want to classify only a small subset of classes (such as 10 different kinds of food). Model's with "/classification" in their name on TensorFlow Hub provide this kind of functionality.

> **Feature extraction transfer learning** is when you take the underlying patterns (also called weights) a pretrained model has learned and adjust its outputs to be more suited to your problem.

    For example, say the pretrained model you were using had 236 different layers (EfficientNetB0 has 236 layers), but the top layer outputs 1000 classes because it was pretrained on ImageNet. To adjust this to your own problem, you might remove the original activation layer and replace it with your own but with the right number of output classes. The important part here is that only the top few layers become trainable, the rest remain frozen.
    This way all the underlying patterns remain in the rest of the layers and you can utilize them for your own problem. This kind of transfer learning is very helpful when your data is similar to the data a model has been pretrained on.

> **Fine-tuning transfer learning** is when you take the underlying patterns (also called weights) of a pretrained model and adjust (fine-tune) them to your own problem.


## Transfer Learning Feature Extraction Steps:-

1) import the libraries and an helper_function if needed
2) Get the training and test datasets
3) Create the train, test directories and split the train and test data.
4) Create a *data augmentation* layer if needed.
5) Create *Callbacks* if needed like ModelCheckpoint, TensorBoard etc.
6) *ModelCheckpoint* callback is needed as it can be used to reset the model weights after it was fine-tuned.
7) Create the model and compile and fit the model.
8) Evaluate the model, save the accuracy value to a variable, plot so curves.


## Transfer Learning Fine-tuning Steps:-

1) Create a Feature *Extraction model* from the above steps.
2) Unfreeze *n* numbers of layers from the model as needed. (n -> numbers of layers to be unfrozen)
3) Recompile the model with a *10x* lower *learning_rate*.
4) Fit the model for some epochs after the *initial epochs* in *feature_extraction* of the model
5) Evaluate the model, save the accuracy value to a variable, plot so curves.







# Tensorflow Certification Course

> 2. Deep Learning and TensorFlow Fundamentals(Completed)

> 3. Neural network regression with TensorFlow(Completed)

> 4. Neural network classification in TensorFlow(Completed)

> 5. Computer Vision and Convolutional Neural Networks in TensorFlow(Completed)

> 6. Transfer Learning in TensorFlow Part 1 Feature extraction(Completed)

> 7. Transfer Learning in TensorFlow Part 2 Fine tuning(Completed)

> 8. Transfer Learning with TensorFlow Part 3 Scaling Up(Completed)

> 9. Milestone Project 1 Food Vision Big™

> Video 2




