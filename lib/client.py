from clip_client import Client

from lib.utils import get_clip_server_address


def get_client() -> Client:
    c = Client('grpc://' + get_clip_server_address())
    c.profile()
    return c

def encode():
    c = get_client()
    r = c.encode(
        [
            'First do it',
            'then do it right',
            'then do it better',
            'https://picsum.photos/200',
        ]
    )
    print(r)