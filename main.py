
from flask import Flask, render_template, Response
from camera import VideoCamera
#from haar import VideoCamera1

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#@app.route('/video')
#def video():
#  return render_template('index1.html')

#def gen(haar):
#   while True:
#       framehaar = haar.get_frame1()
#      yield (b'--frame\r\n'
#              b'Content-Type: image/jpeg\r\n\r\n' + framehaar + b'\r\n\r\n')

#@app.route('/video_feed1')
#def video_feed1():
 #   return Response(gen(VideoCamera1()),
 #                   mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
