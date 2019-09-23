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

#ADICIONANDO AVES
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

SELECT * FROM cidade;
SELECT * FROM usuario;
