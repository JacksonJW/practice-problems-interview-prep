# Every email consists of a local name and a domain name, separated by the @ sign.

# For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

# Besides lowercase letters, these emails may contain '.'s or '+'s.

# If you add periods('.') between some characters in the local name part of an email address, mail
# sent there will be forwarded to the same address without dots in the local name.  For example,
# "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this
# rule does not apply for domain names.)

# If you add a plus('+') in the local name, everything after the first plus sign will be ignored.
# This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to
# my@email.com.  (Again, this rule does not apply for domain names.)

# It is possible to use both of these rules at the same time.

# Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails?


# Example 1:

# Input: ["test.email+alex@leetcode.com",
#         "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


# Note:

# 1 <= emails[i].length <= 100
# 1 <= emails.length <= 100
# Each emails[i] contains exactly one '@' character.
# All local and domain names are non-empty.
# Local names do not start with a '+' character.

# The time complexity of the solution below is O(C) where C is the size of the content (# of input emails and the total letters)


def numUniqueEmails(emails):
    unique_emails = set()
    for email in emails:
        i = 0
        new_email = ""
        local_name = True
        while i < len(email):
            if email[i] == "." and local_name == True:
                i += 1
            elif email[i] == "+" and local_name == True:
                while email[i] != "@":
                    i += 1
            elif email[i] == "@":
                local_name = False
                new_email += email[i]
                i += 1
            else:
                new_email += email[i]
                i += 1

        if new_email not in unique_emails:
            unique_emails.add(new_email)

    return len(unique_emails)


print("The expected result is 2 and the actual result is " + str(numUniqueEmails(["test.email+alex@leetcode.com",
                                                                                  "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])))
