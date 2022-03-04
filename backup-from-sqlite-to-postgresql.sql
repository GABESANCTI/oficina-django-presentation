INSERT INTO blog_categoria (nome)
VALUES ('Banco de Dados'),
       ('SCRUM'),
       ('Lógica'),
       ('Banco de Dados 2'),
       ('HTML'),
       ('Banco de Dados 3'),
       ('Programação');

SELECT *
FROM blog_categoria;

INSERT INTO blog_post (titulo, conteudo, criado_em, alterado_em)
VALUES ('HTML é uma linguagem de programação', 'Lorem ipsum', '2021-11-06 01:23:30.037167',
        '2021-11-06 01:23:30.037167'),
       ('MySQL', 'SELECT * FROM POSTS', '2021-11-06 01:30:39.965735', '2021-11-06 01:30:39.965735');

SELECT *
FROM blog_post;

INSERT INTO blog_post_categorias (post_id, categoria_id)
VALUES (1, 7),
       (1, 6),
       (2, 2),
       (2, 5),
       (2, 7);

SELECT *
FROM blog_post_categorias;

INSERT INTO blog_comentario (autor, mensagem, criado_em, post_id)
VALUES ('Carolina', 'Muito bom', '2021-11-06 01:46:37.062588', 1),
       ('Pedro', 'Legal', '2021-11-06 01:46:51.727444', 1),
       ('Andressa', 'Adoro o MySQL, pra mim é o melhor Banco de Dados que existe!!!!', '2022-03-04 04:02:35.500811', 2);