# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails 
# representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts 
# have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely 
# have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. 
# The accounts themselves can be returned in any order.

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # construct a dictionary of emails
        emails_dict = {}
        for i, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email in emails_dict:
                    emails_dict[email].append(i)
                else:
                    emails_dict[email] = [i]

        # DFS over accounts to find connected components
        def scan_emails(idx, emails):
            for email in emails:
                for tmp_account in emails_dict[email]:
                    if tmp_account == idx or visited[tmp_account] == 1:
                        continue
                    
                    tmp_emails = accounts[tmp_account][1:]
                    merged_accounts[idx].update(tmp_emails)
                    visited[tmp_account] = 1
                    scan_emails(idx, tmp_emails)

        visited = [0] * len(accounts)
        merged_accounts = {}
        for account_idx in range(len(accounts)):
            if visited[account_idx] == 1:
                continue
                
            emails = accounts[account_idx][1:]
            merged_accounts[account_idx] = set(emails)
            visited[account_idx] = 1
            scan_emails(account_idx, emails)

        # re-format merged accounts
        ret = []
        for idx in merged_accounts:
            emails = merged_accounts[idx]
            ret.append([accounts[idx][0]] + sorted(list(emails)))
        return ret






