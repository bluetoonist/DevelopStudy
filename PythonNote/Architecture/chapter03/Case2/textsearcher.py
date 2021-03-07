import operator


class TextSearcher(object):

    def __init__(self, db):
        self.cache = False
        self.cache_dict = {}
        self.db = db
        self.db.connect()

    # 검색기를 설정하고 데이터 베이스 객체도 구성
    def setup(self, cache=False, max_items=500):
        self.cache = cache
        self.db.configure(max_items=max_items)

    # 데이터 소스를 사용해 검색을 수행한다. 주어진 키워드의 검색 결과를 반환한다.
    def get_results(self, keyword, num=10):

        if keyword in self.cache_dict:
            print("Form cache")
            return self.cache_dict[keyword]

        results = self.db.query(keyword)
        results = sorted(results, key=operator.itemgetter(1), reverse=True)[:num]

        if self.cache:
            self.cache_dict[keyword] = results

        return results
