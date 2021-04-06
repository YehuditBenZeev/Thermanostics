class PointLengthError(Exception):
    def __init__(self, message="not enough points"):
        super().__init__(message)


class HomographyError(Exception):
    def __init__(self, message="findHomography() returned an empty homography"):
        super().__init__(message)
