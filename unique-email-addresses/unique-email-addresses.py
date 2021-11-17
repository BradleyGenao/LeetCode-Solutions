class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        """
        Step 1: Iterate through emails
        Step 2: grab email and parition at @
        Step 3: remove all "." and partition out the right side of +
        Step 4: Add back together and to dic increasing the count
        
        """
        
        
        email_count = collections.defaultdict(int)
        for email in emails:
            local, _ , domain = email.partition('@')
            local = local.replace('.', '')
            left, _, _ = local.partition('+')
            cleaned_email = left + '@' + domain
            email_count[cleaned_email] += 1
        return len(email_count) 


        