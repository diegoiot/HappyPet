import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilente-v2",["--model=/PetBowlDetector/ssd-mobilenet.onnx","--labels=/PetBowlDetector/labels.txt","--input-blob=input_0","--output-cvg=scores","--output-bbox=boxes"])
camera = jetson.utils.videoSource("rtsp://USER:KEYCAM@IPLAN:554/H.264")
display = jetson.utils.videoOutput("display://0")

while display.IsStreaming():
       img = camera.Capture()
       detections = net.Detect(img)
       n_obj = len(detections)
       display.Render(img)
       display.SetStatus("Object Detection | Network {:.0f} FPS | #n_obj: {}".format(net.GetNetworkFPS(),n_obj))
