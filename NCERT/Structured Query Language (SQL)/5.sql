SELECT MatchID FROM MATCH_DETAILS WHERE FirstTeamScore > 70 AND SecondTeamScore > 70;

SELECT MatchID FROM MATCH_DETAILS WHERE FirstTeamScore < 70 AND SecondTeamScore > 70;

SELECT MatchID, MatchDate FROM MATCH_DETAILS WHERE (FirstTeamID = 1 AND FirstTeamScore > SecondTeamScore) OR (SecondTeamID = 1 AND SecondTeamScore > FirstTeamScore);

SELECT MatchID FROM MATCH_DETAILS WHERE (FirstTeamID = 2 AND FirstTeamScore < SecondTeamScore) OR (SecondTeamID = 2 AND SecondTeamScore < FirstTeamScore);

ALTER TABLE TEAM RENAME TO T_DATA;
ALTER TABLE T_DATA RENAME COLUMN TeamID TO T_ID;
ALTER TABLE T_DATA RENAME COLUMN TeamName TO T_NAME;