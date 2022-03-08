import aepp
from aepp import connector
import logging


class AccessControl:
    """
    Access Control API endpoints.
    Complete documentation is available:
    https://www.adobe.io/apis/experienceplatform/home/api-reference.html#!acpdr/swagger-specs/access-control.yaml
    """

    ## logging capability
    loggingEnabled = False
    logger = None

    def __init__(
        self,
        config: dict = aepp.config.config_object,
        header=aepp.config.header,
        loggingObject: dict = None,
        **kwargs,
    ) -> None:
        """
        Instantiate the access controle API wrapper.
        Arguments:
            config : OPTIONAL : config object in the config module. (DO NOT MODIFY)
            header : OPTIONAL : header object  in the config module. (DO NOT MODIFY)
            loggingObject : OPTIONAL : logging object to log messages.
        kwargs :
            header options
        """
        if loggingObject is not None and sorted(
            ["level", "stream", "format", "filename", "file"]
        ) == sorted(list(loggingObject.keys())):
            self.loggingEnabled = True
            self.logger = logging.getLogger(f"{__name__}")
            self.logger.setLevel(loggingObject["level"])
            formatter = logging.Formatter(loggingObject["format"])
            if loggingObject["file"]:
                fileHandler = logging.FileHandler(loggingObject["filename"])
                fileHandler.setFormatter(formatter)
                self.logger.addHandler(fileHandler)
            if loggingObject["stream"]:
                streamHandler = logging.StreamHandler()
                streamHandler.setFormatter(formatter)
                self.logger.addHandler(streamHandler)
        self.connector = connector.AdobeRequest(
            config_object=config,
            header=header,
            loggingEnabled=self.loggingEnabled,
            logger=self.logger,
        )
        self.sandbox = self.connector.config["sandbox"]
        self.header = self.connector.header
        self.header.update(**kwargs)
        self.endpoint = (
            aepp.config.endpoints["global"] + aepp.config.endpoints["access"]
        )

    def getReferences(self) -> dict:
        """
        List all available permission names and resource types.
        """
        if self.loggingEnabled:
            self.logger.debug(f"Starting getReferences")
        path = "/acl/reference"
        res = self.connector.getData(self.endpoint + path, headers=self.header)
        return res

    def postEffectivePolicies(self, listElements: list = None):
        """
        List all effective policies for a user on given resources within a sandbox.
        Arguments:
            listElements : REQUIRED : List of resource urls. Example url : /resource-types/{resourceName} or /permissions/{highLevelPermissionName}
        """
        if type(listElements) != list:
            raise TypeError("listElements should be a list of elements")
        if self.loggingEnabled:
            self.logger.debug(f"Starting postEffectivePolicies")
        path = "/acl/effective-policies"
        res = self.connector.postData(
            self.endpoint + path, data=listElements, headers=self.header
        )
        return res
