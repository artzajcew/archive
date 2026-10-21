CREATE TABLE archive_folder (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    owner_id INTEGER NOT NULL REFERENCES auth_user(id)
);

CREATE TABLE archive_tag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40) NOT NULL,
    owner_id INTEGER NOT NULL REFERENCES auth_user(id)
);

CREATE TABLE archive_archivefile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    file VARCHAR(100) NOT NULL,
    created_at DATETIME NOT NULL,
    owner_id INTEGER NOT NULL REFERENCES auth_user(id),
    folder_id INTEGER REFERENCES archive_folder(id)
);

CREATE TABLE archive_archivefile_tags (
    archivefile_id INTEGER NOT NULL REFERENCES archive_archivefile(id),
    tag_id INTEGER NOT NULL REFERENCES archive_tag(id),
    PRIMARY KEY (archivefile_id, tag_id)
);
