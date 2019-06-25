from adb.client import Client as AdbClient
from time import sleep


def swipe_to_next():
    device.shell('input swipe 500 1213 500 1008')


def back():
    device.shell('input keyevent 4')


def click_message():
    device.shell('input tap 540 580')


def click_input():
    device.shell('input tap 538 1944')


def input_message():
    device.shell("am broadcast -a ADB_INPUT_TEXT --es msg '您好，我对这个职位很感兴趣，希望您看一下我的简历，谢谢！'")


def send_message():
    device.shell('input tap 1003 1893')


client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
for device in devices:
    print('Device %s connected' % device)
    device.shell('ime set com.android.adbkeyboard/.AdbIME')
    i = 1
    while(True):
        print('Try next message: %s' % i)
        click_message()
        click_input()
        input_message()
        send_message()
        back()
        back()
        sleep(0.5)
        swipe_to_next()
        i = i + 1
