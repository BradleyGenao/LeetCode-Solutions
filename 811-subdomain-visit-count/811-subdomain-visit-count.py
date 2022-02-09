class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        counts = defaultdict(int)
        
        for string in cpdomains:
            count, domain = string.split()
            count = int(count)
            counts[domain] += count
            
            pos = domain.find('.') + 1
            while pos > 0:
                counts[domain[pos:]] += count
                pos = domain.find('.', pos) + 1
        
        for d, c in counts.items():
            yield ''.join(str(c) + ' ' + d)
        
            
        