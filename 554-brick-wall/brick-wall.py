class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hashmap={0:0}
        for i in range(len(wall)):
            count=0
            for j in range(len(wall[i])-1):
                count+=wall[i][j]
                if count not in hashmap:
                    hashmap[count]=1
                else:
                    hashmap[count]+=1
        maxi=0
        for i,j in hashmap.items():
            maxi=max(j,maxi)
        return len(wall)-maxi

        