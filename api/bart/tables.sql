DROP TABLE IF EXISTS route;
CREATE TABLE route (
    id INT PRIMARY KEY,
    depart TEXT NOT NULL,
    arrive TEXT NOT NULL,
    abbr TEXT NOT NULL,
    routeID INT NOT NULL,
    hexColor TEXT NOT NULL,
    color TEXT NOT NULL,
    direction TEXT NOT NULL,
    date DATE NOT NULL
);