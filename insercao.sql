#ADICIONANDO CIDADES
CALL adiciona_cidade('São paulo');
CALL adiciona_cidade('Rio de Janeiro');
CALL adiciona_cidade('Brasilia');
CALL adiciona_cidade('Rio Grande do Sul');
CALL adiciona_cidade('Campinas');
CALL adiciona_cidade('Salvador');
CALL adiciona_cidade('Belo Horizonte');
CALL adiciona_cidade('Florianópois');
CALL adiciona_cidade('Manaus');
CALL adiciona_cidade('Bauru');

#ADICIONANDO USUÁRIOS
CALL adiciona_usuario('Ana', 'Veloso', 'ana.veloso@gmail.com', 'ana_veloso', 1);
CALL adiciona_usuario('Carlos', 'Viana', 'cviana@gmail.com', 'caiov', 1);
CALL adiciona_usuario('Amanda', 'Alencar', 'amandaalencar@gmail.com', 'alencar_amanda', 2);
CALL adiciona_usuario('Monica', 'Borges', 'borgesm@gmail.com', 'monica', 4);
CALL adiciona_usuario('Eduardo', 'Silva', 'edu_silva@gmail.com', 'dudu_silva', 7);
CALL adiciona_usuario('Gabriel', 'Lisboa', 'gabriel_lisboa@gmail.com', 'gabriel.l', 3);
CALL adiciona_usuario('Luciana', 'Monaco', 'luci_m@gmail.com', 'luciana_m', 6);
CALL adiciona_usuario('Giovana', 'Sipolati', 'giovanas@gmail.com', 'giovanas', 1);
CALL adiciona_usuario('André', 'Coelho', 'andrecc@gmail.com', 'coelho_a', 5);
CALL adiciona_usuario('Lucas', 'Blunk', 'lucasblunck@gmail.com', 'blunk_lucas', 8);
CALL adiciona_usuario('Otávio', 'Hon', 'otavio.hon@gmail.com', 'otaviohon', 10);
CALL adiciona_usuario('Rafaela', 'Bosi', 'rafabosi@gmail.com', 'rafabosi', 1);
CALL adiciona_usuario('Julia', 'Campos', 'jucampos@gmail.com', 'jucampos', 1);

#ADICIONANDO PASSAROS
CALL adiciona_passaro('Canário');
CALL adiciona_passaro('Bem-te-vi');
CALL adiciona_passaro('Papagaio');
CALL adiciona_passaro('Periquito');
CALL adiciona_passaro('Tucano');
CALL adiciona_passaro('Calopsita');
CALL adiciona_passaro('Cacatua');
CALL adiciona_passaro('Agapornis');
CALL adiciona_passaro('Perdiz');
CALL adiciona_passaro('Galinha');
CALL adiciona_passaro('Flamingo');
CALL adiciona_passaro('Pinguim-rei');
CALL adiciona_passaro('Albatroz-real');
CALL adiciona_passaro('Garça-azul');
CALL adiciona_passaro('Arara-azul');
CALL adiciona_passaro('Arara');
CALL adiciona_passaro('Ararinha');
CALL adiciona_passaro('Pardal');

#ADICIONANDO PREFERENCIAS
CALL adiciona_preferencia(1,1);
CALL adiciona_preferencia(1,4);
CALL adiciona_preferencia(1,10);
CALL adiciona_preferencia(2,1);
CALL adiciona_preferencia(2,18);
CALL adiciona_preferencia(3,3);
CALL adiciona_preferencia(3,12);
CALL adiciona_preferencia(3,13);
CALL adiciona_preferencia(3,16);
CALL adiciona_preferencia(4,2);
CALL adiciona_preferencia(4,5);
CALL adiciona_preferencia(5,7);
CALL adiciona_preferencia(6,11);
CALL adiciona_preferencia(6,17);
CALL adiciona_preferencia(7,15);
CALL adiciona_preferencia(7,18);
CALL adiciona_preferencia(8,12);
CALL adiciona_preferencia(8,13);
CALL adiciona_preferencia(8,15);
CALL adiciona_preferencia(8,16);
CALL adiciona_preferencia(9,9);
CALL adiciona_preferencia(10,1);
CALL adiciona_preferencia(10,4);
CALL adiciona_preferencia(10,5);
CALL adiciona_preferencia(11,2);
CALL adiciona_preferencia(11,17);
CALL adiciona_preferencia(12,2);
CALL adiciona_preferencia(13,14);
CALL adiciona_preferencia(13,15);
CALL adiciona_preferencia(13,18);

#ADICIONDO POSTS
CALL adiciona_post(1,'Visita ao parque', 'Encontrei um #Canário durante a visita ao Ibirapuera com o @caiov', 'www.fotourl.com/12345'); 
CALL adiciona_post(10,'Parque dos pássaros', 'Visitei hoje o parque dos pássaros! Ótima oportunidade para observar diversas espécies', 'www.fotourl.com/56789'); 

SELECT * FROM cidade;
SELECT * FROM usuario;
