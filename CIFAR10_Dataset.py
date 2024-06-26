#Input the relevant libraries
import streamlit as st

# Define the Streamlit app
def app():
    text = """Comparison of Basic Feed-Forward ANN and Convolutional Neural Network Built Using Tensorflow and Keras for the CIFAR-10 Dataset"""
    st.subheader(text)

    text = """Prof. Louie F. Cervantes, M. Eng. (Information Engineering) \n
    CCS 229 - Intelligent Systems
    Department of Computer Science
    College of Information and Communications Technology
    West Visayas State University"""
    st.text(text)

    st.image('tf-keras.png', caption="Tensorflow and Keras")
    st.write("https://www.tensorflow.org/")
    st.write("https://keras.io/")

    text = """TensorFlow, an open-source library, provides a powerful 
    end-to-end platform for various machine learning tasks. It offers 
    low-level computational capabilities, enabling fine-grained control 
    over model architectures. However, for tasks focused on rapid prototyping 
    and experimentation with deep neural networks, Keras acts as a 
    complementary high-level API. Built on top of TensorFlow, 
    Keras streamlines the development process with a user-friendly 
    Python interface. It abstracts away intricate low-level operations, 
    allowing computer scientists to focus on designing model components 
    like layers, optimizers, and loss functions. """
    st.write(text)
    st.image('cifar10.png', caption="CIFAR-10 Dataset")
    
    with st.expander("How to use this App"):
         text = """Step 1. Go to Training page. Set the parameters of the CNN. Click the button to begin training.
         \nStep 2.  Go to Performance Testing page and click the button to load the image
         and get the model's output on the classification task.
         \nYou can return to the training page to try other combinations of parameters."""
         st.write(text)

    with st.expander("Show more information"):
        text = """
        This Streamlit application utilizes a pre-existing dataset called CIFAR-10 
        for image classification using a Convolutional Neural Network (CNN).
        Data Source:
        The application relies on the CIFAR-10 dataset, a well-known benchmark 
        dataset for image classification tasks.
        This dataset is publicly available and can be downloaded directly within 
        the application code using TensorFlow's datasets.cifar10.load_data() function.
        Data Description:
        CIFAR-10 consists of 60,000 color images in 32x32 pixel resolution.
        
        The images are categorized into 10 mutually exclusive classes:
        airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.
        The data is split into 50,000 training images and 10,000 testing images.
        This split allows the CNN model to learn from the training data and evaluate 
        its performance on unseen data (testing data).
        
        Data Preprocessing (performed within the application):
        The application performs minimal preprocessing on the data:
        Normalization: Pixel values are typically normalized to a range between 0 and 1 
        for better training efficiency.
        Data Used in the App:
        
        The application utilizes the following data from CIFAR-10:
        Training images: Used to train the CNN model to recognize patterns and features.
        Training labels: These labels correspond to the class categories of each training image.
        Test images: Used to evaluate the trained model's performance on unseen data.
        Test labels: Labels corresponding to the classes of the test images.    
        """
        st.write(text)
    
#run the app
if __name__ == "__main__":
    app()
