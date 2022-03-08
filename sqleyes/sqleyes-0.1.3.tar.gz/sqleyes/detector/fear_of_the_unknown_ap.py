"""Fear of the Unknown anti-pattern detector class"""
import re
from sqleyes.detector.abstract_ap import APDetector
from sqleyes.detector.detector_output import DetectorOutput


class FearOfTheUnknownApDetector(APDetector):
    type = "Fear of the Unknown"

    def __init__(self, query):
        super().__init__(query)

    def check(self):
        patterns = [re.compile(r'<>\s*NULL', re.IGNORECASE),
                    re.compile(r'!=\s*NULL', re.IGNORECASE),
                    re.compile(r'=\s*NULL', re.IGNORECASE)]
        for pattern in patterns:
            if pattern.search(self.query):
                return DetectorOutput(detector_type=self.detector_type,
                                      type=self.type)

        return None
