# Celery: Um sistema de fila de tarefas distribuídas que permite o processamento assíncrono de tarefas em segundo plano, frequentemente usado para gerenciar tarefas de longa duração.

# Corrotinas: Funções especiais em Python que podem ser pausadas e retomadas, permitindo a execução de operações assíncronas de forma eficiente.

# Locks: Mecanismos de controle de concorrência que garantem que apenas uma tarefa possa acessar um recurso compartilhado por vez, prevenindo condições de corrida.

# PyTest: Uma ferramenta de teste em Python que suporta a execução de testes assíncronos, permitindo verificar a funcionalidade de código assíncrono.

# Semáforos: Estruturas de dados usadas para controlar o acesso a múltiplos recursos compartilhados, permitindo que um número limitado de tarefas acesse o recurso simultaneamente.

# Tarefas Assíncronas: Operações que são executadas de forma não bloqueante, permitindo que outras operações continuem enquanto aguardam a conclusão.

# Teste de Funções Assíncronas: O processo de verificar a funcionalidade e a correção de funções que executam operações assíncronas, garantindo que se comportem conforme o esperado.

# Tratamento de Exceções Assíncronas: A prática de capturar e lidar com erros que ocorrem durante a execução de tarefas assíncronas, garantindo que não interrompam o fluxo de execução do programa.




# Por que é importante lidar com exceções em tarefas assíncronas?: Lidar com exceções em tarefas assíncronas é crucial para garantir que erros sejam capturados e tratados adequadamente, sem interromper a execução de outras tarefas. Isso ajuda a manter a aplicação estável e funcional, mesmo quando ocorrem falhas em partes específicas do sistema.


# Como o asyncio e o async for são utilizados no processamento assíncrono?: O asyncio é uma biblioteca do Python que fornece uma infraestrutura para escrever código assíncrono usando a sintaxe async/await. O async for é utilizado para iterar sobre objetos assíncronos, permitindo um controle mais refinado e eficiente ao trabalhar com recursos como conexões de banco de dados e arquivos.


# Qual é a importância do processamento assíncrono com bancos de dados?: O processamento assíncrono com bancos de dados é importante para realizar operações não bloqueantes, melhorando a performance das APIs e evitando gargalos em sistemas de alta demanda. Isso permite que a aplicação continue a processar outras tarefas enquanto aguarda a conclusão de operações de banco de dados.


# Como o FastAPI se integra com o Celery para gerenciar tarefas em segundo plano?: O FastAPI pode ser integrado com o Celery para gerenciar tarefas de longo prazo em segundo plano, como envio de e-mails ou processamento de dados pesados. O Celery permite que essas tarefas sejam executadas assincronamente, liberando a aplicação principal para continuar respondendo a solicitações de usuários.


# Quais são as técnicas de otimização de desempenho discutidas no módulo?: O módulo discute várias técnicas de otimização de desempenho, incluindo o uso de semáforos e locks para controle de concorrência, a implementação de operações não bloqueantes e a gestão eficiente de recursos e tarefas assíncronas em produção para evitar sobrecarga e garantir alta disponibilidade.


# Por que os testes de funções assíncronas são importantes?: Os testes de funções assíncronas são importantes para assegurar a qualidade e manutenção do código. Utilizando ferramentas como o PyTest, os desenvolvedores podem verificar se as funções assíncronas estão se comportando conforme o esperado, identificando e corrigindo problemas antes que eles afetem a produção.


# O que são corrotinas e por que são importantes?: Corrotinas são funções que podem ser pausadas e retomadas, permitindo a execução de métodos assíncronos de forma mais eficiente. Elas são fundamentais para o processamento assíncrono, pois permitem que a aplicação continue a executar outras tarefas enquanto aguarda a conclusão de operações demoradas.


# Quais são os erros comuns no desenvolvimento de software assíncrono?: Erros comuns no desenvolvimento de software assíncrono incluem ignorar a ordem de execução dos processos, não armazenar processos em variáveis e a falta de testes para código assíncrono. Esses erros podem levar a comportamentos inesperados e falhas na aplicação.
