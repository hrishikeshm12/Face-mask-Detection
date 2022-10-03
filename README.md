# Face-mask-Detection

In this project I have made a simple Face Mask Detecion web application. The app is built using python and Juypter notebooks. Face mask detection was implemented as solution to detect the correct usage of face mask to curb the spread of COVID-19. In this project I have used machine learning and more specifically neural networks to detect face masks dynamically using live video capture. The model used was VGG-16 due to its robustness and high accuracy.

VGG16 is object detection and classification algorithm which is able to classify 1000 images of 1000 different categories with 92.7% accuracy. It is one of the popular algorithms for image classification and is easy to use with transfer learning.

Dataset used: 
  With Mask: 2700 images
  Without Mask: 3800 images
  
Model Description:
 
   Total params: 134,260,544
   Trainable params: 134,260,544
   activation used: sigmoid
   Layers used: Max pooling 2D, Conv2D
   optimizer: Adam
   loss: Binary Cross Entropy
  
  Results:
  
    The implemented model gave an accuracy of 92.45%. Training accuracy can be increased by increasing the number of epochs, number of trainable images and features.
    A good GPU with above recommendations will certainly make the model perform better.
    
    
