import os


class DeleteFolderService:
    @staticmethod
    def deleteFolder():
        path = "upload/updated_audios/"
        for filename in os.listdir(path):
            os.unlink(path + filename)
            # print(filename)

    @staticmethod
    def deleteFolderConverted_audio():
        path = "upload/convertedAudio/"
        for filename in os.listdir(path):
            os.unlink(path + filename)
            # print(filename)
