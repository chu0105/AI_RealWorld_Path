# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import cv2
from datetime import datetime
from ctypes import *

current_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_folder, "MvImport"))

try:
    from MvCameraControl_class import *
except ImportError:
    print("錯誤：找不到 MvImport 資料夾！")
    sys.exit()

def main():
    deviceList = MV_CC_DEVICE_INFO_LIST()
    ret = MvCamera.MV_CC_EnumDevices(MV_USB_DEVICE, deviceList)
    if ret != 0 or deviceList.nDeviceNum == 0:
        print("找不到相機！")
        return

    stDeviceList = cast(deviceList.pDeviceInfo[0], POINTER(MV_CC_DEVICE_INFO)).contents
    cam = MvCamera()
    cam.MV_CC_CreateHandle(stDeviceList)
    cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
    
    nPayloadSize = 4096 * 4096 * 3
    data_buf = (c_ubyte * nPayloadSize)() 
    convert_buf = (c_ubyte * nPayloadSize)()
    cam.MV_CC_StartGrabbing()
    stFrameInfo = MV_FRAME_OUT_INFO_EX()

    print("✅ 相機已啟動！[q] 離開 [s] 存檔")
    while True:
        ret = cam.MV_CC_GetOneFrameTimeout(byref(data_buf), nPayloadSize, stFrameInfo, 1000)
        if ret == 0:
            stConvertParam = MV_CC_PIXEL_CONVERT_PARAM()
            stConvertParam.nWidth, stConvertParam.nHeight = stFrameInfo.nWidth, stFrameInfo.nHeight
            stConvertParam.pSrcData = cast(data_buf, POINTER(c_ubyte))
            stConvertParam.nSrcDataLen = stFrameInfo.nFrameLen
            stConvertParam.enSrcPixelType = stFrameInfo.enPixelType
            stConvertParam.enDstPixelType = PixelType_Gvsp_BGR8_Packed
            stConvertParam.pDstBuffer = cast(convert_buf, POINTER(c_ubyte))
            stConvertParam.nDstBufferSize = nPayloadSize
            
            if cam.MV_CC_ConvertPixelType(stConvertParam) == 0:
                image = np.asarray(convert_buf)[:stConvertParam.nDstLen].reshape((stFrameInfo.nHeight, stFrameInfo.nWidth, 3))
                image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                edges = cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 50, 150)
                cv2.imshow("Color", cv2.resize(image, (640, 480)))
                cv2.imshow("Edges (Canny)", cv2.resize(edges, (640, 480)))

        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'): break
        elif k == ord('s'):
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            cv2.imwrite(f"feather_color_{ts}.jpg", image)
            cv2.imwrite(f"feather_edge_{ts}.jpg", edges)
            print(f"📸 存檔成功: {ts}")

    cam.MV_CC_StopGrabbing()
    cam.MV_CC_CloseDevice()
    cv2.destroyAllWindows()

if __name__ == "__main__": main()
