-- DROP TABLE "alembic_version";

-- DROP TABLE "tokens";

-- DROP TABLE "users";

-- UPDATE users SET is_superuser = True
-- WHERE users.id = 4;

DELETE FROM funding_opp_requirements
WHERE fund_id = 267;
