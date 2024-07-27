import requests

# Set the base URL for your Flask app
BASE_URL = 'http://127.0.0.1:5000'

video_script = """
[Intro Music]

Host: "Welcome back to our channel! Today, we're going to explore one of the most fascinating aspects of artificial intelligence: neural networks. Whether you're a beginner or just looking to refresh your knowledge, this video will give you a solid understanding of what neural networks are and how they work."

[Cut to Visuals of Neural Networks]

Host: "So, what exactly is a neural network? In simple terms, a neural network is a series of algorithms that attempt to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates. It consists of layers of nodes, or 'neurons,' each connected to the next layer."

[Graphic Animation of Neural Network Layers]

Host: "Each neuron receives input from the previous layer, processes it, and passes the output to the next layer. The first layer is called the input layer, and the last layer is known as the output layer. In between, we have hidden layers, which perform most of the computations."

[Detailed Diagram of a Neural Network]

Host: "Neural networks learn by adjusting the weights of the connections between neurons. This is done through a process called backpropagation, where the network adjusts its weights based on the error of its predictions compared to the actual results."

[Example of a Simple Neural Network in Action]

Host: "Let’s take a simple example. Suppose we have a neural network designed to recognize handwritten digits. We feed it images of digits, and the network processes these images, making adjustments based on its accuracy in identifying them correctly. Over time, it gets better and better at recognizing digits."

[Cut to Host]

Host: "The applications of neural networks are vast and varied. They are used in image and speech recognition, medical diagnosis, stock market prediction, and even in autonomous vehicles. Their ability to learn from data and improve over time makes them incredibly powerful tools in the AI toolkit."

[Outro Music]

Host: "We hope this video has given you a clear understanding of neural networks. If you have any questions or topics you'd like us to cover, leave a comment below. Don't forget to like and subscribe for more videos on AI and machine learning. Thanks for watching!"

[End Screen with Channel Information]
"""

def test_ocr():
    with open(r'test\testocr.png', 'rb') as image:
        response = requests.post(f'{BASE_URL}/ocr', files={'image': image})
        print(response.json())

def test_chatbot():
    data = {'text': 'Hello, how are you?'}
    response = requests.post(f'{BASE_URL}/chatbot', data=data)
    print(response.json())

def test_yolosegment():
    with open(r'test\Happy.jpg', 'rb') as image:
        response = requests.post(f'{BASE_URL}/yolosegment', files={'image': image})
        with open(r'output\yolosegment_output.png', 'wb') as f: # Didn't work
            f.write(response.content)
        print('YOLO Segment output saved to yolosegment_output.png')

def test_emotiondetection():
    with open(r'test\Happy.jpg', 'rb') as image:
        response = requests.post(f'{BASE_URL}/emotiondetection', files={'image': image})
        with open(r'output\emotiondetection_output.jpg', 'wb') as f:
            f.write(response.content)
        print('Emotion detection output saved to emotiondetection_output.jpg')

def test_receiptgeneration():
    data = {'values': {'name': 'John Doe', 'email': 'john@example.com'}}
    response = requests.post(f'{BASE_URL}/receiptgeneration', json=data)
    with open(r'output\receipt.pdf', 'wb') as f:
        f.write(response.content)
    print('Receipt saved to receipt.pdf')

def test_imagecaptioning():
    with open(r'test\thumbnail.png', 'rb') as image:
        response = requests.post(f'{BASE_URL}/imagecaptioning', files={'image': image})
        print(response.json())

def test_getTranscipt():
    with open(r'test\story.mp3', 'rb') as audio:
        response = requests.post(f'{BASE_URL}/getTranscipt', files={'audio': audio})
        print(response.json())

def test_generateAlternateThumbnail():
    with open(r'test\thumbnail.png', 'rb') as image:
        data = {'n_thumbnails': '3'}
        response = requests.post(f'{BASE_URL}/generateAlternateThumbnail', files={'image': image}, data=data)
        print(response.json())

def test_editImagewithPrompt():
    with open(r'test\luggage.png', 'rb') as image:
        with open('path_to_mask.png', 'rb') as mask: # ADD HERE
            data = {'prompt': 'Add a sun in the sky'}
            response = requests.post(f'{BASE_URL}/editImagewithPrompt', files={'image': image, 'mask': mask}, data=data)
            print(response.json())

def test_generateImage():
    data = {'prompt': 'A beautiful landscape with mountains and a river'}
    response = requests.post(f'{BASE_URL}/generateImage', data=data)
    print(response.json())

def test_generateThumbnailfromTitle():
    data = {'title': 'How to cook pasta'}
    response = requests.post(f'{BASE_URL}/generateThumbnailfromTitle', data=data)
    print(response.json())

