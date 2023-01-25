stops = ["Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]
#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverly")
# # #2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
# # #3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")  
# print(stops)
print(stops) 
# 4. Print out the index position of "Linlithgow"
stop = "Linlithgow"
Lin = stops.index("Linlithgow")
print(Lin)
# #5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
# #6. Delete "Cumbernauld" from the list by index
stop = "Cumbernauld"
Cumb = stops.index("Cumbernauld")
stops.pop(2)
# #7. Print the number of stops there are in the list
total_stops = 0

for stop in stops:
    total_stops = total_stops+1

print(stops) 
print("Number of STOPS on the way to the capital are", total_stops)

# #8. Sort the list alphabetically
stops.sort()
# #9. Reverse the positions of the stops in the list
stops.reverse()
# #10 Print out all the stops using a for loop
print(stops)


# PythonMethods
# https://docs.python.org/3/tutorial/datastructures.html
# quiz
# https://docs.google.com/forms/d/e/1FAIpQLSc0FNd66FGGdtQMRC6_fx5r3mp6zGA3EP2e1VoImdqS2FcAiA/viewform
