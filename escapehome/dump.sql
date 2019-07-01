PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2019-06-17 15:11:44.874753');
INSERT INTO django_migrations VALUES(2,'auth','0001_initial','2019-06-17 15:11:44.887797');
INSERT INTO django_migrations VALUES(3,'admin','0001_initial','2019-06-17 15:11:44.896863');
INSERT INTO django_migrations VALUES(4,'admin','0002_logentry_remove_auto_add','2019-06-17 15:11:44.906162');
INSERT INTO django_migrations VALUES(5,'admin','0003_logentry_add_action_flag_choices','2019-06-17 15:11:44.925800');
INSERT INTO django_migrations VALUES(6,'contenttypes','0002_remove_content_type_name','2019-06-17 15:11:44.943756');
INSERT INTO django_migrations VALUES(7,'auth','0002_alter_permission_name_max_length','2019-06-17 15:11:44.949907');
INSERT INTO django_migrations VALUES(8,'auth','0003_alter_user_email_max_length','2019-06-17 15:11:44.959775');
INSERT INTO django_migrations VALUES(9,'auth','0004_alter_user_username_opts','2019-06-17 15:11:44.969044');
INSERT INTO django_migrations VALUES(10,'auth','0005_alter_user_last_login_null','2019-06-17 15:11:44.979555');
INSERT INTO django_migrations VALUES(11,'auth','0006_require_contenttypes_0002','2019-06-17 15:11:44.981824');
INSERT INTO django_migrations VALUES(12,'auth','0007_alter_validators_add_error_messages','2019-06-17 15:11:44.991701');
INSERT INTO django_migrations VALUES(13,'auth','0008_alter_user_username_max_length','2019-06-17 15:11:45.004897');
INSERT INTO django_migrations VALUES(14,'auth','0009_alter_user_last_name_max_length','2019-06-17 15:11:45.015148');
INSERT INTO django_migrations VALUES(15,'core','0001_initial','2019-06-17 15:11:45.036210');
INSERT INTO django_migrations VALUES(16,'sessions','0001_initial','2019-06-17 15:11:45.040061');
INSERT INTO django_migrations VALUES(17,'core','0002_auto_20190617_1556','2019-06-17 15:56:21.896383');
INSERT INTO django_migrations VALUES(18,'core','0003_activescenario','2019-06-23 21:04:41.772218');
INSERT INTO django_migrations VALUES(19,'core','0004_auto_20190623_2121','2019-06-23 21:21:39.006747');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_flag" smallint unsigned NOT NULL);
INSERT INTO django_admin_log VALUES(1,'2019-06-17 15:12:20.698800','1','Lamp 1 - decke in wohnzimmer','[{"added": {}}]',11,1,1);
INSERT INTO django_admin_log VALUES(2,'2019-06-17 15:12:32.877243','2','Lamp 2 - sofa in wohnzimmer','[{"added": {}}]',11,1,1);
INSERT INTO django_admin_log VALUES(3,'2019-06-17 15:13:25.530657','1','Command 1 - blicken','[{"added": {}}]',7,1,1);
INSERT INTO django_admin_log VALUES(4,'2019-06-17 15:24:54.650059','2','Command 2 - farbe setzen','[{"added": {}}]',7,1,1);
INSERT INTO django_admin_log VALUES(5,'2019-06-17 15:25:58.159223','3','Command 3 - einschalten','[{"added": {}}]',7,1,1);
INSERT INTO django_admin_log VALUES(6,'2019-06-17 15:31:56.226202','1','Riddle 1','[{"added": {}}]',9,1,1);
INSERT INTO django_admin_log VALUES(7,'2019-06-17 15:32:50.870164','2','Riddle 2','[{"added": {}}]',9,1,1);
INSERT INTO django_admin_log VALUES(8,'2019-06-17 15:34:23.716187','1','Scenario 1 - Party Höhle','[{"added": {}}]',10,1,1);
INSERT INTO django_admin_log VALUES(9,'2019-06-17 15:34:30.236838','1','Scenario 1 - Party Höhle','[{"changed": {"fields": ["severity"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(10,'2019-06-17 15:34:53.064081','1','Scenario 1 - Party Höhle','[]',10,1,2);
INSERT INTO django_admin_log VALUES(11,'2019-06-17 15:37:52.100549','3','Riddle 3','[{"added": {}}]',9,1,1);
INSERT INTO django_admin_log VALUES(12,'2019-06-17 15:38:01.691873','1','Scenario 1 - Party Höhle','[{"changed": {"fields": ["riddles"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(13,'2019-06-17 15:43:02.439012','4','Riddle 4','[{"added": {}}]',9,1,1);
INSERT INTO django_admin_log VALUES(14,'2019-06-17 15:44:11.137990','2','Scenario 2 - Quiz Fragen','[{"added": {}}]',10,1,1);
INSERT INTO django_admin_log VALUES(15,'2019-06-17 15:51:19.850942','2','Scenario 2 - Quiz Fragen','[{"changed": {"fields": ["severity", "length"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(16,'2019-06-17 15:51:28.608429','1','Scenario 1 - Party Höhle','[{"changed": {"fields": ["severity", "length"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(17,'2019-06-17 15:56:34.592567','3','Scenario 3 - test','[{"added": {}}]',10,1,1);
INSERT INTO django_admin_log VALUES(18,'2019-06-17 15:56:39.450319','3','Scenario 3 - test','',10,1,3);
INSERT INTO django_admin_log VALUES(19,'2019-06-17 15:56:42.755745','1','Scenario 1 - Party Höhle','[{"changed": {"fields": ["length"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(20,'2019-06-17 15:56:47.131661','2','Scenario 2 - Quiz Fragen','[{"changed": {"fields": ["length"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(21,'2019-06-22 14:35:04.133324','2','Scenario 2 - Quizfragen','[{"changed": {"fields": ["name"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(22,'2019-06-22 14:41:18.815287','1','Scenario 1 - Lichterchaos','[{"changed": {"fields": ["name"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(23,'2019-06-22 14:43:41.561480','1','Scenario 1 - lustige Lichter','[{"changed": {"fields": ["name"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(24,'2019-06-23 10:36:35.746060','4','Riddle 4 - Warum gehen Ameisen nicht in die Kirche?','[{"changed": {"fields": ["solution"]}}]',9,1,2);
INSERT INTO django_admin_log VALUES(25,'2019-06-23 10:37:09.851084','5','Riddle 5 - Was ist 7 * 7?','[{"added": {}}]',9,1,1);
INSERT INTO django_admin_log VALUES(26,'2019-06-23 10:37:25.127717','2','Scenario 2 - Quizfragen','[{"changed": {"fields": ["riddles"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(27,'2019-06-23 10:57:56.628200','2','Scenario 2 - quiz fragen','[{"changed": {"fields": ["name"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(28,'2019-06-23 20:29:39.075128','1','Scenario 1 - Lustige Lichter','[{"changed": {"fields": ["name"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(29,'2019-06-23 20:29:45.440928','2','Scenario 2 - Quiz Fragen','[{"changed": {"fields": ["name"]}}]',10,1,2);
INSERT INTO django_admin_log VALUES(30,'2019-06-23 21:21:46.028975','1','ActiveScenario object (1)','[{"added": {}}]',12,1,1);
INSERT INTO django_admin_log VALUES(31,'2019-06-23 21:25:52.266104','1','ActiveScenario object (1)','',12,1,3);
INSERT INTO django_admin_log VALUES(32,'2019-06-23 22:17:03.981257','3','ActiveScenario object (3)','',12,1,3);
INSERT INTO django_admin_log VALUES(33,'2019-06-23 22:17:03.983296','2','ActiveScenario object (2)','',12,1,3);
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'auth','user');
INSERT INTO django_content_type VALUES(5,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(6,'sessions','session');
INSERT INTO django_content_type VALUES(7,'core','command');
INSERT INTO django_content_type VALUES(8,'core','device');
INSERT INTO django_content_type VALUES(9,'core','riddle');
INSERT INTO django_content_type VALUES(10,'core','scenario');
INSERT INTO django_content_type VALUES(11,'core','lamp');
INSERT INTO django_content_type VALUES(12,'core','activescenario');
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_user','Can add user');
INSERT INTO auth_permission VALUES(14,4,'change_user','Can change user');
INSERT INTO auth_permission VALUES(15,4,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(16,4,'view_user','Can view user');
INSERT INTO auth_permission VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(21,6,'add_session','Can add session');
INSERT INTO auth_permission VALUES(22,6,'change_session','Can change session');
INSERT INTO auth_permission VALUES(23,6,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(24,6,'view_session','Can view session');
INSERT INTO auth_permission VALUES(25,7,'add_command','Can add command');
INSERT INTO auth_permission VALUES(26,7,'change_command','Can change command');
INSERT INTO auth_permission VALUES(27,7,'delete_command','Can delete command');
INSERT INTO auth_permission VALUES(28,7,'view_command','Can view command');
INSERT INTO auth_permission VALUES(29,8,'add_device','Can add device');
INSERT INTO auth_permission VALUES(30,8,'change_device','Can change device');
INSERT INTO auth_permission VALUES(31,8,'delete_device','Can delete device');
INSERT INTO auth_permission VALUES(32,8,'view_device','Can view device');
INSERT INTO auth_permission VALUES(33,9,'add_riddle','Can add riddle');
INSERT INTO auth_permission VALUES(34,9,'change_riddle','Can change riddle');
INSERT INTO auth_permission VALUES(35,9,'delete_riddle','Can delete riddle');
INSERT INTO auth_permission VALUES(36,9,'view_riddle','Can view riddle');
INSERT INTO auth_permission VALUES(37,10,'add_scenario','Can add scenario');
INSERT INTO auth_permission VALUES(38,10,'change_scenario','Can change scenario');
INSERT INTO auth_permission VALUES(39,10,'delete_scenario','Can delete scenario');
INSERT INTO auth_permission VALUES(40,10,'view_scenario','Can view scenario');
INSERT INTO auth_permission VALUES(41,11,'add_lamp','Can add lamp');
INSERT INTO auth_permission VALUES(42,11,'change_lamp','Can change lamp');
INSERT INTO auth_permission VALUES(43,11,'delete_lamp','Can delete lamp');
INSERT INTO auth_permission VALUES(44,11,'view_lamp','Can view lamp');
INSERT INTO auth_permission VALUES(45,12,'add_activescenario','Can add active scenario');
INSERT INTO auth_permission VALUES(46,12,'change_activescenario','Can change active scenario');
INSERT INTO auth_permission VALUES(47,12,'delete_activescenario','Can delete active scenario');
INSERT INTO auth_permission VALUES(48,12,'view_activescenario','Can view active scenario');
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "last_name" varchar(150) NOT NULL);
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$120000$T4atjpOabmoK$eDP8KYiLICtvPIiJ6x5LMu096GeEYZ8xFxCgvNH6OOY=','2019-06-17 15:12:06.624216',1,'jgiebelhausen','','',1,1,'2019-06-17 15:11:55.974876','');
CREATE TABLE IF NOT EXISTS "core_command" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL UNIQUE, "function" varchar(255) NOT NULL, "config" text NOT NULL);
INSERT INTO core_command VALUES(1,'blicken','blink','[]');
INSERT INTO core_command VALUES(2,'farbe setzen','set_color','[]');
INSERT INTO core_command VALUES(3,'einschalten','turn_on','{}');
CREATE TABLE IF NOT EXISTS "core_device" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT);
INSERT INTO core_device VALUES(1);
INSERT INTO core_device VALUES(2);
CREATE TABLE IF NOT EXISTS "core_riddle" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "task" text NOT NULL, "solution" text NOT NULL, "code" varchar(255) NOT NULL, "hints" text NOT NULL, "correct" text NOT NULL, "incorrect" text NOT NULL);
INSERT INTO core_riddle VALUES(1,'Wer hat an der Uhr gedreht?','paulchen panther','42',replace(replace('Soll das heißen, ja ihr Leut‘,\r\nmit dem Paul ist Schluss für heut‘\r\nPaulchen, Paulchen, mach‘ doch weiter\r\nJag'' das Männchen auf die Leiter.','\r',char(13)),'\n',char(10)),'ich komm‘ wieder keine Frage, Heute ist nicht alle Tage.','dedöööm');
INSERT INTO core_riddle VALUES(2,'Welche Farbe hat die Lampe?','rot, die Farbe ist rot, die Lampe leuchtet rot, sie leuchtet rot','3','','','');
INSERT INTO core_riddle VALUES(3,'Wie oft blickt die Lampe?','die Lampe blickt 3 mal Rot, drei mal, 3, drei','3','achte nur auf die Farbe von dem vorher gelösten Rätsel.','','');
INSERT INTO core_riddle VALUES(4,'Warum gehen Ameisen nicht in die Kirche?','Weil sie Insekten sind!','0','','Haa Haa ha ha','');
INSERT INTO core_riddle VALUES(5,'Was ist 7 * 7?','Feiner Sand','49','','Ha ha ha!','');
CREATE TABLE IF NOT EXISTS "core_riddle_commands" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "riddle_id" integer NOT NULL REFERENCES "core_riddle" ("id") DEFERRABLE INITIALLY DEFERRED, "command_id" integer NOT NULL REFERENCES "core_command" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO core_riddle_commands VALUES(1,2,2);
INSERT INTO core_riddle_commands VALUES(2,3,1);
CREATE TABLE IF NOT EXISTS "core_scenario_riddles" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "scenario_id" integer NOT NULL REFERENCES "core_scenario" ("id") DEFERRABLE INITIALLY DEFERRED, "riddle_id" integer NOT NULL REFERENCES "core_riddle" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO core_scenario_riddles VALUES(1,1,2);
INSERT INTO core_scenario_riddles VALUES(2,1,3);
INSERT INTO core_scenario_riddles VALUES(3,2,1);
INSERT INTO core_scenario_riddles VALUES(4,2,4);
INSERT INTO core_scenario_riddles VALUES(6,2,5);
CREATE TABLE IF NOT EXISTS "core_lamp" ("device_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES "core_device" ("id") DEFERRABLE INITIALLY DEFERRED, "lamp_id" integer NOT NULL, "name" varchar(255) NOT NULL, "on" bool NOT NULL, "color" varchar(7) NOT NULL, "room" varchar(255) NOT NULL, "brightness" integer NOT NULL);
INSERT INTO core_lamp VALUES(1,1,'decke',0,'#ffffff','wohnzimmer',254);
INSERT INTO core_lamp VALUES(2,3,'sofa',0,'#ffffff','wohnzimmer',254);
CREATE TABLE IF NOT EXISTS "core_command_devices" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "command_id" integer NOT NULL REFERENCES "core_command" ("id") DEFERRABLE INITIALLY DEFERRED, "device_id" integer NOT NULL REFERENCES "core_device" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO core_command_devices VALUES(1,1,1);
INSERT INTO core_command_devices VALUES(2,1,2);
INSERT INTO core_command_devices VALUES(3,2,1);
INSERT INTO core_command_devices VALUES(4,2,2);
INSERT INTO core_command_devices VALUES(5,3,1);
INSERT INTO core_command_devices VALUES(6,3,2);
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO django_session VALUES('vnt3bvhfhs636rblupfvlzsyv0fniz5u','Nzg3Y2ZlMWZlNzUzMmE4ZmYzNDFmYzVjNjFkYjQxYTgzYWQ2ZjE2ODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ZDliYTNlYzcxZDI1YzI3YTk4MDM3ODRjMTVmNzQyNGQzN2E5NDQ1In0=','2019-07-01 15:12:06.626231');
CREATE TABLE IF NOT EXISTS "core_scenario" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "description" text NOT NULL, "severity" varchar(255) NOT NULL, "length" bigint NULL);
INSERT INTO core_scenario VALUES(1,'Lustige Lichter','Höhle im Partymodus','MEDIUM',NULL);
INSERT INTO core_scenario VALUES(2,'Quiz Fragen','beantworte komische Fragen!','EASY',NULL);
CREATE TABLE IF NOT EXISTS "core_activescenario" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "players" integer NULL, "score" integer NOT NULL, "state" integer NOT NULL, "scenario_id" integer NOT NULL REFERENCES "core_scenario" ("id") DEFERRABLE INITIALLY DEFERRED, "duration" bigint NULL);
INSERT INTO core_activescenario VALUES(4,2,0,0,2,NULL);
INSERT INTO core_activescenario VALUES(5,2,0,0,2,NULL);
INSERT INTO core_activescenario VALUES(6,2,0,0,2,NULL);
INSERT INTO core_activescenario VALUES(7,2,0,0,2,NULL);
INSERT INTO core_activescenario VALUES(8,2,0,0,2,NULL);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',19);
INSERT INTO sqlite_sequence VALUES('django_admin_log',33);
INSERT INTO sqlite_sequence VALUES('django_content_type',12);
INSERT INTO sqlite_sequence VALUES('auth_permission',48);
INSERT INTO sqlite_sequence VALUES('auth_user',1);
INSERT INTO sqlite_sequence VALUES('core_device',2);
INSERT INTO sqlite_sequence VALUES('core_command',3);
INSERT INTO sqlite_sequence VALUES('core_command_devices',6);
INSERT INTO sqlite_sequence VALUES('core_riddle',5);
INSERT INTO sqlite_sequence VALUES('core_riddle_commands',2);
INSERT INTO sqlite_sequence VALUES('core_scenario_riddles',6);
INSERT INTO sqlite_sequence VALUES('core_scenario',3);
INSERT INTO sqlite_sequence VALUES('core_activescenario',8);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "core_riddle_commands_riddle_id_command_id_45e7f2ac_uniq" ON "core_riddle_commands" ("riddle_id", "command_id");
CREATE INDEX "core_riddle_commands_riddle_id_9ffb9841" ON "core_riddle_commands" ("riddle_id");
CREATE INDEX "core_riddle_commands_command_id_9f4ab1d6" ON "core_riddle_commands" ("command_id");
CREATE UNIQUE INDEX "core_scenario_riddles_scenario_id_riddle_id_eb0414f6_uniq" ON "core_scenario_riddles" ("scenario_id", "riddle_id");
CREATE INDEX "core_scenario_riddles_scenario_id_dbb0e2b8" ON "core_scenario_riddles" ("scenario_id");
CREATE INDEX "core_scenario_riddles_riddle_id_686f5484" ON "core_scenario_riddles" ("riddle_id");
CREATE UNIQUE INDEX "core_command_devices_command_id_device_id_b5181b32_uniq" ON "core_command_devices" ("command_id", "device_id");
CREATE INDEX "core_command_devices_command_id_9ff141e9" ON "core_command_devices" ("command_id");
CREATE INDEX "core_command_devices_device_id_618578ae" ON "core_command_devices" ("device_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE INDEX "core_activescenario_scenario_id_5b2b6d62" ON "core_activescenario" ("scenario_id");
COMMIT;