# 🛠️ Energys — Sistema de Gestão em Python

O **Energys** é um projeto acadêmico desenvolvido para simular o fluxo de um sistema de gerenciamento voltado ao setor alimentício.
A aplicação funciona inteiramente via console, utilizando **Python** como linguagem principal e **MySQL** para armazenamento de dados.

---

## 📌 Objetivo do Projeto

O sistema foi criado com o propósito de aplicar conceitos fundamentais aprendidos no primeiro semestre da faculdade, como:

* Organização de código e **Clean Code**
* Separação de responsabilidades (princípio **SRP — Single Responsibility Principle**)
* Noções de **segurança** e **LGPD**, incluindo criptografia de senhas
* Integração com banco de dados
* Simulação de permissões e níveis de acesso

---

## 👥 Tipos de Usuário

* **Usuário comum:**
  Pode visualizar produtos, gerenciar seu perfil e adicionar itens ao carrinho.

* **Administrador:**
  Tem acesso completo ao CRUD de produtos e categorias.

Essa separação foi aplicada para representar controles de acesso reais em sistemas profissionais.

---

## 🔒 Segurança

O projeto utiliza bibliotecas de **criptografia de senha**, garantindo que credenciais não fiquem expostas nem para administradores, seguindo boas práticas de proteção e privacidade.

---

## 🧼 Organização do Sistema

O código foi dividido em módulos e pastas para manter clareza, facilitar manutenção e permitir evolução futura do projeto.
Cada arquivo possui **uma única responsabilidade**, tornando o sistema mais limpo e compreensível.

---

## 🧪 Sobre o Projeto

Este é um **trabalho simples de faculdade**, mas estruturado de forma profissional para demonstrar:

* Uso de Python em aplicações reais
* Modelagem de fluxo de usuários
* Implementação de menus e lógicas de carrinho
* Interação com banco de dados
* Noções básicas de arquitetura de software
