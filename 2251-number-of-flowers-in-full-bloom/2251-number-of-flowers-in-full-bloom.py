class Solution:

    def search(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if target >= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return high + 1

    def fullBloomFlowers(self, flowers, people):
        n = len(flowers)
        bloom = [0] * n
        out = [0] * n

        # Storing the day when the flower bloomed and bloomed out.
        for i in range(n):
            bloom[i] = flowers[i][0]
            out[i] = flowers[i][1]

        # Sorting the days so that we can quickly search the day when the flower bloomed and bloomed out.
        bloom.sort()
        out.sort()

        n = len(people)
        result = [0] * n

        for i in range(n):
            # Searching how many flowers bloomed until the day people arrive to see.
            bloomed = self.search(bloom, people[i])

            # Searching how many flowers are bloomed out just before the day people arrive to see.
            bloomedOut = self.search(out, people[i] - 1)

            # Calculating the result.
            result[i] = bloomed - bloomedOut

        return result