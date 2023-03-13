/******** Insert rows into DIRECTOR table ******************/

INSERT INTO Director /*None of the top 10 Director's middle name listed on excel given*/
	(DirectorID, DirectorFirst, DirectorLast) /*therefore skipping middle name colum*/
VALUES
	(1, 'Don', 'Siegel'),
	(2, 'Rob', 'Reiner'),
	(3, 'Victor', 'Fleming'),
	(4, 'Elia', 'Kazan'),
	(5, 'Stanley', 'Kubrick'),
	(6, 'Diane', 'Johnson'),
	(7, 'Steven', 'Spielberg'),
	(8, 'Andrew', 'Stanton'),
	(9, 'Frank', 'Capra'),
	(10, 'Francis', 'Coppola');



	/******** Insert rows into COMPANY table ******************/

INSERT INTO Company /*For efficiency purpose, address will only be its city & state*/
VALUES
	(1, 'Warner Bros', 'Los Angeles, CA'),
	(2, 'Sony Pictures Motion Picture Group', 'Culver City, CA'),
	(3, 'Walt Disney Studios', 'Los Angeles, CA'),
	(4, 'Universal Pictures', 'New York, NY'),
	(5, '20th Century Fox', 'Los Angeles, CA'),
	(6, 'Paramount Pictures', 'Los Angeles, CA'),
	(7, 'Lionsgate Films', 'Santa Monica, CA'),
	(8, 'The Weinstein Company', 'New York, NY'),
	(9, 'Metro-Goldwyn-Mayer Studios', 'Beverly Hills, CA'),
	(10, 'DreamWorks Pictures', 'Universal City, CA');



	/******** Insert rows into GENRE table ******************/

INSERT INTO Genre
VALUES
	(1, 'Action'),
	(2, 'Animation'),
	(3, 'Comedy'),
	(4, 'Crime'),
	(5, 'Drama'),
	(6, 'Experiment'),
	(7, 'Fantasy'),
	(8, 'Historical'),
	(9, 'Horror'),
	(10, 'Romance');



	/******** Insert rows into ACTOR table ******************/

INSERT INTO Actor /*Again none of the top 10 Actor has a middle name*/
	(ActorID, ActorFirst, ActorLast)
VALUES
	(1, 'Clint', 'Eastwood'),
	(2, 'Carey', 'Elwes'),
	(3, 'Dick', 'Shawn'),
	(4, 'Judy', 'Garland'),
	(5, 'Marlon', 'Brando'),
	(6, 'Jack', 'Nicholson'),
	(7, 'Roy', 'Scheider'),
	(8, 'Kathleen', 'Turner'),
	(9, 'Ellen', 'Degeneres'),
	(10, 'Frank', 'Travers');



	/******** Insert rows into MOVIE table ******************/

INSERT INTO Movie /*Since none genre was given in excel, I will be guessing based on title*/
VALUES
	(1, 'Dirty Harry', 1971, 5),
	(2, 'The Princess Bride', 1987, 10),
	(3, 'Wizard of Oz', 1939, 7),
	(4, 'On the Waterfront', 1954, 10),
	(5, 'The Shining', 1980, 9),
	(6, 'Jaws', 1975, 9),
	(7, 'Who Framed Roger Rabbit?', 1988, 3),
	(8, 'Finding Nemo', 2003, 2),
	(9, 'Its a Wonderful Life', 1946, 10),
	(10, 'The Godfather, Part II (Remake)', 1974, 8), /*Creating 10 similar movie for remake table purpose*/
	(11, 'Dirty Harry (Remake)', 1971, 5),
	(12, 'The Princess Bride (Remake)', 1987, 10),
	(13, 'Wizard of Oz (Remake)', 1939, 7),
	(14, 'On the Waterfront (Remake)', 1954, 10),
	(15, 'The Shining (Remake)', 1980, 9),
	(16, 'Jaws (Remake)', 1975, 9),
	(17, 'Who Framed Roger Rabbit? (Remake)', 1988, 3),
	(18, 'Finding Nemo (Remake)', 2003, 2),
	(19, 'Its a Wonderful Life (Remake)', 1946, 10),
	(20, 'The Godfather, Part II (Remake)', 1974, 8);



	/******** Insert rows into MOVIE_COMPANY table ******************/

