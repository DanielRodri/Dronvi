import wx
import os
class CreateProject(wx.Frame):
    tc1=""
    tc2 = ""

    def __init__(self, parent, title, videoName, projectName):
        super(CreateProject, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
        self.__path = ""
        self.__pathArchive = ""
        self.__imagePath = ""
        self.__videoName = videoName
        self.__projectName = projectName



    def InitUI(self):
        global tc1,tc2
        panel = wx.Panel(self)

        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("Frame/new.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="Options Project")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)

        #icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('exec.png'))
        #sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,
         #   border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="Name")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)

        text3 = wx.StaticText(panel, label="Video URL")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND,
            border=5)

        button1 = wx.Button(panel, label="Browse...")
        sizer.Add(button1, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)
        button1.Bind(wx.EVT_BUTTON, self.onBrower)


        button4 = wx.Button(panel, label="Ok")
        sizer.Add(button4, pos=(7, 3))
        button4.Bind(wx.EVT_BUTTON, self.onButton)
        button5 = wx.Button(panel, label="Cancel")
        sizer.Add(button5, pos=(7, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=10)
        button5.Bind(wx.EVT_BUTTON, self.onCancel)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)
        sizer.Fit(self)

    def onButton(self,e):
        global tc1,tc2
        if(tc2.GetValue()!="" and tc1.GetValue()!=""):
            try:
                os.mkdir('./Projects/'+ str(tc1.GetValue()))
                ruta = str('./Projects/'+ str(tc1.GetValue()))
                nombre = str(tc1.GetValue()+'.vid')
                self.__projectName.SetLabelText(nombre)
                os.mkdir('./Projects/' + str(tc1.GetValue()+'/Images'))
                self.__imagePath = str('./Projects/' + str(tc1.GetValue() + '/Images'))
                self.__pathArchive = ruta +'/'+nombre
                file = open(ruta +'/'+nombre, "w")
                file.write("0")
                file.close()
                self.Close()
            except:
                wx.MessageBox('The name of the project is already in use', 'Info', wx.OK | wx.ICON_INFORMATION)

        else:
            wx.MessageBox('Empty fields are not allowed', 'Info', wx.OK | wx.ICON_INFORMATION)

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
        self.pathVideo = os.path.basename(self.__path)
        self.__videoName.SetLabelText(self.pathVideo)
        tc2.SetValue(self.__path)
        openFileDialog.Destroy()
        self.Show()

    def onCancel(self,e):
        self.Close()

    def getPath(self):
        return self.__path

    def setPath(self, path):
         self.__path = path

    def getImagePath(self):
        return self.__imagePath

    def getArchive(self):
        return self.__pathArchive

