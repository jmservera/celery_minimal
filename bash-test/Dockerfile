FROM alpine:latest

# RUN apk add --no-cache strace pstree tini

# ENTRYPOINT ["/sbin/tini", "-g", "--"]
# Copy the script to the container
COPY spawntest.sh /app/spawntest.sh

# Make the script executable
RUN chmod +x /app/spawntest.sh

# Set the working directory
WORKDIR /app

CMD ["./spawntest.sh"]

