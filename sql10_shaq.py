"""given the dataset provided MOCK_DATA.csv, find out the following: 
- sort the IP addresses by the first three digits (network identifier) 
- What are all the domains in the emails (domain i.e. : @engadget.com)
- what is the most common domain name ? 
- Out of the emails create a dictionary of counts for the top level domain names (.com, .pl etc..)
```
{ '.com': 10, .... }
```

- Write a function called check_username that takes an email address and checks that the first letter matches the first letter of the name in the first name column and the rest of the string is from the last name 

def check_username(email, firstname, lastname):
"""""
import csv
from pprint import pprint
from collections import Counter
with open('mock_data.csv', newline='') as csvfile:
     data = csv.DictReader(csvfile)

     all_ip_addresses = []
     all_emails = []
     for row in data:
         all_ip_addresses.append(row['ip_address'])
         all_emails.append(row['email'])

     #part 1: sorted ip addresses


     sorted_ips = sorted(all_ip_addresses, key=lambda ip: int(ip.split('.')[0]))
    #  pprint(sorted_ips)


     #part 2: What are all the domains in the emails (domain i.e. :@ engadget.com)

     #helper function
     get_domain = lambda email : email.split('@')[1]

     # def get_domain(email):
     # 	return email.split('@')[1]

     distinct_domains = { get_domain(dom) for dom in all_emails }
     #print( set([ get_domain(dom) for dom in all_emails ]))
     #distinct_domains_list = set([ get_domain(dom) for dom in all_emails ])
     #pprint(distinct_domains)

     #part 3: What is the most common domain name ? (using counter)
     domain_counts = {}
     for dom in all_emails:
     	dom = get_domain(dom)
     	if dom not in domain_counts:
     		domain_counts[dom] = 0
     	domain_counts[dom] += 1
     pprint(sorted(domain_counts.items(), key=lambda entry:entry[1] ,reverse=True)[:5])

     #part 3 alt: What is the most common domain name ? (using counter)
     pprint(Counter(get_domain(dom) for dom in all_emails).most_common()[:3])

     #Part 4: Create a dictionary of counts for the top level domain names

     #helper function
     get_top_level_domain = lambda email : email.split('.')[-1]

     pprint(Counter(get_top_level_domain(dom) for dom in all_emails).most_common()[:3])

     """
 	Write a function called check_username that takes an email address and 
 	checks that the first letter matches the first letter of the name in the first name column and the rest of the string is from the last name

     """
     def check_username(email, firstname, lastname):
     	email = email.lower()
     	firstname = firstname.lower()
     	lastname = lastname.lower()
     	if email.startswith(firstname[:1]) and lastname in email:
     		return True
     	return False