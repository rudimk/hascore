#!/usr/bin/env python

from coaster.manage import init_manager

from hascore.models import db
from hascore import app, init_for


if __name__ == '__main__':
    db.init_app(app)
    manager = init_manager(app, db, init_for)
    manager.run()
