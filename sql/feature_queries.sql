SELECT
    playerid,
    yearid,
    teamid,
    ab,
    h,
    hr,
    bb,
    so,
    avg,
    obp,
    slg,
    babip,
    iso,
    bb_pct,
    k_pct,
    xbh_pct,

    ROUND((CASE WHEN so > 0 THEN bb::float / so ELSE NULL END)::NUMERIC, 3) AS bb_k_ratio,
	ROUND((1 - (so::float / ab))::NUMERIC, 3) AS contact_rate,
	ROUND((hr::float / ab)::NUMERIC, 3) AS hr_rate,
	ROUND(((hr::float + "2b" + "3b") / ab)::NUMERIC, 3) AS xbh_rate,
	ROUND((rbi::float / ab)::NUMERIC, 3) AS rbi_rate,
	ROUND((((h + bb) * (h + "2b" + 2*"3b" + 3*hr)::float) / NULLIF((ab + bb),0))::NUMERIC, 3) AS runs_created,
	ROUND((sb::float / ab)::NUMERIC, 3) AS sb_rate,
	ROUND(("1b"::float / NULLIF(h,0))::NUMERIC, 3) AS singles_pct

		
FROM batting
WHERE ab >= 50