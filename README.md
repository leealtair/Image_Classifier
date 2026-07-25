# AI Image Classifier 📷

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/leealtair/Image_Classifier/actions)
[![Version](https://img.shields.io/badge/version-0.1.0-blue)](https://pypi.org/project/image-classifier/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)

## Description 📝

This project is a Streamlit-based web application that allows users to upload an image and have it classified by an AI model. It utilizes the MobileNetV2 architecture, pre-trained on the ImageNet dataset, to predict the top three labels and their confidence scores for the uploaded image.

## Table of Contents 📜

- [Features](#features-🌟)
- [Tech Stack](#tech-stack-🛠️)
- [Installation](#installation--)
- [Usage](#usage--)
- [Project Structure](#project-structure-📁)
- [Contributing](#contributing--)
- [License](#license-⚖️)
- [Important Links](#important-links--)
- [Footer](#footer-✨)

## Features 🌟

- **Image Upload**: Allows users to upload images in JPG, JPEG, and PNG formats.
- **AI-Powered Classification**: Employs a pre-trained MobileNetV2 model for image recognition.
- **Top Predictions**: Displays the top 3 predicted labels and their confidence scores.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive user experience.
- **Cached Model Loading**: Efficiently loads the AI model using Streamlit's caching mechanism for faster subsequent predictions.

## Tech Stack 🛠️

- **Language**: Python
- **Frameworks/Libraries**:
  - Streamlit: For building the interactive web application.
  - TensorFlow/Keras: For the machine learning model (MobileNetV2).
  - OpenCV: For image processing tasks.
  - NumPy: For numerical operations.
  - Pillow (PIL): For image manipulation.

## Installation 🚀

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/leealtair/Image_Classifier.git
    cd Image_Classifier
    ```

2.  **Install dependencies** using pip:
    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, based on `pyproject.toml`:
    ```bash
    pip install opencv-python>=4.13.0.92 streamlit>=1.58.0 tensorflow>=2.21.0
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run main.py
    ```

## Usage 🖥️

This application provides a simple web interface for classifying images:

1.  **Run the application** using the command `streamlit run main.py`.
2.  **Open your web browser** and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
3.  **Upload an image** by clicking the "Choose an image..." button and selecting a file from your local machine (supports JPG, JPEG, PNG).
4.  **Click the "Classify Image" button** to get the AI's predictions.
5.  The application will display the uploaded image and then list the top 3 predicted labels with their corresponding confidence percentages.

**Real-world Use Case:** This tool can be used for educational purposes, quick image content identification, or as a starting point for more complex image analysis applications.

## Project Structure 📁

```
Image_Classifier/
├── README.md
├── pyproject.toml
├── main.py
├── .python-version
└── uv.lock
```

-   `README.md`: This file, containing project documentation.
-   `pyproject.toml`: Project metadata and dependencies.
-   `main.py`: The main entry point for the Streamlit application, containing the image classification logic.
-   `.python-version`: Specifies the Python version (though content is empty).
-   `uv.lock`: A lock file, likely for dependency management (content is large and unspecified).

## Contributing 🤝

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request. You can also open an issue with the tag "enhancement".

## License ⚖️

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Important Links 🔗

-   **Repository URL**: [https://github.com/leealtair/Image_Classifier](https://github.com/leealtair/Image_Classifier)

## Footer ✨

This README was generated based on the analysis of the `Image_Classifier` repository.

-   **Repository**: [Image_Classifier](https://github.com/leealtair/Image_Classifier)
-   **Author**: leealtair
-   **Contact**: Please refer to the repository for contact information.

Feel free to **fork** this repository, **like** it, give it a **star** ⭐, and report any **issues**!


---
**<p align="center">© 2026 LeeAltair. All Rights Reserved.</p>**
