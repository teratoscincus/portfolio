import os


def domain_name(request):
    return {"domain_name": os.environ["DOMAIN_NAME"]}


def site_owner(request):
    return {"site_owner": os.environ["SITE_OWNER"]}
