class Solution:
    def interpret(self, command: str) -> str:
        res=""
        for i in range(len(command)):
            if command[i] =="G":
                res+="G"
            if command[i] =="(":
                if command[i+1]==")":
                    res+="o"
                if command[i+1]=="a":
                    res+="al"
        return res