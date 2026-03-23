# Docker Compose: Uma ferramenta que permite definir e gerenciar multi-containers Docker applications. Com ele, é possível orquestrar múltiplos serviços, como bancos de dados e caches, simplificando a gestão de ambientes complexos.

# Dockerfile: Um script de texto que contém uma coleção de comandos que são executados para montar uma imagem Docker. Ele é essencial para encapsular aplicações em containers.

# FastAPI: Um framework moderno e de alto desempenho para construir APIs com Python 3.6+ baseado em padrões como OpenAPI e JSON Schema, utilizado para desenvolver aplicações backend.

# Podman: Uma ferramenta de gerenciamento de containers que serve como uma alternativa ao Docker, permitindo executar e gerenciar containers com consistência em diferentes ambientes.

# Imagens personalizadas: Imagens Docker criadas especificamente para atender às necessidades de uma aplicação, com foco em otimização e segurança, permitindo controle total sobre o ambiente de execução.

# Imagens verificadas: Imagens oficiais disponíveis no Docker Hub que passaram por verificações de segurança e são recomendadas para uso em produção para garantir segurança e confiabilidade.

# Monitoração contínua: O processo de monitorar constantemente os containers e logs para identificar e resolver problemas rapidamente, garantindo a estabilidade e segurança das aplicações.

# Privilégios desnecessários: Privilégios que não são essenciais para a execução de uma aplicação e que devem ser desativados para garantir que apenas usuários autorizados tenham acesso a determinadas funcionalidades.




# O que é um Dockerfile e por que é importante?: Um Dockerfile é um script de texto que contém uma série de instruções para construir uma imagem Docker. Ele é importante porque define como a aplicação será encapsulada em um container, especificando o ambiente de execução, as dependências e as configurações necessárias para que a aplicação funcione corretamente.


# Como o Docker Compose facilita a gestão de ambientes complexos?: O Docker Compose facilita a gestão de ambientes complexos ao permitir que múltiplos serviços, como aplicações, bancos de dados e caches, sejam definidos e orquestrados em um único arquivo YAML. Isso simplifica o processo de configuração e execução de ambientes de desenvolvimento e produção, garantindo que todos os serviços necessários sejam iniciados e configurados corretamente.


# Por que é importante "dockerizar" aplicações FastAPI?: "Dockerizar" aplicações FastAPI é importante porque transforma a aplicação em uma unidade portátil e fácil de gerenciar. Isso garante que a aplicação possa ser executada de forma consistente em diferentes ambientes, seja localmente ou na nuvem, facilitando o desenvolvimento, a implantação e a escalabilidade.


# Qual é o papel das variáveis de ambiente e volumes no Docker?: As variáveis de ambiente no Docker são usadas para configurar a aplicação sem alterar o código-fonte, permitindo flexibilidade e segurança. Os volumes são usados para persistir dados fora dos containers, garantindo que os dados não sejam perdidos quando o container é removido ou atualizado.


# O que é o Podman e como ele se compara ao Docker?: O Podman é uma ferramenta de gerenciamento de containers que serve como uma alternativa ao Docker. Ele oferece funcionalidades semelhantes, mas com algumas diferenças, como a capacidade de executar containers sem privilégios de root. O Podman é conhecido por sua segurança e flexibilidade, permitindo que aplicações sejam executadas de forma consistente em diferentes ambientes.


# Quais são os riscos de usar imagens de terceiros no Docker?: Usar imagens de terceiros no Docker pode introduzir riscos de segurança, pois essas imagens podem conter vulnerabilidades ou configurações inadequadas. É importante desenvolver imagens próprias ou usar imagens oficiais e verificadas para garantir segurança e adequação às necessidades específicas das empresas.


# Por que é importante manter as imagens Docker atualizadas?: Manter as imagens Docker atualizadas é importante para aproveitar melhorias de segurança e correções de bugs. Imagens desatualizadas podem conter vulnerabilidades que podem ser exploradas por atacantes, colocando em risco a segurança da aplicação e dos dados.


# Quais práticas de segurança devem ser adotadas ao usar Docker?: Práticas de segurança ao usar Docker incluem não armazenar senhas e credenciais dentro dos containers, remover containers e imagens não utilizadas, desativar privilégios desnecessários e monitorar continuamente os containers e logs para identificar e resolver problemas rapidamente.


# Como a monitoração contínua dos containers ajuda na segurança?: A monitoração contínua dos containers ajuda na segurança ao permitir que problemas sejam identificados e resolvidos rapidamente. Isso inclui monitorar logs para detectar atividades suspeitas, verificar o uso de recursos e garantir que os containers estejam funcionando conforme o esperado.
