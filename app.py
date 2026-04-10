# from CosmeticDetection.pipeline.training_pipeline import TrainPipeline

# obj = TrainPipeline()
# obj.run_pipeline()

import os
import sys
from CosmeticDetection.pipeline.training_pipeline import TrainPipeline
from CosmeticDetection.utils.main_utils import decodeImage,encodeImageIntoBase64
from flask import Flask, request, jsonify,render_template,Response
from flask_cors import CORS,cross_origin
from CosmeticDetection.constant.application import APP_HOST,APP_PORT
from ultralytics import YOLO
import shutil
import glob

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.file_name=os.path.join(os.getcwd(),"input_image.jpg")
        self.model = YOLO("artifacts/model_trainer/best.pt")

clApp = ClientApp()

@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Completed!!"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        print("STEP 1: Request received")
        image = request.json['image']
        decodeImage(image,clApp.file_name)
        if not os.path.exists(clApp.file_name):
            raise Exception("Image NOT saved ❌")

        print("STEP 2: Image saved at", clApp.file_name)

        results =clApp.model.predict(source=clApp.file_name,conf=0.1,imgsz= 320,save=True)
        save_dir = results[0].save_dir
        output_files = glob.glob(os.path.join(save_dir, "*.jpg"))
        if not output_files:
            raise Exception("No output image found ❌")

        output_image_path = output_files[0]
        # files= os.listdir(save_dir)
        # if len(files) == 0:
        #     raise Exception("No output image found ❌")
        
        #output_image_path = os.path.join(save_dir,files[0])
        print("STEP 3: Output at", output_image_path)
        output_image = encodeImageIntoBase64(output_image_path)
        result = {"image": output_image.decode("utf-8")}

        # cleanup
        # if os.path.exists("runs"):
        #     shutil.rmtree("runs")
        return jsonify(result)

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)})
    
@app.route("/live")
def predictLive():
    try:
        #results = clApp.model.predict(source=0, stream=True, conf=0.5)
        results =clApp.model.predict(source=clApp.file_name,conf=0.01,imgsz= 320,save=True)

        for r in results:
            print(r.boxes.data)
        return "Camera starting!!"
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT , debug=True)

