import threading
import time
import os, sys, inspect
# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath("C:\Users\Aran Sena\Documents\Repos\kcl-as\kivy_ws\uarm_gui")
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from trakstar import TrakSTARInterface, TrakSTARRecordingThread

if __name__=="__main__":

    print "Connecting to trakStar...please wait..."
    try:
        trakStar = TrakSTARInterface()
        thr_init_trackstar = threading.Thread(target=trakStar.initialize)
        thr_init_trackstar.start()
        # fig = plt.figure()
        # plt.ion()
        # ax = fig.add_subplot(111, projection='3d')

        # ydata = [0]*50
        # line, = plt.plot(ydata)
        #
        # ax = fig.gca(projection='3d')

        while True:
            if trakStar.is_init:
                trakstar_thread = TrakSTARRecordingThread(trakStar)
                trakstar_thread.start()
                trakstar_thread.start_recording()
                print trakStar.attached_sensors
                while True:
                    data_array = trakstar_thread.get_data_array()
                    sensor_data = []
                    sensor_x = []
                    sensor_y = []
                    for data in data_array:
                        if data.has_key(1):
                            sensor_data = (data[1].tolist())
                            print sensor_data
                            sensor_x.append(sensor_data[0])
                            sensor_y.append(sensor_data[1])
                            # x = data[1][0]
                            # y = data[1][1]
                            # azimuth = data[1][3]
                            # print "x, y: ", x, y
                            # ax.clear()
                            # ax.set_xlim(-10, 10)
                            # ax.set_ylim(-10, 10)
                            # ax.set_zlim(-10, 10)

                            # if azimuth >= 0:
                            #     azimuth = 180-azimuth
                            # else:
                            #     azimuth = -1.0*(180+azimuth)
                            #ax.quiver(data[1][0], data[1][1], data[1][2], azimuth , data[1][4], data[1][5], length=3)
                            #ax.quiver(data[1][0], data[1][1], data[1][2], azimuth, data[1][4], data[1][5], length=3)
                            # line.set_xdata(x)
                            # line.set_ydata(y)
                            # plt.draw()
                            #plt.pause(0.0001)
                            #break
                    print sensor_x
                    #plt.pause(0.0001)
            else:
                print "waiting to connect: ", trakStar.is_init
                time.sleep(1)

    except Exception as e:
        print "error connecting: ", e
