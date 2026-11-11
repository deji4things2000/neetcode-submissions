class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            
            c = word[i]

            if c == ".":
                #Try every child
                for child in node.child.values():
                    if dfs(child, i+1) == True:
                        return True
                return False
            
            else:
                #normal character - must exist as a child
                if c not in node.child:
                    return False
                return dfs(node.child[c], i+1)
        return dfs(self.root, 0)
        
