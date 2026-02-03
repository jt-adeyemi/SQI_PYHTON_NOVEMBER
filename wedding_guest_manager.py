# Scenario: You are managing a guest list for a high-profile wedding. You have two lists: one for the 
# confirmed guests and another for the waitlisted guests. The couple wants a simple wedding with close friends and family in attendance so there is room for only 10 guests. Follow the instructions to manage the guest lists accordingly. Write the program in a file `wedding_guest_manager.py`.
# Currently, Alice, Charlie, Eve, Bob, Frank, Grace, David, Hannah, Liam and Mia have accepted invitations to the wedding and are on the confirmed_guests list. The confirmed_guests list is full. New guests who accept the invitation will be waitlisted.
# Three siblings Ken, Jack and Ivy accept the invitation but are put on the waitlist.
# Noah, the groom’s ex-classmate in the university and Oliver who lives next door to the bride have accepted the invitation. Put them on the waitlist.
# Alice has a family emergency and won’t be able to attend the wedding, She cancels her attendance. Remove Alice from the confirmed guest list and add the first person from the waitlist to the confirmed list. 
# Charlie is the godfather of the groom and he is the one funding the wedding. Therefore he is a VIP guest and the couple has asked you to make sure he is on the guestlist. Check whether or not Charlie is on the guestlist.
# David and Eve have decided they no longer want to attend the wedding and therefore cancel their attendance. Remove them from the confirmed_guests list. 
# Move the first 2 people on the waitlist into the guestlist to fill up the newly freed slots.
# Oliver just realized the day of the wedding is the same day he has to take his pet to see the vet and he cancels his attendance. Remove him from the waitlist.
# The event planner has asked you for the names of the last 3 guests on the guest list because she needs to make additional arrangements for them. Get her this information.
# The bride and groom have decided that they want to allow room for 5 more people to attend their wedding. Move 
# 	waitlisted guest (Noah) into the confirmed_guests list.
# 11. 	The event planner wants a report on the number of people who will be attending the wedding. Give her this information.
# 12. 	The event planner has also requested that you give her a list of all the names of the confirmed_guests. 
# The guests would be seated alphabetically at the venue and so she wants the names in alphabetical order.
# 13. 	A new guest called Collins who is the son of Grace and Noah would be attending on their behalf, Replace Grace and Noah 
# 	on the confirmed_guests list with Collins. Make sure you re-sort the list.
# 14. 	The caterer has also requested for the confirmed_guests list so she can provide the guests with customized bags 
# 	containing their food with their names on it. Give her a copy of the confirmed_guests list titled 
# 	guests_list_for_caterer`.
# 15. 	The deadline for accepting the invitations sent has now passed. There is no more need for the waitlist. 	Clear the 
# 	waitlist.

# At every stage from numbers 1 to 15, print out the following like so:
# print(“\n\nStage X”)
# print(“Confirmed guests: ”, confirmed_guests)
# print(“Waitlist: ”, waitlist)
# X means the current stage i.e. 1, 2, etc. If the question requests for some particular info apart from the content of confirmed_guests and waitlist such as numbers 5, 9 and 11, print it under the three lines above.

# Stage 1
print('\n\nStage 1')
confirmed_guests = ['Alice', 'Charlie', 'Eve', 'Bob', 'Frank', 'Grace','David', 'Hannah', 'Liam', 'Mia']
print('Confirmed guests: ', confirmed_guests)
print('The number of confirmed guests attending the wedding is: ', len(confirmed_guests))
waitlist = []
print('Waitlist: ', waitlist)

# Stage 2
print('\n\nStage 2')
waitlist = ['Ken', 'Jack', 'Ivy']
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

#Stage 3
print('\n\nStage 3')
waitlist.append('Noah')
waitlist.append('Oliver')
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 4
print('\n\nStage 4')
confirmed_guests.remove('Alice')
confirmed_guests.append(waitlist.pop(0))
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 5
print('\n\nStage 5')
vip = 'Charlie' in confirmed_guests
print(f'It is {vip} that Charlie is on the guestlist')
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 6
print('\n\nStage 6')
confirmed_guests.remove('David')
confirmed_guests.remove('Eve')
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 7
print('\n\nStage 7')
confirmed_guests.append(waitlist.pop(0))
confirmed_guests.append(waitlist.pop(0))
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 8
print('\n\nStage 8')
waitlist.remove('Oliver')
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 9
print('\n\nStage 9')
last_three_guests = confirmed_guests[-3:]
print(f'The names of the last 3 guests on the guest list are: {last_three_guests}')
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 10
print('\n\nStage 10')
confirmed_guests.append(waitlist.pop(0))
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 11
print('\n\nStage 11')
event_planner_report = len(confirmed_guests)
print(f'The number of confirmed guests who will be attending the wedding is: {event_planner_report}')
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 12
print('\n\nStage 12')
event_planner_list = confirmed_guests.copy()
event_planner_list.sort()
print(f'These are the alphabetically sorted names of all the confirmed guests: {event_planner_list}')
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 13
print('\n\nStage 13')
confirmed_guests.remove('Grace')
confirmed_guests.remove('Noah')
confirmed_guests.append('Collins')
confirmed_guests.sort()
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 14
print('\n\nStage 14')
guests_list_for_caterer = confirmed_guests.copy()
print('Guest list for caterer: ', guests_list_for_caterer)
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)

# Stage 15
print('\n\nStage 15')
waitlist.clear()
print('Confirmed guests: ', confirmed_guests)
print('Waitlist: ', waitlist)
