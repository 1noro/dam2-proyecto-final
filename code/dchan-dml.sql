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
    
SELECT * FROM BOARD;
SELECT * FROM THREAD;