-- ЗАДАНИЕ 2

SELECT name, duration FROM track
ORDER BY duration DESC
LIMIT 1;

SELECT name, duration FROM track
WHERE duration < 210;

SELECT name FROM collection
WHERE date_create BETWEEN '2018-01-01' AND '2021-01-01';

SELECT nickname FROM artist
WHERE LENGTH(nickname) - LENGTH(REPLACE(nickname, ' ', '')) = 0

SELECT name FROM track
WHERE name LIKE '%My%';


-- ЗАДАНИЕ 3

SELECT s.name AS название_группы, COUNT(a.id) AS количество_пользователей
FROM style AS s
LEFT JOIN style_artist AS sa ON s.id = sa.style_id
LEFT JOIN artist AS a ON sa.artist_id = a.id
GROUP BY s.name
ORDER BY s.name;


-- Количество треков, вошедших в альбомы 2019–2020 годов.

SELECT COUNT(t.name) AS Количество_треков, a.date_create AS дата_создания
FROM track AS t
LEFT JOIN album AS a on a.id = t.album_id
where a.date_create BETWEEN '2019-01-01' AND '2021-01-01'
group by a.date_create;

-- Средняя продолжительность треков по каждому альбому.

SELECT AVG(t.duration) AS среднее_время, a.name AS имя_альбома
FROM track AS t
LEFT JOIN album AS a ON a.id = t.album_id
GROUP BY a.name;

-- Все исполнители, которые не выпустили альбомы в 2020 году.КАК УБРАТЬ ФРЕДДИ ИЗ ВЫДАЧИ?

SELECT ar.name AS имя_артиста
FROM artist AS ar
WHERE ar.id NOT IN (
    SELECT al_ar.artist_id
    FROM album_artist AS al_ar
    JOIN album AS al ON al.id = al_ar.album_id
    WHERE al.date_create BETWEEN '2020-01-01' AND '2020-12-31'
)
GROUP BY ar.name;

-- Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами) - Queen.

SELECT col.name AS название_соборника, tr.name
FROM collection AS col
LEFT JOIN track_collection AS tr_col ON col.id = tr_col.collection_id
LEFT JOIN track AS tr ON tr.id = tr_col.track_id
LEFT JOIN album AS al ON al.id = tr.album_id
LEFT JOIN album_artist AS al_ar ON al_ar.album_id = al.id
LEFT JOIN artist AS ar ON ar.id = al_ar.artist_id
WHERE ar.nickname = 'Queen'
