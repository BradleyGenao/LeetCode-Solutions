class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        
        domains = {}
        
        for domain in cpdomains:
            
            num = int(domain.split()[0])
            item = domain.split()[1]
            
            if item in domains:
                domains[item] += num
            else:
                domains[item] = num
            
            for i in range(len(item)):
                if item[i] == '.':
                    elem = item[i+1:]
                    if elem in domains:
                        domains[elem] += num
                    else:
                        domains[elem] = num
        answer = []
        for key, value in domains.items():
            answer.append(str(value) + ' ' + key)
        return answer
        
        
        