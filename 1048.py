class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda w: -len(w))
        max_chain = 1
        hashed = {}
        for i, word in enumerate(words):
            max_chain = max(Solution.traverse(word, words[i+1:], hashed) + 1, max_chain)
        return max_chain

    def traverse(word: str, words: list[str], hashed: Dict[Tuple[str, str], int]) -> int:
        max_chain = 0
        for i, comp in enumerate(words):
            if len(comp) == len(word):
                continue
            if len(comp) + 1 != len(word):
                break
            if Solution.is_predecessor(comp, word):
                if (comp, word) in hashed:
                    s = hashed[(comp, word)]
                else:
                    s = Solution.traverse(comp, words[i+1:], hashed) + 1
                    hashed[(comp, word)] = s
                max_chain = max(s, max_chain)
        return max_chain

    def is_predecessor(pre: str, post: str) -> bool:
        used_skip = False
        pre_index = 0
        post_index = 0
        while len(pre) > pre_index:
            if pre[pre_index] != post[post_index]:
                if used_skip:
                    return False
                else:
                    used_skip = True
                    pre_index -= 1
            pre_index += 1
            post_index += 1
        if used_skip:
            return len(post) == post_index
        else:
            return len(post) == post_index + 1
