
import time


def _write_elapsed_time(start_t, msg=None):
    cur_time = time.time()
    elapsed_time = time.strftime("%H:%M:%S",
                                 time.gmtime(cur_time - start_t))
    print("{}".format(msg), elapsed_time)
    return cur_time
