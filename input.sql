INSERT INTO style(name)
VALUES
    ('rock'),
    ('rap'),
	  ('pop');

INSERT INTO artist(name, nickname)
VALUES
    ('Freddie Mercury', 'Queen'),
    ('John Winston Ono Lennon', 'The Beatles'),
    ('Madonna Louise Ciccone', 'Madonna'),
    ('Marshall Bruce Mathers', 'Eminem');

INSERT INTO style_artist(style_id, artist_id)
VALUES
    (1, 1),
    (1, 2),
    (2, 4),
    (3, 3),
    (3, 2);

INSERT INTO album(name, date_create)
VALUES
    ('A Kind of Magic', '1986-03-23'),
    ('Made in Heaven', '2020-04-23'),
    ('The Early Beatles', '1965-04-12'),
    ('Something New', '1964-05-20'),
    ('Like a Prayer', '1989-01-01'),
    ('Finally Enough Love', '2019-07-18'),
    ('The Eminem Show', '2002-09-12'),
    ('Recovery', '2010-04-10');

INSERT INTO album_artist(album_id, artist_id)
VALUES
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 2),
    (5, 3),
    (6, 3),
    (7, 4),
    (8, 4);

INSERT INTO track(name, duration, album_id)
VALUES
    ('One Vision', 310, 1),
    ('A Kind of Magic', 256, 1),
    ('One Year of Love', 230, 1),
    ('Its a Beautiful Day', 152, 2),
    ('Made in Heaven', 325, 2),
    ('Let Me Live', 285, 2),
    ('Love Me Do', 138, 3),
    ('Twist and Shout', 152, 3),
    ('Chains', 143, 3),
    ('Things We Said Today', 153, 4),
    ('Any Time at All', 130, 4),
    ('When I Get Home', 134, 4),
    ('Express Yourself', 479, 5),
    ('Love Song', 492, 5),
    ('Promise to Try', 215, 5),
    ('My Holiday', 200, 6),
    ('Into the Groove', 243, 6),
    ('Open Your Heart', 453, 6),
    ('Curtains Up', 29, 7),
    ('My White America', 124, 7),
    ('Business', 287, 7),
    ('Square Dance', 176, 7),
    ('Cold Wind Blows', 276, 8),
    ('On Fire', 365, 8);


INSERT INTO collection(name, date_create)
VALUES
    ('Classic Queen', '1995-04-23'),
    ('Greatest Hits III', '1990-02-20'),
    ('Rock ’n’ Roll Music', '1986-02-23'),
    ('A Collection of Beatles Oldies', '1980-11-02'),
    ('The Immaculate Collection', '2019-02-01'),
    ('The Best of MNM', '2022-05-07');

INSERT INTO track_collection(track_id, collection_id)
VALUES
    (1, 1),
    (3, 1),
    (4, 1),
    (2, 2),
    (3, 2),
    (4, 2),
    (7, 3),
    (8, 3),
    (9, 3),
    (8, 4),
    (9, 4),
    (10, 4),
    (13, 5),
    (16, 5),
    (20, 6),
    (21, 6),
    (22, 6);
