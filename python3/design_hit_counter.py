"""
Leetcode #362 Design Hit Counter

Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 

Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""
import collections


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hit_q = collections.deque()
        self.hit_count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if self.hit_q and self.hit_q[-1][0] == timestamp:
            self.hit_q[-1][1] += 1
        else:
            self.hit_q.append((timestamp, 1))

        self.hit_count += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.hit_q and self.hit_q[0][0] <= timestamp - 300:
            self.hit_count -= self.hit_q.popleft()[1]

        return self.hit_count


def main():
    counter = HitCounter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    print("Expected result is 3 and the Actual result is: " +
          str(counter.getHits(4)))
    counter.hit(300)
    print("Expected result is 4 and the Actual result is: " +
          str(counter.getHits(300)))
    print("Expected result is 3 and the Actual result is: " +
          str(counter.getHits(301)))
    counter.hit(301)
    print("Expected result is 1 and the Actual result is: " +
          str(counter.getHits(600)))


if __name__ == "__main__":
    main()
