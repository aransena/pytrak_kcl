from trakstar import TrakSTARInterface
import threading
import time

trakstar_data = []
trakstar = None

def trakstar_thread():
    global trakstar_data
    global trakstar
    while True:
        trakstar_data = trakstar.get_synchronous_data_dict(
            write_data_file=False)  # self.trakstar.get_data_array()


if __name__=='__main__':
    global trakstar
    print "Connecting to trakstar"
    trakstar = TrakSTARInterface()
    thr_init_trakstar = threading.Thread(target=trakstar.initialize)
    thr_init_trakstar.start()
    while True:
        if trakstar.is_init:
            print "Connected to trakstar!"
            trakstar_thread = threading.Thread(target=trakstar_thread)
            trakstar_thread.start()
            #self.root.setup_trakstar(trakstar_thread)
            print "trakstar ready"
            break
        else:
            print "waiting on trakstar...\n"
            time.sleep(1)

    while True:
        print "Received: ", trakstar_data