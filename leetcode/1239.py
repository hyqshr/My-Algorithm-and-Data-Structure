class Solution:
    def maxLength(self, arr: List[str]) -> int:

        dp = [set()]

        for string in arr:

            # skip if word duplicate itself
            if len(set(string)) < len(string): continue
            string = set(string)

            for i in dp:
                # skip it if word duplicate
                if i & string: continue
                dp.append(i | string)

        # return max length
        return max([len(x) for x in dp])