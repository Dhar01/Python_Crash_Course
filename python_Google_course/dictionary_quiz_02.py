def groups_per_user(group_dictionary):
    users_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user in users_groups:
                users_groups[user].append(group)
            else:
                users_groups[user] = [group]
    
    return(users_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))