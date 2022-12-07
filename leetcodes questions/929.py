class Solution(object):
    def numUniqueEmails(self, emails):
        emailsHash, res = {}, 0
        
        for email in emails:
            splitEmail = email.split('@') 
            localName = splitEmail[0].split('+')[0].replace('.','')
            domainName = splitEmail[1]
            cleanEmail = localName + '@' + domainName
            emailsHash[(cleanEmail)] = 1 + emailsHash.get(cleanEmail, 0)
            
        return len(emailsHash)

# Adamın çözdüğü
# Çözüm sayısı 0 | Hedef 5 çözüm
class Solution(object):
    def numUniqueEmails(self, emails):
        emailsHash = set()
        
        for email in emails:
            i, local = 0, ''
            while email[i] not in ['@', '+']:
                if email[i] != '.':
                    local += email[i]
                i += 1
            
            while email[i] != '@':
                i += 1
            
            domain = email[i+1:]
            emailsHash.add((local, domain))
                
            
        return len(emailsHash)