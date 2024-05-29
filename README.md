# Extensible design patterns for Python

Exploration of extensible design patterns in Python, heavily influenced by Amir Rachum's wonderful
["Python Entry Points Explained"](https://amir.rachum.com/python-entry-points/) article.

Further reading:
- Architecture Patterns with Python (repository pattern): https://www.cosmicpython.com/book/chapter_02_repository.html

## Context

It's been 7 glorious years since “Snek Semiconductors and Software, Incorporated” and their
subsidiary “Snek Pro Solutions and Consultation Services” cornered the global snek market with an extensible
command line tool that brought sneks right into the homes of millions. However, whilst you, as Benevolent Dictator for Life, 
have been resting on your laurels in the Bahamas, the world has moved on and your new CEO and VP R&D have been 
begging you for months to come back to the office and help them do the same.

As you arrive at Snek HQ, you see your VP R&D lambasting the company's current set of snek offerings whilst new 
competitors have adopted distributed systems and microservices for on-demand snek delivery.

_"Customers these days don't want to **install** new sneks, they want to **download** them from the internet! We should be leading
the market in web-based SaaS (Sneks as a Service) solutions, rather than focussing on desktop applications."_

Intrigued, you listen in on the conversation as a product owner tries to defend the current strategy:

_"But our customers have always installed sneks and accessed them via a command line tool. In this new design,
where would they get them from?"_

_"A remote snek data store that can be accessed via a HTTP API."_

A member of the cyber-security team wades in:

_"But our customers are very concerned about the privacy of their sneks. They want to be able to share sneks
internally without risking IP leakage across the open internet. The current market-leading SaaS solutions don't cater
for this level of data security."_

_"That's fine, we'll sell them their own SaaS platform that they can deploy internally. Their users will still get
the same product, it'll just be managed by their own internal IT group, rather than by us."_

Eventually, an unconvinced engineering manager steps forward:

_"But our existing customers' IT departments have differing policies over the kind of technologies that they can 
adopt internally. How can we cater for this?"_

_"Well we might not be able to cater for every scenario, but in that case our customers should be able to contribute 
their own snek data stores, just as they were able to contribute their own sneks."_

You slip away before being pulled into the conversation, both excited by the VP R&D's vision but also weary about the
leap into uncharted territory that it may require.


# Installation Guide

### Build environment
```commandline
python -m venv --clear --upgrade-deps .venv
```

### Activate environment
On Unix:
```commandline
source .venv/bin/activate
```
On Windows:
```commandline
.venv/bin/activate.bat
```

### Install package
```commandline
(.venv) pip install -e .
```

### Run the snek server
In one terminal:
```commandline
(.venv) uvicorn --factory snek_lib.server.app:create_app
```

### Run the snek client
In another terminal:
```commandline
(.venv) snek [--type] SNEK_NAME
```