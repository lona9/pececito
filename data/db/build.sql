CREATE TABLE IF NOT EXISTS exp (
  UserID integer PRIMARY KEY,
  XP integer DEFAULT 0,
  Level integer DEFAULT 0,
  XPLock text DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS reminders (
  ReminderID NUMERIC PRIMARY KEY,
  ReminderTime DATE,
  ReminderText VARCHAR,
  ReminderAuthor VARCHAR,
  ReminderChannel NUMERIC
);
