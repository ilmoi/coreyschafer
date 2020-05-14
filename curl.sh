# just get a json
curl https://api.exchangeratesapi.io/latest

# get a json + information about your request aka:
"""
HTTP/2 200
date: Sun, 19 Apr 2020 15:22:15 GMT
content-type: application/json
set-cookie: __cfduid=d12a37d93ca67582faae5b856836762731587309735; expires=Tue, 19-May-20 15:22:15 GMT; path=/; domain=.exchangeratesapi.io; HttpOnly; SameSite=Lax
vary: Accept-Encoding
access-control-allow-origin: *
access-control-allow-credentials: true
access-control-allow-methods: GET
cache-control: max-age=1800
cf-cache-status: HIT
age: 1333
expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
server: cloudflare
cf-ray: 58679eb72e85b49c-RIX
cf-request-id: 0234a1867a0000b49c5c32b200000001
"""
# -i is full for "--include"
curl -i url

# to post data (d for data)
curl -d "first=ilja&last=moi" url

# to update data
curl -X PUT -d "first=ilja&last=moi" url

# to delete data
curl -X DELETE url

# sometimes routes require authentication
curl -u login_name:login_pass url

# sometimes we want to get back the enitre file at a link (aka downdload it)
# just hitting the link directly wont do any good (we'll get pure bytes)
# so instead we need do -o for --output
curl -o test.jpg url
open test.jpg
