FROM openjdk:22-jdk-slim

WORKDIR /app

COPY target/docker_java-1.0-SNAPSHOT.jar /app/docker_java.jar

ENTRYPOINT ["java", "-jar", "/app/docker_java.jar"]