INSERT INTO Movie_Company /*Company was not given on excel, I will be making up data*/
VALUES
	(1, 2),
	(2, 4),
	(3, 6),
	(4, 7),
	(5, 3),
	(6, 9),
	(7, 10),
	(8, 1),
	(9, 5),
	(10, 8),
	(11, 2), /*Creating 10 similar match for remake table purpose*/
	(12, 4),
	(13, 6),
	(14, 7),
	(15, 3),
	(16, 9),
	(17, 10),
	(18, 1),
	(19, 5),
	(20, 8);



	/******** Insert rows into MOVIE_DIRECTOR table ******************/

INSERT INTO Movie_Director
VALUES /*Since I inserted data in order, their ID actually match perfectly*/
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
	(9, 9),
	(10, 10),
	(11, 1), /*Creating 10 similar match for remake table purpose, I understand it can just be NULL*/
	(12, 2),
	(13, 3),
	(14, 4),
	(15, 5),
	(16, 6),
	(17, 7),
	(18, 8),
	(19, 9),
	(20, 10);



	/******** Insert rows into REMAKE table ******************/

INSERT INTO Remake /*Since there are no remake data, I will make up 10 rows for capstone purpose*/
VALUES
	(1, 11),
	(2, 12),
	(3, 13),
	(4, 14),
	(5, 15),
	(6, 16),
	(7, 17),
	(8, 18),
	(9, 19),
	(10, 20);



	/******** Insert rows into CHARACTER table ******************/

INSERT INTO Character /*The role of the character will be made up*/
VALUES
	(1, 1, 'Harry', 'MainCast', 1),
	(2, 2, 'Wesley', 'MainCast', 2),
	(3, 3, 'Dorothy', 'Support', 3),
	(4, 4, 'Stanley', 'MainCast', 4),
	(5, 5, 'Jack', 'MainCast', 5),
	(6, 6, 'Brody', 'Support', 6),
	(7, 7, 'Jessica', 'MainCast', 7),
	(8, 8, 'Dory', 'MainCast', 8),
	(9, 9, 'Clarence', 'MainCast', 9),
	(10, 10, 'Don', 'MainCast', 10), /*Remake will be cast by the exact same actor with same name*/
	(11, 11, 'Harry', 'MainCast', 1),
	(12, 12, 'Wesley', 'MainCast', 2),
	(13, 13, 'Dorothy', 'Support', 3),
	(14, 14, 'Stanley', 'MainCast', 4),
	(15, 15, 'Jack', 'MainCast', 5),
	(16, 16, 'Brody', 'Support', 6),
	(17, 17, 'Jessica', 'MainCast', 7),
	(18, 18, 'Dory', 'MainCast', 8),
	(19, 19, 'Clarence', 'MainCast', 9),
	(20, 20, 'Don', 'MainCast', 10);



	/******** Insert rows into MOVIE_QUOTE table ******************/

INSERT INTO Movie_Quote /*Ignoring Remake Movie since they will have same quote*/
Values
	(1, 1, 1, 'Youve got to ask yourself one question: Do I feel lucky? Well, do ya punk?'),
	(2, 2, 2, 'As you wish'),
	(3, 3, 3, 'Ive got a feeling were not in Kansas anymore, Toto!'),
	(4, 4, 4, 'I coulda been a contender. I couldve been somebody, instead of a bum, which is what I am.'),
	(5, 5, 5, 'Heres Johnny!'),
	(6, 6, 6, 'Youre going to need a bigger boat.'),
	(7, 7, 7, 'Im not bad. Im just drawn that way.'),
	(8, 8, 8, 'Just keep swimming'),
	(9, 9, 9, 'Every time a bell rings, an angel gets his wings.'),
	(10, 2, 2, 'Inconceivable!'), /*Just to demonstrate 1:N relationship*/
	(11, 10, 10, 'Keep your friends close, but your enemies closer.');