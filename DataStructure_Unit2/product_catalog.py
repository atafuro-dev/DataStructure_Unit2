from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
#print(products)

for product in products: 
    #setting the values of the dictionary ('products') & breaking them into pieces for later
    name = product["name"] #name of product
    tags = product["tags"] #name of preferences/tags associated with the products

    #print(name) #testing outputs here to see how it broke it down
    #print(tags)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    customer_preferences.append(preference )# Adds the customer preference to the list - adds inputted preference from user here
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences_set = set(customer_preferences) #converts to set - eliminated duplicates automatically

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    additional_product = { #is now saving it as a new product, not just listing it and discarding it immediately
        'name': product['name'], #saves the name
        'tags': set(product["tags"]) #saves the tags as sets
    }
    #print(product['name'], set(product["tags"])) 
    converted_products.append(additional_product) #adding the new product to the 'converted_products' list


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    matches = product_tags.intersection(customer_tags) #intersecting to compare customer tags and products and see what matches
    count = len(matches) #counting the actual number of matches found

    return count #shows us the count found

#matches = intersection of each (compares)
#count = len() of the intersection of each/matches


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    #then sort it

    recommendations = [] #creating the empty list to be added to 

    for product in products:
        product_name = product['name'] #gets the name
        product_tag = product['tags'] #gets the tags
        match_count = count_matches(product_tag, customer_tags) #counts matches between product tags and customer tags
        recommendations.append((match_count, product_name)) #adds to the new list of recommendations in the order of match count, then the name
    recommendations.sort(reverse=True) #sorts it by highest to lowest, resources used for this function
    return recommendations #shows the list

# TODO: Step 7 - Call your function and print the results

recommendations = recommend_products(
    converted_products, customer_preferences_set
)
print(recommendations) #calling on each seperate piece to find the final recommendation


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#   Some of the core operations I used included intersections (to match values and create the match_count), and loops to 
#   loop through whole lists, and later convert them into sets. The loops were also helpful when going through the user
#   quesiton and answer process provided. I also included the use of lists, sets, tuples, parameters, defining variables, and sorting. 
#   These each allowed me to break down the main products list into seperate sets - eliminating duplicates, which were later 
#   compared, sorted, and counted. These tools also allowed me to add values to sets when users input their own values/preferences as well.
#   Using all of these tools together allowed for a thorough, and cleaner, final product with an interactive portion.
# 2. How might this code change if you had 1000+ products?
#   This code could change if there were over 1000 products as it is a much larger data set, with many more possibilites and variables involved.
#   I am assuming the data would be more diverse, and not as straight forward. There also could be the issue of duplicates, or similar values that could call for
#   more thorough code or querying of the data itself. With the limited list, there were some areas that could be more general, but with many more products, it would need to
#   be more refined and specific to ensure accuracy, and efficiency as well. 
