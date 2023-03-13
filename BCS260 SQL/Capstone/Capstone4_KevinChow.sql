/* q1 retrieve all from movie */
select *
from movie;

/* q2 retrieve all from director */
select *
from director;

/* q3 retrieve all from actor */
select *
from actor;

/* q4 retrieve all from company */
select *
from company;

/* q5 retrieve all from movie quote */
select *
from movie_quote;

/* q6 only title from genre */
select genretitle
from genre;

/* q7 only character name, role, and actor ID from character */
select charactername, characterrole, actorid
from character;

/* q8 retrieve all from remake */
select *
from remake;

/* q9 all from movie where ID > 8 */
select *
from movie
where movieID > 8;

/* q10 all from company order by address */
select *
from company
order by companyaddress;

/* q11 all from movie where genreid is 10 */
select *
from movie
where genreid = 10;

/* q12 joining table character and movie quote, display char name and quote */
select charactername, mq_text
from character as c join movie_quote as q
	on c.characterid = q.characterid;

/* q13 joining movie and genere, order by order id, display the movieid, moviename, and genre title */
select movieid, moviename, genretitle
from movie as m join genre as g
	on m.genreid = g.genreid
order by m.genreid;

/* q14 display movie and its company name, by joing movie, movie_company, company. order by companyid */
select m.movieid, moviename, companyname
from movie as m 
	join movie_company as mc
	on m.movieid = mc.movieid
	join company as c
	on mc.companyid = c.companyid
order by mc.companyid;

/* q15 display movie and its actor(only 1 per movie in my database), joining 3 tables */
select m.movieid, moviename, charactername, actorlast, actorfirst
from movie as m
	join character as c
	on m.movieid = c.movieid
	join actor as a
	on c.actorid = a.actorid;

/* q16 total number of movie directed by director per directorid, group by director
	there will be 2 of each for my database, original and remake with same director */
select md.directorid, [number of movie] = count(md.directorid)
from director as d join movie_director as md
	on d.directorid = md.directorid
group by md.directorid;

/* q17 moviename, with its character and quote, joing 3 tables */
select m.movieid, moviename, charactername, mq_text
from movie as m
	join character as c
	on m.movieid = c.movieid
	join movie_quote as mq
	on c.characterid = mq.characterid;

/* q18 similar to q17 but with actor combined last and first name, joing 4 tables */
select m.movieid, moviename, [actor name] = concat(actorfirst,actorlast), charactername, mq_text
from movie as m
	join character as c
	on m.movieid = c.movieid
	join movie_quote as mq
	on c.characterid = mq.characterid
	join actor as a
	on c.actorid = a.actorid;

/* q19 display movie that is produced by Walt Disney Studios */
select m.movieid, moviename, companyname
from movie as m
	join movie_company as mc
	on m.movieid = mc.movieid
	join company as c
	on mc.companyid = c.companyid
where companyname = 'Walt Disney Studios';

/* q20 display movie that is directed by last name Reiner */
select m.movieid, moviename, directorlast, directorfirst
from movie as m
	join movie_director as md
	on m.movieid = md.movieid
	join director as d
	on md.directorid = d.directorid
where directorlast = 'Reiner';