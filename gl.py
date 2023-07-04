import gitlab
from pprint import pprint
gl = gitlab.Gitlab.from_config('gitlab.cn', [r'C:\Users\chenj82\.python-gitlab.cfg'])

# users = gl.users.list()
# for u in users:
#     print(u.username)

groups = gl.groups.list()
for group in groups:
    members = group.members.list()
    for m in members:
        print(m.email)
