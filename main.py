from art import logo

print(logo)

# Variable declaration
start = True
auction_dict = {}

# Auction calculator
def auction(data: dict):
  highest_bid = 0
  bidder_name = ""
  for key in data:
    if data[key] >= highest_bid:
      highest_bid = data[key]
      bidder_name = key
  return f"{bidder_name} is the higest bidder with {highest_bid}"


def bidder():
  name = input("What is your name: ")
  try:
    price = int(input("What is your bid price?: "))
    auction_dict[name] = price
  except ValueError as ve:
    print(f"Caught ValueError - {ve}")
    
while start:
  bidder()
  try:
    restart = int(input("1. Continue\n2. Exit"))
    if restart == 2:
      result = auction(auction_dict)
      print(result)
      start = False
  except ValueError as ve:
    print(f"Caught ValueError - {ve}")
  
  