import meraki

API_KEY = '741b15749edf33d60548fb40f3bc637081941385'

dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

# Organization ID
org_ID = dashboard.organizations.getOrganizations()

# Networks in Org
#network_ID = dashboard.organizations.getOrganizationNetworks(org_ID)

print (org_ID)
#print (network_ID)

