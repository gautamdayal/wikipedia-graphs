import wikipedia as wp
import queue


class Searcher:
    def __init__(self):
        pass

    def search(self, source, breadth, depth):
        dict = {}
        q = []
        q.append(source)
        for i in range(0, breadth * depth):
            page = q.pop(0)
            try:
                page = wp.WikipediaPage(page)
            except Exception:
                return dict
            dict[page.title] = page.links[:breadth]
            for p in dict[page.title]:
                q.append(p)


        return dict
