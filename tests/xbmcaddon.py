class Addon(object):
    def __init__(self, id=None):
        pass

    def getAddonInfo(self, type):
        if type == "id":
            return "Torec"
        pass

    def openSetting(self):
        """ Can simulate openSettings xbmc call """
        print "Settings"

    def getSetting(self, kind):
        """ For unittest - you can return real user credentials
            to check user login.
            returning Nano or empty string will skip login
        """
        if kind == "username":
            return "A"
        elif kind == "password":
            return "X"
