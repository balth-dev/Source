CREATE TABLE equipement(
   id_equipement BIGINT AUTO_INCREMENT,
   name VARCHAR(50) NOT NULL,
   quantity INT NOT NULL,
   PRIMARY KEY(id_equipement)
);

CREATE TABLE role(
   id_role BIGINT AUTO_INCREMENT,
   name VARCHAR(20) NOT NULL,
   PRIMARY KEY(id_role),
   UNIQUE(name)
);

CREATE TABLE location(
   id_address BIGINT AUTO_INCREMENT,
   town VARCHAR(40) NOT NULL,
   street VARCHAR(40) NOT NULL,
   zip_code CHAR(5) NOT NULL,
   PRIMARY KEY(id_address)
);

CREATE TABLE building(
   id_building BIGINT AUTO_INCREMENT,
   name VARCHAR(20) NOT NULL,
   id_address BIGINT NOT NULL,
   PRIMARY KEY(id_building),
   UNIQUE(name),
   FOREIGN KEY(id_address) REFERENCES location(id_address)
);

CREATE TABLE  user(
   id_user BIGINT AUTO_INCREMENT,
   name VARCHAR(50) NOT NULL,
   first_name VARCHAR(50) NOT NULL,
   email VARCHAR(100) NOT NULL,
   password VARCHAR(200) NOT NULL,
   gender ENUM('homme', 'femme', 'non renseigne'),
   id_role BIGINT NOT NULL,
   PRIMARY KEY(id_user),
   UNIQUE(email),
   FOREIGN KEY(id_role) REFERENCES role(id_role)
);

CREATE TABLE Classroom(
   id_classroom BIGINT AUTO_INCREMENT,
   name VARCHAR(50) NOT NULL,
   capacity INT NOT NULL,
   category ENUM ("informatique", "traditionnelle") NOT NULL,
   Stage VARCHAR(50) NOT NULL,
   code_access CHAR(4),
   id_classroom_1 BIGINT,
   id_building BIGINT NOT NULL,
   PRIMARY KEY(id_classroom),
   UNIQUE(code_access),
   FOREIGN KEY(id_classroom_1) REFERENCES Classroom(id_classroom),
   FOREIGN KEY(id_building) REFERENCES building(id_building)
);

CREATE TABLE reservation(
   id_reservation BIGINT AUTO_INCREMENT,
   date_reservation DATE NOT NULL,
   start_time TIME NOT NULL,
   end_time TIME NOT NULL,
   status ,
   id_classroom BIGINT NOT NULL,
   id_user BIGINT NOT NULL,
   PRIMARY KEY(id_reservation),
   FOREIGN KEY(id_classroom) REFERENCES Classroom(id_classroom),
   FOREIGN KEY(id_user) REFERENCES  user(id_user)
);

CREATE TABLE event(
   id_event BIGINT AUTO_INCREMENT,
   description VARCHAR(500),
   status ENUM ("En cours", "Résolue", "Signalé")  Default(Signalé),
   moment DATE,
   id_classroom BIGINT NOT NULL,
   PRIMARY KEY(id_event),
   UNIQUE(description),
   UNIQUE(status),
   FOREIGN KEY(id_classroom) REFERENCES Classroom(id_classroom)
);

CREATE TABLE equipped_with(
   id_classroom BIGINT,
   id_equipement BIGINT,
   PRIMARY KEY(id_classroom, id_equipement),
   FOREIGN KEY(id_classroom) REFERENCES Classroom(id_classroom),
   FOREIGN KEY(id_equipement) REFERENCES equipement(id_equipement)
);
