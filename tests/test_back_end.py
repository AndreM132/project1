import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Lists, Games
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        
        update=Lists(first_name="Andre",last_name="Moses",list_title="My List",list_description="description",favourites="PS4")
        
        addgame=Games(games_id="2", games_title='Mortal Kombat 11')

        newgame=Games(games_id="1",games_title="Ratchet and Clank",age_rating="3",games_price="20",games_description="new game",console_title="PS4")


    




    def tearDown(self):

        db.session.remove()
        db.drop_all()



class TestViews(TestBase):

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_gamesview_view(self):
        response = self.client.get(url_for('gamesconsoles'))
        self.assertEqual(response.status_code, 200)

    def test_aboutview_view(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_listsview_view(self):
        response = self.client.get(url_for('lists'))
        self.assertEqual(response.status_code, 200)




class TestGames(TestBase):

    def test_add_new_game(self):
        with self.client:
            response = self.client.post(
                '/gamesconsoles',
                data=dict(
                    games_title="Ratchet and Clank",
                    age_rating="3",
                    games_price="20",
                    games_description="new game",
                    console_title="PS4"
                ),
                follow_redirects=True
            )
            self.assertIn(b'Ratchet and Clank', response.data)
            print(response.data)


    def test_add_game_tolist(self):

        with self.client:
            response = self.client.post(
                    '/addgame/1',
                    data=dict(
                        games_id="1",
                        games_title="Ratchet and Clank"
                    ),
                    follow_redirects=True
            )
            self.assertIn(b'1', response.data)

class TestLists(TestBase):

    def test_add_lists(self):

        with self.client:
            response = self.client.post(
                    '/lists',
                    data=dict(
                        first_name="Andre",
                        last_name="Moses",
                        list_title="New List",
                        list_description="description",
                        favourites="PS4",
                    ),
                    follow_redirects=True
            )
            self.assertIn(b'Andre', response.data)

    def test_add_lists2(self):

        with self.client:
            response = self.client.post(
                    '/lists',
                    data=dict(
                        first_name="Nadia",
                        last_name="Moses",
                        list_title="Games list",
                        list_description="description",
                        favourites="PS4",
                    ),
                    follow_redirects=True
            )
            self.assertIn(b'Nadia', response.data)

    def test_add_check_lists(self):

        with self.client:
            response = self.client.post(
                    '/lists',
                    data=dict(
                        list_title="New List"
                    ),
                    follow_redirects=True
            )
            self.assertIn(b'New List', response.data)



    def test_update_lists(self):

        with self.client:
            response = self.client.post(
                    '/lists/update/1',
                    data=dict(
                        first_name="Andre",
                        last_name="Moses",
                        list_title="My List",
                        list_description="description",
                        favourites="PS4",
                        
                    ),   
                    follow_redirects=True
            )
            self.assertIn(b'name', response.data)

    def test_delete_lists(self):

        with self.client:
            response = self.client.post(
                    '/lists/delete/<int:list_id>',
                    data=dict(
                        list_id="1"
                    ),
                    follow_redirects=True
            )
            self.assertIn(b'1', response.data)


                







