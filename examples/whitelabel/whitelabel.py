import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient(apikey='YOUR_SENDGRID_API_KEY')
# You can also store your API key an .env variable 'SENDGRID_API_KEY'

##################################################
# Create a domain whitelabel. #
# POST /whitelabel/domains #

data = {'sample': 'data'}
response = sg.client.whitelabel.domains.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List all domain whitelabels. #
# GET /whitelabel/domains #

params = {'username': 'test_string', 'domain': 'test_string', 'exclude_subusers': 0, 'limit': 0, 'offset': 0}
response = sg.client.whitelabel.domains.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Get the default domain whitelabel. #
# GET /whitelabel/domains/default #

response = sg.client.whitelabel.domains.default.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# List the domain whitelabel associated with the given user. #
# GET /whitelabel/domains/subuser #

response = sg.client.whitelabel.domains.subuser.get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Disassociate a domain whitelabel from a given user. #
# DELETE /whitelabel/domains/subuser #

response = sg.client.whitelabel.domains.subuser.delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a domain whitelabel. #
# PATCH /whitelabel/domains/{domain_id} #

data = {'sample': 'data'}
domain_id = "test_url_param"
response = sg.client.whitelabel.domains._(domain_id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a domain whitelabel. #
# GET /whitelabel/domains/{domain_id} #

domain_id = "test_url_param"
response = sg.client.whitelabel.domains._(domain_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a domain whitelabel. #
# DELETE /whitelabel/domains/{domain_id} #

domain_id = "test_url_param"
response = sg.client.whitelabel.domains._(domain_id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Associate a domain whitelabel with a given user. #
# POST /whitelabel/domains/{domain_id}/subuser #

data = {'sample': 'data'}
domain_id = "test_url_param"
response = sg.client.whitelabel.domains._(domain_id).subuser.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Add an IP to a domain whitelabel. #
# POST /whitelabel/domains/{id}/ips #

data = {'sample': 'data'}
id = "test_url_param"
response = sg.client.whitelabel.domains._(id).ips.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Remove an IP from a domain whitelabel. #
# DELETE /whitelabel/domains/{id}/ips/{ip} #

id = "test_url_param"
        ip = "test_url_param"
response = sg.client.whitelabel.domains._(id).ips._(ip).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Validate a domain whitelabel. #
# POST /whitelabel/domains/{id}/validate #

data = {'sample': 'data'}
id = "test_url_param"
response = sg.client.whitelabel.domains._(id).validate.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Create an IP whitelabel #
# POST /whitelabel/ips #

data = {'sample': 'data'}
response = sg.client.whitelabel.ips.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all IP whitelabels #
# GET /whitelabel/ips #

params = {'ip': 'test_string', 'limit': 0, 'offset': 0}
response = sg.client.whitelabel.ips.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve an IP whitelabel #
# GET /whitelabel/ips/{id} #

id = "test_url_param"
response = sg.client.whitelabel.ips._(id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete an IP whitelabel #
# DELETE /whitelabel/ips/{id} #

id = "test_url_param"
response = sg.client.whitelabel.ips._(id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Validate an IP whitelabel #
# POST /whitelabel/ips/{id}/validate #

data = {'sample': 'data'}
id = "test_url_param"
response = sg.client.whitelabel.ips._(id).validate.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Create a Link Whitelabel #
# POST /whitelabel/links #

data = {'sample': 'data'}
params = {'limit': 0, 'offset': 0}
response = sg.client.whitelabel.links.post(request_body=data, query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve all link whitelabels #
# GET /whitelabel/links #

params = {'limit': 0}
response = sg.client.whitelabel.links.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a Default Link Whitelabel #
# GET /whitelabel/links/default #

params = {'domain': 'test_string'}
response = sg.client.whitelabel.links.default.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve Associated Link Whitelabel #
# GET /whitelabel/links/subuser #

params = {'username': 'test_string'}
response = sg.client.whitelabel.links.subuser.get(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Disassociate a Link Whitelabel #
# DELETE /whitelabel/links/subuser #

params = {'username': 'test_string'}
response = sg.client.whitelabel.links.subuser.delete(query_params=params)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Update a Link Whitelabel #
# PATCH /whitelabel/links/{id} #

data = {'sample': 'data'}
id = "test_url_param"
response = sg.client.whitelabel.links._(id).patch(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Retrieve a Link Whitelabel #
# GET /whitelabel/links/{id} #

id = "test_url_param"
response = sg.client.whitelabel.links._(id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Delete a Link Whitelabel #
# DELETE /whitelabel/links/{id} #

id = "test_url_param"
response = sg.client.whitelabel.links._(id).delete()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Validate a Link Whitelabel #
# POST /whitelabel/links/{id}/validate #

data = {'sample': 'data'}
id = "test_url_param"
response = sg.client.whitelabel.links._(id).validate.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Associate a Link Whitelabel #
# POST /whitelabel/links/{link_id}/subuser #

data = {'sample': 'data'}
link_id = "test_url_param"
response = sg.client.whitelabel.links._(link_id).subuser.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

