class ActivityDbRow(object):
	def __init__(self, row=None):
		self.id = None
		self.label = None
		self.start_time = None
		self.end_time = None
		self.camera_id = None
		self.next_camera_id = None

		if row:
			self.id = row[0]
			self.label = row[1]
			self.start_time = row[2]
			self.end_time = row[3]
			self.camera_id = row[4]
			self.next_camera_id = row[5]

	def getID(self):
		return self.id

	def setID(self, id):
		self.id = id;

	def getLabel(self):
		return self.label

	def setLabel(self, label):
		self.label = label;

	def getStart_time(self):
		return self.start_time

	def setStart_time(self, start_time):
		self.start_time = start_time;

	def getEnd_time(self):
		return self.end_time

	def setEnd_time(self, end_time):
		self.end_time = end_time;

	def getCamera_id(self):
		return self.camera_id

	def setCamera_id(self, camera_id):
		self.camera_id = camera_id;

	def getNext_camera_id(self):
		return self.next_camera_id

	def setNext_camera_id(self, next_camera_id):
		self.next_camera_id = next_camera_id;

	def getSelectStatement(self):
		return "select id, label, start_time, end_time, camera_id, next_camera_id from tracking where id = %s" % self.id

	def getUpdateStatement(self):
		return "update tracking set label = '%s', end_time = current_timestamp(),camera_id = %s, next_camera_id = '%s' where id = %s" % (self.label, (self.camera_id if self.camera_id else 'null'), (self.next_camera_id if self.next_camera_id else 'null'), self.id)

	def getInsertStatement(self):
		return "insert into tracking (id, label, start_time, camera_id) values(%s, '%s', current_timestamp(), %s)" % (self.id, self.label, (self.camera_id if self.camera_id else 'null'))