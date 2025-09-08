# novo repositorio
def novo_repositorio():
    from obj.new.new import create
    create()

# salvar projeto em um repositorio
def salvar_projeto(caminho):
    from obj.save.save import save
    save(caminho)

def atualizar_repositorio(caminho):
    from obj.updt.updt import updt
    updt(caminho)


# teste
if __name__ == "__main__":
    salvar_projeto("/caminho/para/o/projeto")