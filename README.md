# demo-CD

## Pour utiliser le workflow
- Créer un AKS sur azure
- Créer un ACR sur azure
- lancer la commande 
```shell
az ad sp  create-for-rbac --name "demo" --role contributor --scope /subscriptions/<ID dabonnement>/resourceGroups/<nom du groupe de resource> --sdk-auth
```
 en remplacant `<ID dabonnement>` par uuid de votre abonnement AZURE et `<nom du groupe de resource>` par le nom de votre groupe de ressource (trouvable sur la page de ressource de votre AKS ou ACR)

 - récupérer le JSON en résultat de la commande precedente.
 - Créer les secrets suivant:
    - `AZURE_CREDENTIALS` contenant le JSON
    - `REGISTRY_USERNAME` cotnenant clientID du JSON
    - `REGISTRY_PASSWORD` contenant clientSecret du JSON
    - `REGISTRY_LOGIN_SERVER` contenant le nom de votre ACR

## Lancer le workflow
- effectuer un changement.
- faire un commit
- lancer la commande `git tag vx.x.x` pour changer la version
- faire un `git push`
- faire un `git push --tags` 