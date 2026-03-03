# Arquitetura de Microsserviços: Uma abordagem arquitetural que divide um sistema em pequenos serviços independentes, cada um executando um processo único e comunicando-se através de APIs. Isso permite escalabilidade e flexibilidade, pois cada serviço pode ser desenvolvido e implantado de forma independente.

# Arquitetura Monolítica: Um estilo arquitetural onde todo o sistema é construído como uma única aplicação coesa. É mais simples de desenvolver e implantar, mas pode apresentar desafios de escalabilidade e manutenção à medida que o sistema cresce.

# Comunicação Assíncrona: Um método de comunicação entre sistemas onde as mensagens são enviadas sem esperar por uma resposta imediata, permitindo que o sistema continue processando outras tarefas. Isso melhora a eficiência e escalabilidade.

# Comunicação Síncrona: Um método de comunicação onde o remetente espera por uma resposta imediata antes de continuar o processamento. É comum em chamadas HTTP, mas pode levar a bloqueios se a resposta demorar.

# Escalabilidade: A capacidade de um sistema de lidar com um aumento na carga de trabalho sem comprometer o desempenho. Arquiteturas de microsserviços são particularmente eficazes para alcançar alta escalabilidade.

# Fila de Mensagens: Um sistema que permite a comunicação assíncrona entre diferentes partes de um sistema, armazenando mensagens até que o destinatário esteja pronto para processá-las. Isso desacopla os componentes e melhora a resiliência.

# Independência de Serviços: Um princípio dos microsserviços onde cada serviço é autônomo e pode ser desenvolvido, implantado e escalado independentemente dos outros, aumentando a resiliência e flexibilidade do sistema.

# PokeAPI: Um exemplo prático de uma aplicação monolítica que demonstra como um sistema pode ser eficiente em cenários específicos, mesmo lidando com grandes volumes de requisições.

# Resiliência: A capacidade de um sistema de continuar operando corretamente mesmo em face de falhas ou problemas. Arquiteturas de microsserviços aumentam a resiliência ao isolar falhas em serviços individuais.

# Sistemas Escaláveis: Sistemas projetados para crescer e se adaptar a um aumento na carga de trabalho sem comprometer o desempenho, frequentemente utilizando arquiteturas de microsserviços para alcançar esse objetivo.




# O que é arquitetura de software e por que é importante?: Arquitetura de software refere-se à estrutura fundamental de um sistema de software, incluindo seus componentes e a interação entre eles. É importante porque influencia a escalabilidade, flexibilidade e eficiência do sistema, além de facilitar a manutenção e o desenvolvimento contínuo.


# Qual é a diferença entre arquitetura monolítica e de microsserviços?: A arquitetura monolítica desenvolve todo o sistema como uma única aplicação, ideal para projetos menores devido à sua simplicidade. Já a arquitetura de microsserviços divide o sistema em partes independentes, permitindo desenvolvimento, implantação e escalabilidade separadas, tornando-a adequada para sistemas maiores e mais complexos.


# Quais são as vantagens da arquitetura de microsserviços?: A arquitetura de microsserviços oferece alta escalabilidade, resiliência e flexibilidade, permitindo que diferentes partes do sistema sejam desenvolvidas e escaladas independentemente. Isso evita que falhas em um serviço afetem todo o sistema, garantindo maior disponibilidade.


# O que é comunicação síncrona e assíncrona entre sistemas?: Comunicação síncrona ocorre quando um sistema envia uma solicitação e espera uma resposta imediata, como via HTTP. Comunicação assíncrona usa sistemas de filas de mensagens, permitindo que o sistema continue processando outras tarefas enquanto aguarda uma resposta, melhorando a eficiência e escalabilidade.


# Quando é mais adequado usar comunicação assíncrona?: Comunicação assíncrona é mais adequada em cenários onde a resposta imediata não é crítica, como no processamento de pagamentos ou tarefas de longa duração. Isso permite que o sistema continue operando sem ficar bloqueado, melhorando a eficiência geral.


# Quais são os desafios de implementar microsserviços?: Implementar microsserviços pode ser desafiador devido à complexidade e necessidade de coordenação entre múltiplos serviços. Isso pode aumentar a possibilidade de erros, exigindo uma equipe bem estruturada e experiente para garantir uma implementação bem-sucedida.


# Por que a arquitetura monolítica ainda é relevante?: A arquitetura monolítica é relevante para projetos menores ou geridos por um único desenvolvedor devido à sua simplicidade e menor complexidade. Para sistemas que não exigem alta escalabilidade, ela pode ser uma solução eficiente e prática.


# Como a PokeAPI ilustra o uso de arquitetura monolítica?: A PokeAPI é um exemplo de como sistemas monolíticos podem ser eficientes em cenários específicos, lidando com grandes volumes de requisições de forma eficaz, demonstrando que a arquitetura monolítica pode ser apropriada para certos tipos de aplicações.
