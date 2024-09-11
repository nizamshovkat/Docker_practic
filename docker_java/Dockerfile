# Используем базовый образ с JDK 17
FROM openjdk:22-jdk-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем скомпилированный JAR-файл в контейнер
COPY target/docker_java-1.0-SNAPSHOT.jar /app/docker_java.jar

# Указываем команду для запуска JAR-файла
ENTRYPOINT ["java", "-jar", "/app/docker_java.jar"]
