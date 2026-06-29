import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image

@st.cache_resource
def load_cached_model():
    model = MobileNetV2(weights='imagenet')
    return model

model = load_cached_model()

def preprocess_image(image):
    img_array = np.array(image)
    resized_img = cv2.resize(img_array, (224, 224))
    preprocessed_img = preprocess_input(resized_img)
    batch_img = np.expand_dims(preprocessed_img, axis=0)
    return batch_img

def classify_image(model, image):
    try:
        processed_img = preprocess_image(image)
        predictions = model.predict(processed_img)
        decoded_predictions = decode_predictions(predictions, top=3)[0]
        return decoded_predictions
    except Exception as e:
        st.error(f"Error classifying image: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="AI Image Classifier", 
        page_icon="📷", 
        layout="centered"
    )
    
    st.title("AI Image Classifier")
    st.write("Upload an image, and the AI will analyze what is inside it.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Classify Image"):
            with st.spinner("Analyzing image..."):
                predictions = classify_image(model, img)
                
                if predictions:
                    st.subheader("Predictions:")
                    for _, label, score in predictions:
                        formatted_label = label.replace('_', ' ').title()
                        st.write(f"**{formatted_label}**: {score * 100:.2f}%")

if __name__ == "__main__":
    main()