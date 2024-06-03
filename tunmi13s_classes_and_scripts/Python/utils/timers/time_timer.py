import time


class Timer:
	"""A timer class, to track time mesured in millis
	"""

	def __init__(self):
		self.inittime = time.time()
		self.paused = 0

	@property
	def elapsed(self):
		"""Returns the exact elapsed time since this timer was created or last restarted.
		"""
		if self.paused != 0:
			return self.paused
		else:
			return self._ms(time.time() - self.inittime)

	@elapsed.setter
	def elapsed(self, amount):
		"""Forces the timer to a specific time.
		
		Args:
			amount (int): The time elapsed (in millis)
		"""
		if self.paused == 0:
			self.inittime = time.time() - (amount / 1000)
		else:
			self.paused = amount

	def restart(self):
		"""Restarts the timer, and set it's elapsed time to 0.
		"""
		self.__init__()

	def pause(self):
		"""Pauses the timer at a certain position."""
		self.paused = self._ms(time.time() - self.inittime)

	def resume(self):
		"""Resumes the timer after being paused."""
		self.inittime = time.time() - (self.paused / 1000)
		self.paused = 0

	def _ms(self, t):
		return int(round(t*1000))