def test_generateThumbnailfromDescription():
    data = {'text': 'This video explains the steps to cook pasta perfectly.'}
    response = requests.post(f'{BASE_URL}/generateThumbnailfromDescription', data=data)
    print(response.json())

def test_tts_api():
    data = {'text': 'Hello, this is a test.', 'voice': 'default', 'tempo': 'normal'}
    response = requests.post(f'{BASE_URL}/tts', data=data)
    with open(r'output\output.mp3', 'wb') as f:
        f.write(response.content)
    print('TTS output saved to output.mp3')

def test_createSummaryFromAudioText():
    data = {'text': "In this audio, we delve into the fundamental concepts of machine learning, exploring its history, core principles, and various applications in today's technology-driven world. Perfect for beginners looking to understand the basics and implications of this exciting field.", 'no_words': '50'}
    response = requests.post(f'{BASE_URL}/createSummaryFromAudioText', data=data)
    print(response.json())

def test_createTitlefromDescription():
    data = {'text': 'In this video, we provide a comprehensive introduction to neural networks, a key concept in the field of artificial intelligence and machine learning. We break down the structure and function of neural networks, explain how they learn from data, and discuss their applications in various industries. Ideal for those new to AI and looking to grasp the essentials of neural networks.', 'no_words': '10'}
    response = requests.post(f'{BASE_URL}/createTitlefromDescription', data=data)
    print(response.json())

def test_createScriptfromDescription():
    data = {'text': 'In this video, we provide a comprehensive introduction to neural networks, a key concept in the field of artificial intelligence and machine learning. We break down the structure and function of neural networks, explain how they learn from data, and discuss their applications in various industries. Ideal for those new to AI and looking to grasp the essentials of neural networks.', 'no_words': '200'}
    response = requests.post(f'{BASE_URL}/createScriptfromDescription', data=data)
    print(response.json())

def test_createDescriptionfromTitle():
    data = {'text': "Understanding Neural Networks: A Beginner's Guide", 'no_words': '50'}
    response = requests.post(f'{BASE_URL}/createDescriptionfromTitle', data=data)
    print(response.json())

def test_generateScriptfromTitle():
    data = {'text': "Understanding Neural Networks: A Beginner's Guide", 'no_words': '200'}
    response = requests.post(f'{BASE_URL}/generateScriptfromTitle', data=data)
    print(response.json())

def test_createHashTagsfromDescription():
    data = {'text': 'In this video, we provide a comprehensive introduction to neural networks, a key concept in the field of artificial intelligence and machine learning. We break down the structure and function of neural networks, explain how they learn from data, and discuss their applications in various industries. Ideal for those new to AI and looking to grasp the essentials of neural networks.', 'no_words': '10'}
    response = requests.post(f'{BASE_URL}/createHashTagsfromDescription', data=data)
    print(response.json())

def test_validateMadeforKidsfromSummary():
    data = {'text': video_script}
    response = requests.post(f'{BASE_URL}/validateMadeforKidsfromSummary', data=data)
    print(response.json())

def test_createDescriptionfromScript():
    data = {'text': video_script, 'no_words': '50'}
    response = requests.post(f'{BASE_URL}/createDescriptionfromScript', data=data)
    print(response.json())

def test_createHashTagsfromScript():
    data = {'text': video_script, 'no_words': '10'}
    response = requests.post(f'{BASE_URL}/createHashTagsfromScript', data=data)
    print(response.json())

def test_createTitlefromScript():
    data = {'text': video_script, 'no_words': '10'}
    response = requests.post(f'{BASE_URL}/createTitlefromScript', data=data)
    print(response.json())

def test_generateThumbnailfromScript():
    data = {'text': video_script}
    response = requests.post(f'{BASE_URL}/generateThumbnailfromScript', data=data)
    print(response.json())

def test_helloworld():
    response = requests.get(f'{BASE_URL}/hello')
    print(response.json())

if __name__ == '__main__':
    test_ocr()
    test_chatbot()
    # test_yolosegment()
    test_emotiondetection()
    test_receiptgeneration()
    test_imagecaptioning()
    test_getTranscipt()
    test_generateAlternateThumbnail()
    # test_editImagewithPrompt()
    test_generateImage()
    test_generateThumbnailfromTitle()
    test_generateThumbnailfromDescription()
    test_tts_api()
    test_createSummaryFromAudioText()
    test_createTitlefromDescription()
    test_createScriptfromDescription()
    test_createDescriptionfromTitle()
    test_generateScriptfromTitle()
    test_createHashTagsfromDescription()
    test_validateMadeforKidsfromSummary()
    test_createDescriptionfromScript()
    test_createHashTagsfromScript()
    test_createTitlefromScript()
    test_generateThumbnailfromScript()
    test_helloworld()
