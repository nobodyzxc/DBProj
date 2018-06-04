-- PRAGMA foreign_keys=OFF;
BEGIN;
INSERT INTO USER VALUES('admin', -- name:admin, passwd:admin
    '4cfd26e6f2a29d55b76c74c5dc04e1bd7f69ec81f7270c41356fef26100fd500:58c9b2b5046c46b4acc79f2e2ebc4d60');
INSERT INTO BLOG VALUES('admin', 'admin');
INSERT INTO LAYOUT VALUES(0, 'admin', '00000000');
COMMIT;
