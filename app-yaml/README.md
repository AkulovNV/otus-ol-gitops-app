argocd app create nginx-app \
  --repo https://github.com/AkulovNV/otus-ol-gitops-app.git \
  --path . \
  --dest-server https://kubernetes.default.svc \
  --dest-namespace nginx-app \
  --sync-policy automated \
  --self-heal \
  --sync-option CreateNamespace=true

# Change image: nginx:1.27 -> nginx:1.28
argocd app sync nginx-app 