import wx
import os
import cv2
from Project import CreateProject
from Video import Example

class Windows(wx.Frame):


    def __init__(self, *args, **kwargs):
        super(Windows, self).__init__(*args, **kwargs)
        self.__path = ""
        self.__ex = ""
        self.__addVideo =""
        self.__imagePath=""
        self.__pathArchive=""
        self.InitUI()

    def InitUI(self):
        #Imagen y Icono
        #-----------------------------------------------------------
        self.png = wx.StaticBitmap(self, -1, wx.Bitmap("Frame/c.jpg", wx.BITMAP_TYPE_ANY))
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap("Frame/iconFrame.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        #--------------------------------------------------------------
        #Label information
        wx.StaticText(self, -1, "Project name: ", wx.Point(15, 30))
        self.projectName = wx.StaticText(self, -1, "No project has been loaded", wx.Point(100, 30))
        wx.StaticText(self, -1, "Video name: ", wx.Point(15, 50))
        self.videoName = wx.StaticText(self, -1, "No video has been uploaded", wx.Point(100, 50))
        menubar = wx.MenuBar()
        #---------------------------------------------------------------------

        fileMenu = wx.Menu()



        videoMenu = wx.Menu()
        #videoMenu.Append(wx.ID_EDIT, 'Get Images\tCtrl+G')
        #videoMenu.Append(wx.ID_ADD, 'Add Video\tCtrl+A')
        #videoMenu.Append(wx.ID_ANY, 'Import mail...')

        imageMenu = wx.Menu()
        imageMenu.Append(wx.ID_APPLY, 'Open Images\tCtrl+I')


        closeProgram = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Exit\tCtrl+E')
        closeProgram.SetBitmap(wx.Bitmap('Frame/exit.png'))



        createFile = wx.MenuItem(fileMenu, wx.ID_NEW, '&New Project\tCtrl+N')
        createFile.SetBitmap(wx.Bitmap("Frame/new.png"))
        fileMenu.AppendItem(createFile)
        openFile = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Open Project\tCtrl+O')
        openFile.SetBitmap(wx.Bitmap('Frame/open.png'))
        fileMenu.AppendItem(openFile)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(closeProgram)

        getImages = wx.MenuItem(videoMenu, wx.ID_EDIT, 'Get Images\tCtrl+G')
        getImages.SetBitmap(wx.Bitmap('Frame/image.png'))
        videoMenu.AppendItem(getImages)
        self.__addVideo = wx.MenuItem(videoMenu, wx.ID_ADD, 'Add Video\tCtrl+A')
        self.__addVideo.SetBitmap(wx.Bitmap('Frame/add.png'))
        videoMenu.AppendItem(self.__addVideo)


        openImages = wx.MenuItem(imageMenu, wx.ID_APPLY)


        self.Bind(wx.EVT_MENU, self.OnQuit, closeProgram)
        self.Bind(wx.EVT_MENU, self.newProject, createFile)
        self.Bind(wx.EVT_MENU, self.openProject, openFile)
        self.Bind(wx.EVT_MENU, self.getImages, getImages)
        self.Bind(wx.EVT_MENU, self.openImages, openImages)



        menubar.Append(fileMenu, '&File')
        menubar.Append(videoMenu, '&Video')
        menubar.Append(imageMenu, '&Image')
        self.SetMenuBar(menubar)

        self.SetSize((800, 600))
        self.SetTitle('Dronvi')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


    def newProject (self, e):
        self.__ex = CreateProject(None, title="Create New Project", videoName=self.videoName, projectName=self.projectName)
        self.__ex.Show()
        self.Bind(wx.EVT_MENU, self.addVideo, self.__addVideo)



    def addVideo (self,e):

        if self.__path != "":
            dlg = wx.MessageDialog(None, 'If you add a new video the present video will be replace whit this new video. Are you '
                                     'chure?', 'Add New Video', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result != wx.ID_YES:
                return


        self.Hide()
        frame = wx.Frame(None, -1, 'win.mp4')
        frame.SetDimensions(0, 0, 200, 50)

        # Create open file dialog
        openFileDialog = wx.FileDialog(frame, "Load Video", "", "",
                                       "All Files (*.*)|*.*",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        self.__path = str(openFileDialog.GetPath())
        pathVideo = os.path.basename(self.__path)
        self.videoName.SetLabelText(pathVideo)
        if self.__ex != "":
            self.__ex.setPath(self.__path)
        openFileDialog.Destroy()
        self.Show()

    def getImages(self,e):
        #self.__path = self.__ex.getPath()
        if self.__ex !="":
            self.__imagePath = self.__ex.getImagePath()
            self.__path = self.__ex.getPath()
            self.__pathArchive =self.__ex.getArchive()
        ex = Example(None, title="Video options", path= self.__path,imagePath=self.__imagePath, pathArchive=self.__pathArchive)
        ex.Show()



    def openImages (self, e):
        file = "./Main.py"
        path = file
        fp = open(path, 'r+');

    def openProject(self,e):
        self.__ex = ""
        self.__path = ""

        frame = wx.Frame(None, -1, 'win.mp4')
        frame.SetDimensions(0, 0, 200, 50)

        # Create open file dialog
        openFileDialog = wx.FileDialog(frame, "Load Project", "", "",
                                       "Project (*.vid)|*.vid",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        self.__imagePath = openFileDialog.GetPath()
        self.__pathArchive = openFileDialog.GetPath()
        pathVid=os.path.basename(self.__imagePath)
        self.projectName.SetLabelText(pathVid)
        self.videoName.SetLabelText("No video has been uploaded")
        self.__imagePath=self.__imagePath.replace(pathVid,"")
        self.__imagePath += "Images"
        print(self.__imagePath)
        openFileDialog.Destroy()

        self.Bind(wx.EVT_MENU, self.addVideo, self.__addVideo)


def main():

    app = wx.App()
    ex = Windows(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()