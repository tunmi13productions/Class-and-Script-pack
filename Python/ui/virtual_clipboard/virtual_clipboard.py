# A virtual clipboard.
# useful for those who do not have NVDA, or if they do, do not have Speech History / Clip Copy

class virtual_clipboard:
	def __init__(self, **kwargs):
		self.copied_items = []
		self.last_copied_item = kwargs.get("text", "")
		# The amount the clipboard can hold before needing to be cleared.
		self.clearance_threshold = kwargs.get("clearance_threshold", 500)

	def reset(self):
		self.last_copied_item = ""
		self.copied_items.clear()

	@property
	def text(self): return self.last_copied_item

	@text.setter
	def text(self, content):
		if self.last_copied_item == content:
			return
		else:
			self.last_copied_item = content
			if len(self.copied_items) >= self.clearance_threshold:
				self.copied_items.clear()
			self.copied_items.append(self.last_copied_item)
