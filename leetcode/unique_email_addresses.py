from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()

        for email in emails:
            temp = []
            domain_start = email.index('@')
            for i in range(len(email)):
                if email[i] == '@' or email[i] == '+':
                    break
                if email[i] != '.':
                    temp.append(email[i])
            e = ''.join(temp)+email[domain_start:]
            email_set.add(e)
        return len(email_set)


emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
solution = Solution().numUniqueEmails(emails)
print(solution)

