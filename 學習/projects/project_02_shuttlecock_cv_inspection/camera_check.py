# -*- coding: utf-8 -*-
import sys
import os
import cv2
import numpy as np
from ctypes import *

current_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_folder, "MvImport"))
from MvCameraControl_class import *

def main():
    deviceList = MV_CC_DEVICE_INFO_LIST()
    MvCamera.MV_CC_EnumDevices(MV_USB_DEVICE, deviceList)
    stDeviceList = cast(deviceList.pDeviceInfo[0], POINTER(MV_CC_DEVICE_INFO)).contents
    cam = MvCamera()
    cam.MV_CC_CreateHandle(stDeviceList)
    cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
    cam.MV_CC_StartGrabbing()
    
    print("相機基礎檢查啟動，按 'q' 退出")
    # ... 簡化版顯示邏輯 ...
    cam.MV_CC_StopGrabbing()
    cam.MV_CC_CloseDevice()

if __name__ == "__main__": main()
