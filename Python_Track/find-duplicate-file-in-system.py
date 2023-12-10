class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res={}
        for i in range(len(paths)):
            file=paths[i].split(" ")
            direct_path=file[0]
            for i in range(1,len(file)):
                file_name=file[i][:file[i].index("(")]
                file_content=file[i][file[i].index("(")+1:file[i].index(")")]
                path=direct_path+"/"+file_name
                if file_content in res:
                    res[file_content].append(path)
                else:
                    res[file_content]=[path]
        ans=[]
        for value in res.values():
            if len(value)>=2:
                ans.append(value)
        return ans
        