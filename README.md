# Notice

This repo is an attempt to bring Dungeonomics into 2026, while also containerizing it for easy distribution.  There are currently many issues, and shouldn't be used for anything serious yet.

## Installation

I've drafted a few simple methods for getting Dungeonomics up and running; a docker compose, a kubernetes deployment, and a Helm chart.  The Helm chart is the currently expected installation method.  

### Build the Docker Image

For now, we are just going to use the dev tag since Dungeonomics is in the process of being heavily updated.

```
docker build -t dungeonomics:dev .
```

### Fetching the Postgres subchart

You'll need to tell helm to download and lock the current version of PostgreSQL (current v18).

```
helm dependency update ./dungeonomics-chart
```

### Switch from the external PostgreSQL to the Helm installed dependancy

In values.yaml, change:

```
useExternalPostgres: true
postgresql:
  enabled: false

database:
  host: generic-postgres-postgresql.default.svc.cluster.local
  port: 5432
  name: dungeonomics
  user: postgres
  password: postgres

# useExternalPostgres: false
# postgresql:
#   enabled: true
# 
#   auth:
#     database: dungeonomics
#     username: dungeonomics
#     password: dungeonomics
# 
#   primary:
#     persistence:
#       enabled: true
#       size: 5Gi
#
# database:
#  name: dungeonomics
#  host: dungeonomics-postgresql
#  port: 5432
#  user: postgres
#  password: postgres
```

to

```
# useExternalPostgres: true
# postgresql:
#   enabled: false

# database:
#   host: generic-postgres-postgresql.default.svc.cluster.local
#   port: 5432
#   name: dungeonomics
#   user: postgres
#   password: postgres

useExternalPostgres: false
postgresql:
  enabled: true

  auth:
    database: dungeonomics
    username: dungeonomics
    password: dungeonomics

  primary:
    persistence:
      enabled: true
      size: 5Gi

database:
 name: dungeonomics
 host: dungeonomics-postgresql
 port: 5432
 user: postgres
 password: postgres
```

### Configure your Administrator

Within values.yaml, you'll find the administrator settings:

```
admin:
  username: admin
  email: admin@example.com
  password: changeme
```

Change these to whatever you wish.  You can access the admin panel by navigating to http:\\your-dungeonomics-instance\admin


### Install the chart

I suggest using the dungeonomics namespace; it'll make it easier to clean up.

```
helm install dungeonomics ./dungeonomics-chart -n dungeonomics --create-namespace
```

### Notes about New Users

New user creation works, but currently I've defaulted to just displaying the verification link in the console.  You'll need to view the logs of the dungenomics pod to get the link should you want to create a new user using the web form.  You can also just use the admin panel to bypass this entirely.