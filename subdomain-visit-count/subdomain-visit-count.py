class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counts= collections.defaultdict(int)
        
        for domains in cpdomains:
            score, _, domain = domains.partition(' ')
            score = int(score)
            
            domain_counts[domain] += score
            
            for i, char in enumerate(domain):
                if char == '.':
                    elem = domain[i+1:]
                    domain_counts[elem] += score
        res = []
        for key, value in domain_counts.items():
            res.append(str(value) + ' ' + key)
        return res