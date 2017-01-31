class PWM:
    _____channel = -1
    _____freq = 0
    _____dutyCycle = 0.0

    def __init__(self, channel, frequency):
        self._____channel = channel
        self._____freq = frequency

    def start(self, dc):
        self._____dutyCycle = dc

    def ChangeFrequency(self, freq):
        self._____freq = freq

    def ChangeDutyCycle(self, dc):
        self._____dutyCycle = dc

    def stop(self):
        pass
