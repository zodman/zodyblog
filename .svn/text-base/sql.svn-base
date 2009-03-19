BEGIN;
DROP TABLE `zodynetwork_pownceevent`;
DROP TABLE `zodynetwork_powncefile`;
DROP TABLE `zodynetwork_powncelink`;
DROP TABLE `zodynetwork_powncenote`;
CREATE TABLE `zodynetwork_powncenote` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `pownce_id` integer UNSIGNED NOT NULL,
    `body` longtext NOT NULL,
    `permalink` varchar(200) NOT NULL,
    `date` datetime NOT NULL
)
;
CREATE TABLE `zodynetwork_powncelink` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `url` varchar(200) NOT NULL,
    `pownce_note_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `zodynetwork_powncelink` ADD CONSTRAINT pownce_note_id_refs_id_35961411 FOREIGN KEY (`pownce_note_id`) REFERENCES `zodynetwork_powncenote` (`id`);
CREATE TABLE `zodynetwork_powncefile` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(200) NOT NULL,
    `type` varchar(100) NOT NULL,
    `pownce_note_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `zodynetwork_powncefile` ADD CONSTRAINT pownce_note_id_refs_id_56691831 FOREIGN KEY (`pownce_note_id`) REFERENCES `zodynetwork_powncenote` (`id`);
CREATE TABLE `zodynetwork_pownceevent` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(200) NOT NULL,
    `ical` varchar(200) NOT NULL,
    `location` varchar(200) NOT NULL,
    `date` datetime NOT NULL,
    `pownce_note_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `zodynetwork_pownceevent` ADD CONSTRAINT pownce_note_id_refs_id_685e8efa FOREIGN KEY (`pownce_note_id`) REFERENCES `zodynetwork_powncenote` (`id`);
COMMIT;
BEGIN;
DROP TABLE `tumble_item`;
CREATE TABLE `tumble_item` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `content_type_id` integer NOT NULL,
    `object_id` integer UNSIGNED NOT NULL,
    `pub_date` datetime NOT NULL
)
;
ALTER TABLE `tumble_item` ADD CONSTRAINT content_type_id_refs_id_6f693a3a FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
CREATE INDEX `tumble_item_content_type_id` ON `tumble_item` (`content_type_id`);
COMMIT;
