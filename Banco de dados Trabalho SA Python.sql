create database barbearia;

use barbearia;

create table agendamentos(
id int auto_increment primary key,
cliente varchar(100) not null,
telefone varchar(20),
servico varchar(100),
preco decimal(10,2),
barbeiro varchar(50),
data date not null,
horario varchar(5),
status enum("Agendado", "Concluido", "Cancelado")
);

iINSERT INTO agendamentos (cliente, telefone, servico, preco, barbeiro, data, horario, status)
Values('Gedian', '(47)992165428', 'Corte de cabelo', 55.00, 'Lucas', '2026-09-20', '10:50', 'Agendado'),
('Kauã', '(47)991544034', 'Corte de cabelo e barba', 75.00, 'Otavio', '2026-09-25', '15:30', 'Agendado'),
('Weslley', '(47)33752968', 'Corte de cabelo', 55.00, 'André', '2026-09-08', '09:00', 'Concluido'),
('Willian', '(47)998476952', 'Corte de cabelo', 55.00, 'Lucas', '2026-09-01', '10:00', 'Cancelado'),
('Guilherme', '(47)996213498', 'Barba', 30.00, 'Enzo', '2026-09-05', '14:00', 'Concluido'),
('Nicolas', '(47)997456213', 'Corte de cabelo e barba', 75.00, 'André', '2026-10-10', '11:00', 'Agendado'),
('Kelvin', '(47)996523149', 'Barba', 30.00, 'Lucas', '2026-09-29', '16:00', 'Agendado'),
('Henrique', '(47)995642879', 'Corte de cabelo', 55.00, 'Otavio', '2026-10-01', '17:30', 'Cancelado');

select * from agendamentos;