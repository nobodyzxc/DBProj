-- PRAGMA foreign_keys=OFF;
BEGIN;
INSERT INTO USER VALUES('admin', -- name:admin, passwd:admin
    '4cfd26e6f2a29d55b76c74c5dc04e1bd7f69ec81f7270c41356fef26100fd500:58c9b2b5046c46b4acc79f2e2ebc4d60');
INSERT INTO USER VALUES('bdmin', -- name:bdmin, passwd:admin
    '4cfd26e6f2a29d55b76c74c5dc04e1bd7f69ec81f7270c41356fef26100fd500:58c9b2b5046c46b4acc79f2e2ebc4d60');
INSERT INTO USER VALUES('cdmin', -- name:cdmin, passwd:admin
    '4cfd26e6f2a29d55b76c74c5dc04e1bd7f69ec81f7270c41356fef26100fd500:58c9b2b5046c46b4acc79f2e2ebc4d60');
INSERT INTO USER VALUES('ddmin', -- name:ddmin, passwd:admin
    '4cfd26e6f2a29d55b76c74c5dc04e1bd7f69ec81f7270c41356fef26100fd500:58c9b2b5046c46b4acc79f2e2ebc4d60');

INSERT INTO LAYOUT VALUES("mist");
INSERT INTO LAYOUT VALUES("muse");
INSERT INTO LAYOUT VALUES("pisces");
INSERT INTO LAYOUT VALUES("gemini");

INSERT INTO BLOG VALUES('Where is the admin?', 'admin', '0000000', "gemini");
INSERT INTO BLOG VALUES('bdmin is here!', 'bdmin', '0000000', "pisces");
INSERT INTO BLOG VALUES('cdmin is foo~', 'cdmin', '0000000', "muse");
INSERT INTO BLOG VALUES('dd the root directory!', 'ddmin', '0000000', "mist");

COMMIT;
