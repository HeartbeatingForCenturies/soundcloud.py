import datetime
from dataclasses import dataclass
from typing import Optional, Tuple

from soundcloud.resource.base import BaseData
from soundcloud.resource.base_item import BaseItem
from soundcloud.resource.user import BasicUser, User
from soundcloud.resource.visuals import Visuals


@dataclass(frozen=True)
class Format(BaseData):
    """Track file format"""

    protocol: str
    mime_type: str


@dataclass(frozen=True)
class Transcoding(BaseData):
    """Available transcoding for track"""

    url: str
    preset: str
    duration: int
    snipped: bool
    format: Format
    quality: str


@dataclass(frozen=True)
class Media(BaseData):
    """List of available transcodings"""

    transcodings: Tuple[Transcoding, ...]


@dataclass(frozen=True)
class PublisherMetadata(BaseData):
    """Publisher info"""

    id: str
    urn: str
    contains_music: bool


@dataclass(frozen=True)
class BaseTrack(BaseItem):
    caption: Optional[str]
    commentable: bool
    comment_count: Optional[int]
    downloadable: bool
    download_count: Optional[int]
    full_duration: int
    has_downloads_left: bool
    playback_count: Optional[int]
    purchase_title: Optional[str]
    purchase_url: Optional[str]
    state: str
    streamable: bool
    urn: str
    visuals: Optional[Visuals]
    waveform_url: str
    media: Media
    station_urn: str
    station_permalink: str
    track_authorization: str
    monetization_model: str
    policy: str


@dataclass(frozen=True)
class Track(BaseTrack):
    """Track with full user info"""

    user: User


@dataclass(frozen=True)
class BasicTrack(BaseTrack):
    """Track with partial user info"""

    user: BasicUser


@dataclass(frozen=True)
class MiniTrack(BaseData):
    """Track with minimal info"""

    id: int
    kind: str
    monetization_model: str
    policy: str


@dataclass(frozen=True)
class CommentTrack(BaseData):
    """Track with partial info"""

    artwork_url: Optional[str]
    caption: Optional[str]
    id: int
    kind: str
    last_modified: datetime.datetime
    permalink: str
    permalink_url: str
    public: bool
    secret_token: Optional[str]
    sharing: str
    title: str
    uri: str
    urn: str
    user_id: int
    full_duration: int
    duration: int
    display_date: datetime.datetime
    media: Media
    station_urn: str
    station_permalink: str
    track_authorization: str
    monetization_model: str
    policy: str
    user: BasicUser
