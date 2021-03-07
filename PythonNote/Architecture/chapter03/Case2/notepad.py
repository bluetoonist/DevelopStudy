
import textsearcher
from unittest.mock import Mock, MagicMock
import operator

db = Mock()
search = textsearcher.TextSearcher(db)

db.connect.assert_called_with()
search.setup(cache=True, max_items=100)
search.db.configure.assert_called_with(max_items=100)

canned_results = [("Python is wonderful", 0.4),
                  ("I Like Python", 0.8),
                  ("Python is easy",0.5),
                  ("Python Can be learnt in an afternoon!",0.3)
                  ]

db.query = MagicMock(return_value=canned_results)

keyword, num = "Python", 3
data = search.get_results(keyword="Python", num=num)
print(data)

search.db.query.assert_called_with(keyword)
results = sorted(canned_results, key=operator.itemgetter(1),
                 reverse=True)[:num]

assert data == results
print(data == results)




