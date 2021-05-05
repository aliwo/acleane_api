INSERT INTO amounts(id, created_at, name) VALUES (1, NOW(), '1 알');
INSERT INTO amounts(id, created_at, name) VALUES (2, NOW(), '2 알');
INSERT INTO amounts(id, created_at, name) VALUES (3, NOW(), '3 알');
INSERT INTO amounts(id, created_at, name) VALUES (4, NOW(), '4 알');
INSERT INTO amounts(id, created_at, name) VALUES (5, NOW(), '1 방울');
INSERT INTO amounts(id, created_at, name) VALUES (6, NOW(), '2 방울');
INSERT INTO amounts(id, created_at, name) VALUES (7, NOW(), '3 방울');
INSERT INTO amounts(id, created_at, name) VALUES (8, NOW(), '10원 동전 크기');
INSERT INTO amounts(id, created_at, name) VALUES (9, NOW(), '3000IU');
INSERT INTO amounts(id, created_at, name) VALUES (10, NOW(), '10000IU');
INSERT INTO amounts(id, created_at, name) VALUES (11, NOW(), '20000IU');
INSERT INTO amounts(id, created_at, name) VALUES (12, NOW(), '30000IU');
INSERT INTO amounts(id, created_at, name) VALUES (13, NOW(), '적정량');


-- routines 를 먼저 insert 해야 합니다. --
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 1, 1);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 1, 2);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 1, 3);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 1, 4);

INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 2, 1);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 2, 2);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 2, 3);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 2, 4);

INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 3, 1);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 3, 2);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 3, 3);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 3, 4);

INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 4, 13);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 5, 13);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 6, 13);

INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 7, 5);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 7, 6);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 7, 7);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 7, 8);

INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 8, 5);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 8, 6);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 8, 7);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 8, 8);

INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 9, 10);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 9, 11);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 9, 12);

INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 10, 10);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 10, 11);
INSERT INTO acleane.routine_amount_relations(created_at, routine_id, amount_id) VALUES (NOW(), 10, 12);

