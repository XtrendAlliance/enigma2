import os

class RcModel:
	RCTYPE_DMM = 0
	RCTYPE_ET9X00 = 1
	RCTYPE_ET6X00 = 2
	RCTYPE_ET9500 = 3
	RCTYPE_VU = 4
	RCTYPE_ET6500 = 5
	RCTYPE_ET4000 = 6

	def __init__(self):
		self.currentRcType = self.RCTYPE_DMM
		self.readRcTypeFromProc()

	def rcIsDefault(self):
		if self.currentRcType != self.RCTYPE_DMM:
			return False
		return True

	def readFile(self, target):
		fp = open(target, 'r')
		out = fp.read()
		fp.close()
		return out.split()[0]

        def readRcTypeFromProc(self):
		if os.path.exists('/proc/stb/info/boxtype'):
			model = self.readFile('/proc/stb/info/boxtype')
                        if model == 'et4000':
                                 self.currentRcType = self.RCTYPE_ET4000
                        elif model == 'et9000':
                                 self.currentRcType = self.RCTYPE_ET9X00
                        elif model == 'et9200':
                                 self.currentRcType = self.RCTYPE_ET9X00
                        elif model == 'et6500':
                                 self.currentRcType = self.RCTYPE_ET6500
                        elif model == 'et6000':
                                 self.currentRcType = self.RCTYPE_ET6X00
                        elif model == 'et9500':
                                 self.currentRcType = self.RCTYPE_ET9500

                        if not len(model) == 6 and model[:2] == 'et':
                            rc = self.readFile('/proc/stb/ir/rc/type')
                            if rc == '4':
                                    self.currentRcType = self.RCTYPE_DMM
                            elif rc == '6':
				    self.currentRcType = self.RCTYPE_DMM
                            elif rc == '9':
                                    self.currentRcType = self.RCTYPE_VU
		elif os.path.exists('/proc/stb/info/vumodel'):
			self.currentRcType = self.RCTYPE_VU

	def getRcLocation(self):
		if self.currentRcType == self.RCTYPE_ET9X00:
			return '/usr/share/enigma2/rc_models/et9x00/'
		elif self.currentRcType == self.RCTYPE_ET9500:
			return '/usr/share/enigma2/rc_models/et9500/'
		elif self.currentRcType == self.RCTYPE_ET6X00:
			return '/usr/share/enigma2/rc_models/et6x00/'
		elif self.currentRcType == self.RCTYPE_ET6500:
			return '/usr/share/enigma2/rc_models/et6500/'
		elif self.currentRcType == self.RCTYPE_ET4000:
			return '/usr/share/enigma2/rc_models/et4000/'	
		elif self.currentRcType == self.RCTYPE_VU:
			return '/usr/share/enigma2/rc_models/vu/'

rc_model = RcModel()
