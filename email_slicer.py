input_email= input("Enter your e-mail address: ")
(username,domain) = input_email.split("@")
(domain,extension) = domain.split(".")
print("your username is:"+username ,"//your domain is :  "+ domain,"//your extension is:   ."+ extension)
