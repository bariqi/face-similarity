# Face Similarity API

An API based on computer vision technique that measure the similarity between two faces.

## Getting Started

To run this program you need to follow instruction bellow step by step carefully:

1. Clone this project by clone or download the code. Now you will have face-similarity folder containing app and testing folder.
2. [Download face similarity pretrained model](https://drive.google.com/file/d/1Wn2_kSzO2MlZp3k1dyGZaLUKGTxQLutc/view?usp=sharing)
3. Put the model to face-similarity/app/models
4. You need to [Download](https://www.python.org/downloads/) and install python on your device. Don't forget to add to path python environment
5. Open your terminal/command line, and cd to the project ./face-similarity/app
6. Run "pip3 install -r requirement"
7. Run "uvicorn main:app --reload"
8. Open another new terminal/command line, and cd to the project .face-similarity/testing
9. Run "python3 post_api.py". You will get similarity value of sample photo
10. you can change the face by edit file post_api.py in the variable image and image 2. example: image = cv2.imread('data\\person1a.jpeg') change person1a.jpeg with person 2a.jpg and so on

For help getting started with Face similarity API, you can contact me on email bariqi.abdillah@gmail.com, which offers tutorials, samples, guidance to run this program.