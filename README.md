# POC: Boas práticas e padrões de projeto

## POC-MVC-MVCSR-MVCSRTO

Projeto visa por em prática parte do conhecimento obtido por meio da Pós-Graduação em Arquitetura de Sistemas Distribuídos - PUC Minas.

O projeto possui seu estilo de arquitetura baseada em serviços, em que cada módulo (serviço), possui tudo relacionado a sí e todos utilizam um único banco de dados.

Projeto base:
TODO List API

User
 * CRUD

Task
 * CRUD

Auth
* Login
* Sign in
* Sign out

--
Padrão arquitetural (Architectural Pattern) x Padrão de projeto (Design Pattern)

A diferença principal é o Escopo.

A arquitetura envolve o macro do projeto - "quais classes teremos, como irão interagir", "que módulos de alto nível terão em nossa arquitetura orientada a serviços e como elas se comunicarão", "quantos níveis nossa arquitetura client-server terá"

Exemplo: MVC, MVVM, micro front-end, monorepo, multirepo, hexagonal..

Em contra-partida os design patterns (padrões de projetos) são uma maneira de resolver um problema localizado, envolvem trechos específicos, tem menos impacto na base de código. - "Como fazer com que um objeto se comportar de maneira diferente de acordo com o seu estado (doente se move mais lento, saudável é mais rápido)?"

Exemplo: 

State, Strategy, Observer, Decorator, Facade, Composite, Factory Method, Builder, Singleton, Prototype


Obs.: Existem controversias nesta questão, e.g. há quem considere MVC um design pattern, e quem o considere como um Architectural Pattern. Pois o MVC define como as classes irão se comunicar, porém ele também pode impactar toda a organização do projeto.
