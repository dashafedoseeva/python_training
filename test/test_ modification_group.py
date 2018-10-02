def test_modification_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_group()
    app.session.logout()
