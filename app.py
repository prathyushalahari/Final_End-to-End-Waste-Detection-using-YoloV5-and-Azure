# import sys
# import os
# from wasteDetection.pipeline.training_pipeline import TrainPipeline
# from wasteDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask import Flask, request, jsonify, render_template, Response
# from flask_cors import CORS, cross_origin
# from wasteDetection.constant.application import APP_HOST, APP_PORT


# app = Flask(__name__)
# CORS(app)


# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"


# @app.route("/train")
# def trainRoute():
#     obj = TrainPipeline()
#     obj.run_pipeline()
#     return "Training Successfull!!"


# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/predict", methods=['POST', 'GET'])
# @cross_origin()
# def predictRoute():
#     try:
#         # Ensure input directory exists
#         input_image_path = "/inputImage.jpg"
#         # os.makedirs("data", exist_ok=True)

#         # Decode the incoming image and save it
#         image = request.json['image']
#         decodeImage(image, input_image_path)

#         # Run YOLOv5 detection
#         custom_output_dir = "yolov5/output_detect"
#         os.makedirs(custom_output_dir, exist_ok=True)

#         command = (
#             f"cd yolov5/ && python detect.py --weights best.pt --img 416 "
#             f"--conf 0.25 --source ../{input_image_path} --save-txt --save-conf "
#             f"--project {custom_output_dir} --name exp --exist-ok"
#         )
#         os.system(command)

#         # Get output detection image
#         output_image_path = f"{custom_output_dir}/exp/inputImage.jpg"

#         # Convert detected image to Base64 for response
#         opencodedbase64 = encodeImageIntoBase64(output_image_path)
#         result = {"predicted_image": opencodedbase64.decode('utf-8')}

#         # (Optional) Clean up the previous results
#         os.system(f"rm -rf {custom_output_dir}/exp")

#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside json data")
#     except KeyError:
#         return Response("Key value error incorrect key passed")
#     except Exception as e:
#         print(e)
#         result = "Invalid input"

#     return jsonify(result)


# @app.route("/live", methods=['GET'])
# @cross_origin()
# def predictLive():
#     try:
#         os.system(
#             "cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.1 --source 0")
#         os.system("rm -rf yolov5/runs")
#         return "Camera starting!!"

#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside  json data")


# if __name__ == "__main__":
#     clApp = ClientApp()
#     app.run(host=APP_HOST, port=APP_PORT)


# ------------------------------------------------------------------------------

import sys
import os
from wasteDetection.pipeline.training_pipeline import TrainPipeline
from wasteDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from wasteDetection.constant.application import APP_HOST, APP_PORT

app = Flask(__name__)
CORS(app)

# Ensure the data directory exists for storing input images
# os.makedirs("data", exist_ok=True)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"  # Store image inside 'data/'


@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successful!!"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        # Decode the incoming image and save it
        image = request.json['image']
        decodeImage(image, clApp.filename)

        # Run YOLOv5 detection
        custom_output_dir = "yolov5/output_detect"
        os.makedirs(custom_output_dir, exist_ok=True)

        command = (
            f"cd yolov5/ && python detect.py --weights best.pt --img 416 "
            f"--conf 0.25 --source ../{clApp.filename} --save-txt --save-conf "
            f"--project {custom_output_dir} --name exp --exist-ok"
        )
        os.system(command)

        # Get the latest detection output image
        output_image_path = f"{custom_output_dir}/exp/inputImage.jpg"
        if not os.path.exists(output_image_path):
            return Response("Error: Output image not found!")

        # Convert detected image to Base64 for response
        opencodedbase64 = encodeImageIntoBase64(output_image_path)
        result = {"predicted_image": opencodedbase64.decode('utf-8')}

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key value error: incorrect key passed")
    except Exception as e:
        print(e)
        return Response("Invalid input")

    return jsonify(result)


@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system(
            "cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.1 --source 0"
        )
        return "Camera starting!!"

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)
