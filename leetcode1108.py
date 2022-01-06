def defangIPaddr(address):
   ans = address.replace(".","[.]")
   return address

address = "1.1.1.1"
print(defangIPaddr(address))