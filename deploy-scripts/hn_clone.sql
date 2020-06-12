CREATE DATABASE HN_ONE;

CREATE TABLE HN_ONE.hn_posts_score
(
  id INT unsigned NOT NULL, # Unique ID for the record
  author VARCHAR(150) NOT NULL, # Author of the article
  title VARCHAR (150) NOT NULL, # Title of the article
  score INT NOT NULL, # Number of votes on the post
  url VARCHAR (300) NOT NULL, # URL to article
  descendants INT unsigned NOT NULL,
  PRIMARY KEY (id) # Make the id the primary key
);

CREATE TABLE HN_ONE.hn_posts_no_score
(
  id INT unsigned NOT NULL, # Unique ID for the record
  author VARCHAR(150) NOT NULL, # Author of the article
  title VARCHAR (150) NOT NULL, # Title of the article
  url VARCHAR (300) NOT NULL, # URL to article
  descendants INT unsigned NOT NULL,
  PRIMARY KEY (id) # Make the id the primary key
);