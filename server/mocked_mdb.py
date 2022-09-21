from dataclasses import dataclass
from dacite import from_dict
from typing import Optional


LECTURES_COLLECTION_FAKE_DATA = [
    {
        'id': 0,
        'author_name': 'ניסים אמון',
        'title': 'תרגול יומי לאושר, חכמת המזרח',
        'video_url': 'https://assets.screenz.live/media/2021/10/21/8a9ad4c5e90db27105433c724d05c30f6b7696be0ec29dd119d5fd903e3d.mp4',
        'video_thumbnail': 'https://images.eventer.co.il/screenzLiveCoverImage/069dedbb-c221-4c63-bd12-b1a06c0e9d02.jpg'
    },
]

@dataclass
class Lecture:
    id: int
    author_name: str
    title: str
    video_url: str
    video_thumbnail: str

class MockedMongoDB:
    def __init__(self, username: str = 'alon.y', password: str = 'Aa1234'):
        self.username = username
        self.password = password

        self.db_collection = LECTURES_COLLECTION_FAKE_DATA

    def find_one(self, obj: object) -> Optional[Lecture]:
        for rec in self.db_collection:
            if obj['id'] == rec['id']:
                return from_dict(data_class=Lecture, data=rec)

        return None

