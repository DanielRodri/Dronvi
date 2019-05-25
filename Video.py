import wx
import os
import cv2
from threading import Thread
import time
class Example(wx.Frame):

    tc2 = ""
    tc1 = ""
    def __init__(self, parent, title, path, imagePath, pathArchive):
        super(Example, self).__init__(parent, title=title)


        self.Centre()
        self.__path = path
        self.__imagePath = imagePath
        self.__pathArchive = pathArchive
        self.__tc1 = ""
        self.InitUI()


    def InitUI(self):
        global tc1, tc2
        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)
        vidcap = cv2.VideoCapture(self.__path)
        fps = round(vidcap.get(cv2.CAP_PROP_FPS))
        success, image = vidcap.read()
        if success == False:
            wx.MessageBox("Error video, please check the video url ", 'Information',
                          wx.OK | wx.ICON_INFORMATION)
            self.Close()
            return
        text1 = wx.StaticText(panel, label="Video fps = "+str(fps))
        vidcap.release()
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)

        #icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('exec.png'))
        #sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,
         #   border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="Numbers frames")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
        tc1.Bind(wx.EVT_CHAR, self.block_non_numbers)
        text2 = wx.StaticText(panel, label="Numbers second")
        sizer.Add(text2, pos=(3, 0), flag=wx.LEFT, border=10)

        self.tc2 = wx.TextCtrl(panel)
        sizer.Add(self.tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND)
        self.tc2.Bind(wx.EVT_CHAR, self.block_non_numbers)
        button4 = wx.Button(panel, label="Ok")
        sizer.Add(button4, pos=(7, 3))
        button4.Bind(wx.EVT_BUTTON, self.onButton)
        button5 = wx.Button(panel, label="Cancel")
        sizer.Add(button5, pos=(7, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=10)
        button5.Bind(wx.EVT_BUTTON, self.onCancel)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)

    def block_non_numbers(self,event):
        key_code = event.GetKeyCode()
        print(key_code)
        # Allow ASCII numerics
        if ord('0') <= key_code <= ord('9'):
            event.Skip()
            return

        # Allow tabs, for tab navigation between TextCtrls
        if key_code == ord('\t'):
            event.Skip()
            return

        if key_code == 8:
            event.Skip()
            return

        # Block everything else
        return

    def getImages(self):
        global tc1
        f = open(self.__pathArchive, 'r')
        self.count = int(f.read())
        f.close()

        count2 = 1
        frame_rate = int(tc1.GetValue())
        contador = 0
        try:

            vidcap = cv2.VideoCapture(self.__path)

            # print(vidcap.read())
            success, image = vidcap.read()
            fps = round(vidcap.get(cv2.CAP_PROP_FPS))

            if (frame_rate > fps):
                wx.MessageBox("Error in fps", 'Information',
                              wx.OK | wx.ICON_INFORMATION)
                return

            if success == False:
                wx.MessageBox("Error, the video has not been added ", 'Information',
                              wx.OK | wx.ICON_INFORMATION)
            else:

                length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
                pulse_dlg = wx.ProgressDialog(title="Processing Video", message="Please Wait", maximum=length - 2,
                                              style=wx.PD_CAN_ABORT | wx.PD_AUTO_HIDE)

                while length - 2 >= count2:

                    cancel = pulse_dlg.Update(count2)
                    if cancel == (False, False):
                        pulse_dlg.Destroy()
                        return

                    success, image = vidcap.read()


                    if ((int(self.tc2.GetValue())*fps)==contador-frame_rate and int(self.tc2.GetValue()) !=0):
                        contador = 0

                    if(contador == fps and int(self.tc2.GetValue()) == 0):
                        contador=0

                    if contador < frame_rate:
                        cv2.imwrite(self.__imagePath + "/frame%d.jpg" % self.count, image)  # save frame as JPEG file
                        self.count += 1

                    count2 += 1
                    contador += 1


        except:
            wx.MessageBox("Error, Firt you need to create or open a project", 'Information',
                          wx.OK | wx.ICON_INFORMATION)

        f = open(self.__pathArchive, 'w')
        f.write(str(self.count))
        f.close()
        self.Close()

    def onButton(self,e):

        self.getImages()



    def onBrower(self,e):
        global tc2
        self.Hide()
        frame = wx.Frame(None, -1, 'win.mp4')
        frame.SetDimensions(0, 0, 200, 50)

        # Create open file dialog
        openFileDialog = wx.FileDialog(frame, "Load Video", "", "",
                                       "All Files (*.*)|*.*",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        self.__path = openFileDialog.GetPath()
        tc2.SetValue(self.__path)
        openFileDialog.Destroy()
        self.Show()

    def onCancel(self,e):
        self.Close()

    def getPath(self):
        return self.__path

    def setPath(self, path):
         self.__path = path