INSERT INTO notes (title, content)
SELECT
    CASE WHEN i = 25000 THEN 'target-note' ELSE 'note-' || i END,
    'seeded content ' || i
FROM generate_series(1, 50000) AS i;
