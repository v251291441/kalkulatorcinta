DROP TABLE IF EXISTS loves;
CREATE TABLE loves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    namacowok TEXT NOT NULL,
    tanggalcowok DATE NOT NULL,
    namacewek TEXT NOT NULL,
    tanggalcewek DATE NOT NULL,
    nilai FLOAT(1) NOT NULL
);