DROP TABLE Publishers;
DROP TABLE Studios;
DROP TABLE Games;
DROP TABLE GameTypes;
DROP TABLE Comments;

CREATE TABLE Publishers(publisher_id INTEGER,
                        publisher_name CHAR(30),
                        PRIMARY KEY(publisher_id));

CREATE TABLE Studios(studio_id INTEGER,
                     studio_name CHAR(30),
                     PRIMARY KEY(studio_id));

CREATE TABLE GameTypes(gametype_id INTEGER,
                       gametype_abbrv CHAR(10),
                       gametype_name CHAR(30),
                       gametype_description char(100),
                       PRIMARY KEY(gametype_id));

CREATE TABLE Games(game_id INTEGER,
                   game_name CHAR(30),
                   release_date DATE,
                   gametype_id INTEGER,
                   publisher_id INTEGER,
                   studio_id INTEGER,
                   start_time DATE,
                   end_time DATE,
                   platform CHAR(5),
                   play_status INTEGER,
                   total_time_played INTEGER,
                   PRIMARY KEY(game_id),
                   FOREIGN KEY(gametype_id) REFERENCES GameTypes(gametype_id),
                   FOREIGN KEY(publisher_id) REFERENCES Publishers(publisher_id),
                   FOREIGN KEY(studio_id) REFERENCES Studios(studio_id));

CREATE TABLE Comments(comment_id INTEGER,
                      comment_date DATE,
                      comment_type DATE,
                      score INTEGER,
                      game_id INTEGER,
                      good_or_bad BOOLEAN,
                      comment CHAR(250),
                      comment_level CHAR(20),
                      game_record_id INTEGER,
                      PRIMARY KEY(comment_id),
                      FOREIGN KEY(game_id) REFERENCES Games(game_id)
                      FOREIGN KEY(game_record_id) REFERENCES GameRecords(game_record_id));

CREATE TABLE GameRecords(game_record_id INTEGER,
                         start_time DATE,
                         end_time DATE,
                         record_type CHAR(20),
                         duration TIME,
                         game_id INTEGER,
                         PRIMARY KEY(game_record_id),
                         FOREIGN KEY(game_id) REFERENCES Games(game_id));