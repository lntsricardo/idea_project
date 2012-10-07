REATE TABLE USER_TYPE
(
	ID_TYPE INT NOT NULL PRIMARY KEY,
	TYPE VARCHAR(30) NOT NULL
);

CREATE TABLE PERSON
(
	ID_USER BIGINT NOT NULL PRIMARY KEY,
	NAME VARCHAR(50) NOT NULL,
	USERNAME VARCHAR(30) NOT NULL,
	PASSWORD VARCHAR(255) NOT NULL,
	ID_TYPE INT NOT NULL,
	FOREIGN KEY (ID_TYPE) REFERENCES USER_TYPE(ID_TYPE)
);
