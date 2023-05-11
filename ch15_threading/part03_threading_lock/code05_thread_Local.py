"threadLocal"
import threading

local = threading.local()


def process_student():
    student_name = local.name
    print("threadName: %s studentName: %s " % (threading.current_thread().name, student_name))


def process_thread(name):
    local.name = name
    process_student()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('Jack',), name="Thread-A")
    t2 = threading.Thread(target=process_thread, args=('Tom',), name="Thread-B")
    t1.start()
    t2.start()
