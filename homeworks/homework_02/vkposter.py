#!/usr/bin/env python
# coding: utf-8


import heapq


# первый лист - собственный пост; второй - прочитанные посты; третий - подписки


class VKPoster:

    def __init__(self):
        self.post_relationship = {}
        self.posts = {}

    def user_posted_post(self, user_id: int, post_id: int):
        self.post_id = post_id
        self.user_id = user_id
        self.posts[post_id] = 0
        if user_id not in self.post_relationship:
            self.post_relationship[user_id] = [[], [], []]
            self.post_relationship[user_id][0].append(post_id)
        else:
            self.post_relationship[user_id][0].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        if user_id not in self.post_relationship.keys():
            self.post_relationship[user_id] = [[], [], []]
            self.post_relationship[user_id][1] = [post_id]
        else:
            self.post_relationship[user_id][1].append(post_id)
        if post_id not in self.posts.keys():
            self.posts[post_id] = []
        if user_id not in self.posts[post_id]:
            self.posts[post_id].append(user_id)
        if post_id in self.post_relationship[user_id][1]:
            self.posts[post_id] += 1

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if follower_user_id in self.post_relationship.keys():
            self.post_relationship[follower_user_id][2].append(followee_user_id)
        else:
            self.post_relationship[follower_user_id] = [[], [], [], []]
            self.post_relationship[follower_user_id][2] = [followee_user_id]

    def get_recent_posts(self, user_id: int, k: int)-> list:
        temp = []
        for i in self.post_relationship[user_id][2]:
            for j in self.post_relationship[i][0]:
                temp.append(j)
        temp.sort(reverse=True)
        return temp[:k:]

    def get_most_popular_posts(self, k: int) -> list:
        list = []
        for key, val in self.posts.items():
            heapq.heappush(list, (val, key))
        return [s[1] for s in heapq.nlargest(k, list)]

    def print_VK(self):
        print("self.post_relationship: ", self.post_relationship, "\n", "self.posts: ", self.posts, "\n\n")


a = VKPoster()
for i in range(15):
    a.user_posted_post(i, 10+i)

for i in range(5):
    a.user_read_post(i, 10)
for i in range(8):
    a.user_read_post(i, 11)
for i in range(3):
    a.user_read_post(i, 17)

print(a.get_most_popular_posts(5))
