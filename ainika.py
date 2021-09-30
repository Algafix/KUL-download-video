import requests as req
from io import BytesIO

url = 'https://cfvod.kaltura.com/scf/hls/p/2375821/sp/237582100/serveFlavor/entryId/1_06hj0nd9/v/1/ev/7/flavorId/1_4rs2zmht/name/a.mp4/seg-{segment}-v1-a1.ts?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvaGxzL3AvMjM3NTgyMS9zcC8yMzc1ODIxMDAvc2VydmVGbGF2b3IvZW50cnlJZC8xXzA2aGowbmQ5L3YvMS9ldi83L2ZsYXZvcklkLzFfNHJzMnptaHQvbmFtZS9hLm1wNC8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjMzMDgxMTM0fX19XX0_&Signature=dJw3IsvyeFnI30M1nep9GJkFEmfmU7UsrviLNWGudcbOsomI4pGijqG0Mf0h~-C1Xa-uuYlFSktU7WWfY0o2cUvvtc38eXLR3LOUTS-70Tb197~rX-hp7-kMtjcLXi9kr~Dd9X7EuNRQxtN-05S7h4bDYYkWgd4HJokB8IEm8UQeclwfL~gZpGqzxPqY3r0VRqh0-QVvZuvr-rkJfOT9xmzkU1EfYgnFx00VICNICW7PE5q~rmkjJHRVKjICqIaMWNpNyHdIVjHQJvEW8IsOsjfgKuWumLOkPNEC76sx7utEMl3mD5ZnB0IPrMq-Y5AzW57jrso~7gtsDvreVhY6xg__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A'

url1 = 'https://cfvod.kaltura.com/scf/hls/p/2375821/sp/237582100/serveFlavor/entryId/1_06hj0nd9/v/1/ev/7/flavorId/1_4rs2zmht/name/a.mp4/seg-11-v1-a1.ts?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvaGxzL3AvMjM3NTgyMS9zcC8yMzc1ODIxMDAvc2VydmVGbGF2b3IvZW50cnlJZC8xXzA2aGowbmQ5L3YvMS9ldi83L2ZsYXZvcklkLzFfNHJzMnptaHQvbmFtZS9hLm1wNC8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjMzMDgxMTM0fX19XX0_&Signature=dJw3IsvyeFnI30M1nep9GJkFEmfmU7UsrviLNWGudcbOsomI4pGijqG0Mf0h~-C1Xa-uuYlFSktU7WWfY0o2cUvvtc38eXLR3LOUTS-70Tb197~rX-hp7-kMtjcLXi9kr~Dd9X7EuNRQxtN-05S7h4bDYYkWgd4HJokB8IEm8UQeclwfL~gZpGqzxPqY3r0VRqh0-QVvZuvr-rkJfOT9xmzkU1EfYgnFx00VICNICW7PE5q~rmkjJHRVKjICqIaMWNpNyHdIVjHQJvEW8IsOsjfgKuWumLOkPNEC76sx7utEMl3mD5ZnB0IPrMq-Y5AzW57jrso~7gtsDvreVhY6xg__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A'


url2 = 'https://cfvod.kaltura.com/scf/hls/p/2375821/sp/237582100/serveFlavor/entryId/1_06hj0nd9/v/1/ev/7/flavorId/1_4rs2zmht/name/a.mp4/seg-12-v1-a1.ts?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvaGxzL3AvMjM3NTgyMS9zcC8yMzc1ODIxMDAvc2VydmVGbGF2b3IvZW50cnlJZC8xXzA2aGowbmQ5L3YvMS9ldi83L2ZsYXZvcklkLzFfNHJzMnptaHQvbmFtZS9hLm1wNC8qIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjMzMDgxMTM0fX19XX0_&Signature=dJw3IsvyeFnI30M1nep9GJkFEmfmU7UsrviLNWGudcbOsomI4pGijqG0Mf0h~-C1Xa-uuYlFSktU7WWfY0o2cUvvtc38eXLR3LOUTS-70Tb197~rX-hp7-kMtjcLXi9kr~Dd9X7EuNRQxtN-05S7h4bDYYkWgd4HJokB8IEm8UQeclwfL~gZpGqzxPqY3r0VRqh0-QVvZuvr-rkJfOT9xmzkU1EfYgnFx00VICNICW7PE5q~rmkjJHRVKjICqIaMWNpNyHdIVjHQJvEW8IsOsjfgKuWumLOkPNEC76sx7utEMl3mD5ZnB0IPrMq-Y5AzW57jrso~7gtsDvreVhY6xg__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A'



#r1 = req.get(url1)
#io_object1 = BytesIO(r1.content)

#r2 = req.get(url2)
#io_object2 = BytesIO(r2.content)

with open('test.ts', 'wb') as out_file:
    
    for i in range(1,10000):
        r = req.get(url.format(segment=i))
        if r.status_code == 404:
            print('I have finished xx')
            break
        elif r.status_code != 200:
            print('oooops, something went bad')
            print(f'I have died at segment {i}')
            break
        else:
            io_object = BytesIO(r.content)
            out_file.write(io_object.getbuffer())
            print(f'segment {i}', end = '\r')



