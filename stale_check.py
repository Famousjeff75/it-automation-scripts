name = "Test User"
days_inactive = 30

if days_inactive > 90:
    print(name, "is stale: no login for", days_inactive, "days")
elif days_inactive > 60:
    print(name, "is at risk: no login for", days_inactive, "days")
else:
    print(name, "is active")