"""
Module to get videos data
"""
from dataclasses import dataclass
from typing import Any, Dict, List
from dataclasses_json import dataclass_json, LetterCase, Undefined, CatchAll
import deeplabel.client
import deeplabel
from deeplabel.exceptions import InvalidIdError
import deeplabel.infer.video_tasks
from deeplabel.basemodel import DeeplabelBase


class Video(DeeplabelBase):
    video_id: str
    title: str
    video_fps: float
    duration: float # in seconds
    input_url: str

    @classmethod
    def _from_search_params(cls, params:Dict[str, Any], client: "deeplabel.client.BaseClient") -> List["Video"]:
        resp = client.get("/videos", params=params)
        videos = resp.json()["data"]["videos"]
        videos = [cls(**video, client=client) for video in videos]
        return videos
    
    @classmethod
    def from_video_id(cls, video_id:str, client: "deeplabel.client.BaseClient")->"Video":
        video = cls._from_search_params({"videoId":video_id}, client=client)
        if not len(video):
            raise InvalidIdError(f"Failed to fetch video with videoId: {video_id}")
        return video[0]
    
    @classmethod
    def from_folder_id(cls, folder_id:str, client: "deeplabel.client.BaseClient")-> List["Video"]:
        return cls._from_search_params({"parentFolderId":folder_id}, client)
    
    @property
    def video_tasks(self):
        if hasattr(self, "_video_tasks"): return self._video_tasks
        self._video_tasks =  deeplabel.infer.video_tasks.VideoTask.from_video_id(self.video_id, self.client)
        return self._video_tasks

    def update_metadata(self, data: dict)->"Video":
        """Update metadata of this video and return new Video object from it
        Since update might not work for all fields, do check in the returned
        Video object if the desired change has taken effect.

        Returns:
            Video: New Video object of the returned data
        """
        data["videoId"] = self.video_id
        res = self.client.put("/metadata", json=data)
        video = res.json()["data"]
        return Video.from_dict(video)
