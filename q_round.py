n_photos = int(input().strip())
photos = list()

class Photo:
    def __init__(self, id, orient, tags):
        self.id = id
        self.orient = orient
        self.tags = tags

for i in range(n_photos):
    words = input().split()
    photos.append(Photo(i, words[0], words[2:]))


horizontals = [ p for p in photos if p.orient == 'H' ]
verticals = [ p for p in photos if p.orient == 'V' ]

print(len(horizontals) + len(verticals)//2)
for h in horizontals:
    print(h.id)
for i in range(0, len(verticals)//2*2, 2):
    print(str(verticals[i].id) + ' ' + str(verticals[i+1].id))
