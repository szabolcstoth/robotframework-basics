# 3.0. Set up a remote host

!!! info "Hints"
    If you already have a remote host with an `OpenSSH` server configured, you can skip this step. (The following exercises will use password-based authentication, but the `SSHLibrary` also supports key-based authentication.)

    The prerequisite for the next steps is to have an already installed and configured [Docker Engine](https://docs.docker.com/engine/install/).

We will use the [openssh-server](https://hub.docker.com/r/linuxserver/openssh-server) container from the [LinuxServer.io](https://www.linuxserver.io/) team to quickly set up a restricted and sandboxed environment that we can ssh into.

Create an `openssh-server` based container with the following command.

``` bash
docker create \
  --name=openssh-server-for-robot \
  --hostname=openssh-server-for-robot \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Budapest \
  -e SUDO_ACCESS=true \
  -e PASSWORD_ACCESS=true \
  -e USER_PASSWORD=Hn7c5%lyBpIn8*8Z \
  -e USER_NAME=robotdev \
  -p 2222:2222 \
  --restart unless-stopped \
  linuxserver/openssh-server
```

Verify that your container has been created.

``` bash
docker container ls --all --filter "name=openssh-server-for-robot"
```

    CONTAINER ID        IMAGE                        COMMAND             CREATED             STATUS              PORTS               NAMES
    95313a9f85f1        linuxserver/openssh-server   "/init"             3 minutes ago       Created                                 openssh-server-for-robot

Start the container.

``` bash
docker container start openssh-server-for-robot
```

Try to access it using ssh.

``` bash
ssh robotdev@localhost -p 2222
```

    The authenticity of host '[localhost]:2222 ([127.0.0.1]:2222)' can't be established.
    ECDSA key fingerprint is SHA256:x4bTJ6bxYJEp4zMk9sQMYhK8ou8oQrm6aCsKaBnj+2o.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?

You should see the following prompt.

    Welcome to OpenSSH Server

    openssh-server-for-robot:~$

That is it, you are good to go!
