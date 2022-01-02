website=["Amazon","flipcart",'paytm']

#using list comrehensions, generate the below list]
#["www.amazon.com","www.flipkart.com","www.paytm.com"]


#using list comprehension
result=["www."+item+".com" for item in website]
print(result)


#Using list comprehensions
website=["Amazon","flipcart",'paytm','snapdeal']
extensions=['com','org','in']

result=["www."+web+"."+ext for web in website for ext in extensions]

print(result)

