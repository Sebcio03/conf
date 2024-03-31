# My scripts and configs for SWE productivity

# Some aliases

```bash
alias py="~/pypy3.10/bin/pypy"
alias pyp="py -m pip"

# Terraform
alias tf="terraform"
alias tfl="tflocal"

# Kubernetes
alias k='kubectl'
alias kg='kubectl get'
alias kgpo='kubectl get pod'

# Docker
alias d="docker"
alias de="docker -it exec"
alias dl="docker logs"
alias di="docker inspect"
alias ds="docker system"
alias dp="docker ps"

# Docker Compose
alias dc="docker compose"
alias dcu="docker compose up"
alias dcub="docker compose up --build"
alias dcd="docker compose down"
alias dcdv="docker compose down --volumes"
alias dcr="docker compose restart"
```

### gptcli

Init gptcli
- mkdir $HOME/gptcli
- cp src/* $HOME/gptcli

```bash
alias jj="python3 $HOME/gptcli/main.py job"
alias nn="python3 $HOME/gptcli/main.py none"
alias mm="python3 $HOME/gptcli/main.py maczsh"
```