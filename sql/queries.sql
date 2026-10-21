-- 1. Все файлы пользователя
SELECT * FROM archive_archivefile WHERE owner_id = ?;
-- 2. Новые файлы
SELECT * FROM archive_archivefile ORDER BY created_at DESC LIMIT 10;
-- 3. Поиск по названию
SELECT * FROM archive_archivefile WHERE title LIKE ?;
-- 4. Поиск по описанию
SELECT * FROM archive_archivefile WHERE description LIKE ?;
-- 5. Файлы в папке
SELECT * FROM archive_archivefile WHERE folder_id = ?;
-- 6. Файл и его папка
SELECT f.title, d.name FROM archive_archivefile f
LEFT JOIN archive_folder d ON d.id = f.folder_id;
-- 7. Файл и теги
SELECT f.title, t.name FROM archive_archivefile f
JOIN archive_archivefile_tags ft ON ft.archivefile_id = f.id
JOIN archive_tag t ON t.id = ft.tag_id;
-- 8. Количество файлов в папках
SELECT folder_id, COUNT(*) FROM archive_archivefile GROUP BY folder_id;
-- 9. Количество файлов пользователей
SELECT owner_id, COUNT(*) FROM archive_archivefile GROUP BY owner_id;
-- 10. Количество использований тегов
SELECT tag_id, COUNT(*) FROM archive_archivefile_tags GROUP BY tag_id;
