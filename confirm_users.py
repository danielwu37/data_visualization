#验证用户
unconfirmed_users = ['alice', 'brian', 'candice']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print('Verifying user: ' + current_user.title())
	confirmed_users.append(current_user)
	
print('\nThe following user has been confirmed:')
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

