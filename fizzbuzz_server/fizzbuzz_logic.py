from collections import Counter

request_stats_counter = Counter()


def get_result(int1, int2, limit, str1, str2):

    global request_stats_counter
    params = (int1, int2, limit, str1, str2)
    request_stats_counter[params] += 1

    result = ""
    for i in range(1, limit + 1):
        res = ''
        if i % int1 == 0:
            res += str1
        if i % int2 == 0:
            res += str2
        if not res:
            res += str(i)
        if i != limit:
            result += res + ','
        else:
            result += res

    return result


def get_stats():

    global request_stats_counter
    if not request_stats_counter:
        return {'stats message': 'No requests'}

    most_frequent_request, hits = request_stats_counter.most_common(1)[0]
    return {'most_frequent_request': most_frequent_request, 'hits': hits}

