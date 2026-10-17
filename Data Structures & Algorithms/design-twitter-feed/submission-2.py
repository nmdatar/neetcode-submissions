class Twitter:

    def __init__(self):
        self.users_posts = defaultdict(list)
        self.users_following = defaultdict(set)
        self.t = 0
        self.limit = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users_posts[userId].append([-self.t, tweetId])
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users_following[userId]:
            self.users_following[userId].add(userId)
        
        idx = {user: len(self.users_posts[user]) - 1 for user in self.users_following[userId]}
        feed = []
        recent = []

        for user in self.users_following[userId]:
            if idx[user] >= 0:
                t, tweet_id = self.users_posts[user][idx[user]]
                heapq.heappush(recent, [t, tweet_id, user])

        while len(feed) < self.limit and len(recent) > 0:
            r = heapq.heappop(recent)
            feed.append(r[1])
            user = r[2]
            idx[user] -= 1
            if idx[user] >= 0:
                t, tweet_id = self.users_posts[user][idx[user]]
                heapq.heappush(recent, [t, tweet_id, user])
        
        return feed
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users_following[followerId]:
            self.users_following[followerId].remove(followeeId)
