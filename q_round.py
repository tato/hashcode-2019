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

if 0:
    tags = set()
    for p in photos:
        tags = tags.union(set(p.tags))
    tags_ids = dict()
    for i,t in enumerate(tags):
        tags_ids[t] = i
    for p in photos:
        tags_as_ids = [ tags_ids[t] for t in p.tags ]
        p.tags = tags_as_ids


horizontals = [ p for p in photos if p.orient == 'H' ]
verticals = [ p for p in photos if p.orient == 'V' ]

slides = []
if len(horizontals) > 0:
    slides = [ horizontals[0] ]
    del horizontals[0]

    def compare(xs, ys):
        common = 0
        for x in xs.tags:
            if x in ys.tags:
                common += 1
        return min(len(xs.tags)-common, len(ys.tags)-common, common)

    while len(horizontals) > 0:
        previous = slides[len(slides)-1]
        best = sorted(horizontals[:100], key=lambda p: compare(p, previous))[-1]
        slides.append(best)
        horizontals.remove(best)
        #print("{} slides, {} photos".format(len(slides), len(photos)))

print(len(slides) + len(verticals)//2)

for s in slides:
    print(s.id)

for i in range(0, len(verticals)//2*2, 2):
    print(str(verticals[i].id) + ' ' + str(verticals[i+1].id))

