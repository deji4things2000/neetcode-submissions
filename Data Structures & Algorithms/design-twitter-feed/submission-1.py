class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweet[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for timestamp, tweetId in self.tweet[userId]:
            heapq.heappush(heap, (-timestamp, tweetId))

        for followee in self.following[userId]:
            for timestamp, tweetId in self.tweet[followee]:
                heapq.heappush(heap, (-timestamp, tweetId))
        
        res = []
        
        while heap and len(res) <10:
            _, tweetId = heapq.heappop(heap)
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        