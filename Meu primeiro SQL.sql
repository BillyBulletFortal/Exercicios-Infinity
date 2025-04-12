-- Arquivo para criação de banco de dados - meu primeiro SQL script
create database aula01_71;  -- cria o banco de dados vazio
use aula01_71; -- iniciar o uso
-- drop database aula01_71; -- destroi o banco de dados

create table alunos(
	id int auto_increment primary key, -- ele se auto incrementa, ou seja ele é criado automaticamente pelo sistema
	nome varchar(50) not null, -- varchar vai ate (255) - not null é uma restrição (constraint)
    cpf char(11) unique, -- unique restringe para que so exista um do valor
    descricao text, -- numero ilimitado de caracteres, nao vai funcionar bem como variavel , ocupa 1024bytes
    idade int, -- numeros inteiros ate 11 digitos
	mensalidade decimal(5,2), -- float normal tem 16 algarismos podendo ser somente 8 ou 4 - o decimal voce decide quantos algarismo antes e depois da virgula
    media_final decimal(3,1),
    data_matricula date, -- aaa/mm/dd
    horario_aula time, -- hh:mm:ss
    matricula_ativa bool 
    );