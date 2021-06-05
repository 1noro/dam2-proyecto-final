USE DCHAN;

INSERT INTO BOARD(slug, name) VALUES('a', 'Anime & Manga');
INSERT INTO BOARD(slug, name) VALUES('b', 'Random');
INSERT INTO BOARD(slug, name) VALUES('g', 'Technology');
INSERT INTO BOARD(slug, name) VALUES('news', 'Current News');
INSERT INTO BOARD(slug, name) VALUES('vr', 'Retro Games');
INSERT INTO BOARD(slug, name) VALUES('wg', 'Wallpapers/General');
INSERT INTO BOARD(slug, name) VALUES('x', 'Paranormal');

INSERT INTO THREAD(id, subject, comment, fileurl, board)
    VALUES(
        1,
        'Alien Disclosure',
        'How do the vessels move without any visible propulsion system?',
        'https://dcdn.org/x/1622583515994s.jpg',
        'x'
    );

INSERT INTO THREAD(id, subject, comment, fileurl, board)
    VALUES(
        81930017,
        '/pcbg/ - PC Building General',
        '>UPGRADE & BUILD ADVICE\nPost build "list" or current specs including MONITOR\nConvient lister: https://pcpartpicker.com/\nProvide specific use cases (e.g. gaming, editing, rendering)\nState budget and region',
        'https://dcdn.org/g/1622853294379s.jpg',
        'g'
    );
INSERT INTO THREAD(id, subject, comment, fileurl, board)
    VALUES(
        81931054,
        'What is the most efficient way to heat water?',
        'Microfusion reactors?',
        'https://dcdn.org/g/1622859370330.jpg',
        'g'
    );

CALL insert_post('Anonymous', 'seems bad for dust build up', 'https://dcdn.org/g/1622861743004.png', 81931054);
CALL insert_post('Anonymous', 'is that cover at least used as a heatsink?', 'https://dcdn.org/g/1622865285989.png', 81931054);
   
SELECT * FROM BOARD;
SELECT * FROM THREAD;
SELECT * FROM POST;



