-- PRAGMA foreign_keys=OFF;
BEGIN;
CREATE TABLE USER ( USERNAME   TEXT  PRIMARY KEY,
                    HASDEDPW   TEXT  NOT NULL);

CREATE TABLE LAYOUT( LAYOUTNAME TEXT   PRIMARY KEY);

CREATE TABLE BLOG ( BLOGNAME   TEXT    PRIMARY KEY,
                    OWNER      TEXT    NOT NULL,
                    MKDSETTING TEXT    NOT NULL,
                    LAYOUTNAME TEXT    NOT NULL,
                    FOREIGN KEY(OWNER) REFERENCES USER(USERNAME),
                    FOREIGN KEY(LAYOUTNAME) REFERENCES LAYOUT(LAYOUTNAME));

CREATE TABLE POST ( POSTID     INTEGER   PRIMARY KEY   AUTOINCREMENT,
                    TITLE      TEXT      NOT NULL,
                    CONTENT    TEXT      NOT NULL,
                    POSTDATE   DATE      NOT NULL,
                    OWNER      TEXT      NOT NULL,
                    FOREIGN KEY(OWNER) REFERENCES USER(USERNAME));

CREATE TABLE MESSAGE( MSGID     INTEGER   PRIMARY KEY   AUTOINCREMENT,
                      MSGDATE   DATE      NOT NULL,
                      POSTER    TEXT      NOT NULL,
                      CONTENT   TEXT      NOT NULL,
                      POSTID    INTEGER   NOT NULL,
                      FOREIGN KEY(POSTID) REFERENCES POST(POSTID)
                        ON DELETE CASCADE,
                      FOREIGN KEY(POSTER) REFERENCES USER(USERNAME));
COMMIT;
