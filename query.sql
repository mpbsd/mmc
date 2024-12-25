select campus.y, curso.y, disciplina.y, horario.y, semestre.y from campus, curso, disciplina, horario, semestre, blob where  (campus.x = blob.campus and curso.x = blob.curso and disciplina.x = blob.disciplina and horario.x = blob.horario and semestre.x = blob.semestre);

campus     curso                      disciplina                              horario  semestre     
---------  -------------------------  --------------------------------------  -------  --------
aparecida  engenharia de transportes  algebra linear                          24m23    2022_2
aparecida  engenharia de producao     algebra linear                          24m45    2022_2
aparecida  engenharia de materiais    algebra linear                          24t23    2022_2
aparecida  engenharia de transportes  calculo numerico                        24m45    2022_2
aparecida  engenharia de producao     calculo numerico                        24t23    2022_2
aparecida  engenharia de materiais    probabilidade e estatistica a           56t23    2022_2
aparecida  engenharia de materiais    geometria analitica                     24t23    2022_2
aparecida  engenharia de producao     inferencia                              24t45    2022_2
aparecida  engenharia de materiais    calculo 1a                              246t23   2022_2
aparecida  engenharia de materiais    calculo 1a                              246t45   2022_2
aparecida  engenharia de materiais    calculo 2a                              246t23   2022_2
aparecida  engenharia de materiais    calculo 2a                              246t45   2022_2
colemar    engenharia eletrica        calculo 1a                              246m12   2022_2
colemar    engenharia de computacao   calculo 1a                              246m34   2022_2
colemar    engenharia civil           edo                                     24m12    2022_2
colemar    engenharia eletrica        edo                                     24m34    2022_2
colemar    engenharia de computacao   edo                                     24m56    2022_2
colemar    engenharia eletrica        calculo 3a                              24m12    2022_2
colemar    engenharia de computacao   calculo 3a                              24m34    2022_2
colemar    engenharia de computacao   calculo numerico                        35m12    2022_2
colemar    engenharia eletrica        calculo numerico                        35m34    2022_2
colemar    engenharia eletrica        geometria analitica                     35m12    2022_2
colemar    engenharia de computacao   matematica discreta                     24m12    2022_2
colemar    engenharia civil           probabilidade e estatistica a           24m34    2022_2
colemar    engenharia civil           calculo 2a                              246m12   2022_2
colemar    engenharia civil           algebra linear                          24m56    2022_2
colemar    engenharia eletrica        calculo 2a                              246t12   2022_2
colemar    engenharia ambiental       calculo 2a                              246t34   2022_2
colemar    engenharia civil           calculo 1a                              246t12   2022_2
colemar    engenharia ambiental       algebra linear                          24t12    2022_2
colemar    engenharia civil           calculo 3a                              24t12    2022_2
colemar    engenharia eletrica        probabilidade e estatistica a           46t34    2022_2
colemar    engenharia civil           geometria analitica                     46t56    2022_2
colemar    farmacia                   bioestatistica                          46t23    2022_2
colemar    nutricao                   bioestatistica                          46t45    2022_2
colemar    medicina                   bioestatistica 2                        4t12     2022_2
colemar    medicina                   bioestatistica 2                        6t12     2022_2
colemar    engenharia eletrica        algebra linear                          35t12    2022_2
colemar    engenharia civil           calculo numerico                        35t34    2022_2
colemar    fisioterapia               bioestatistica                          35t45    2022_2
colemar    engenharia de computacao   calculo 2a                              246n23   2022_2
colemar    psicologia                 estatistica 2                           24n23    2022_2
colemar    engenharia de computacao   probabilidade e estatistica a           24n45    2022_2
colemar    engenharia de computacao   algebra linear                          35n45    2022_2
samambaia  instituto de quimica       calculo 1a                              246m45   2022_2
samambaia  inteligencia artificial    calculo 1a                              246m23   2022_2
samambaia  instituto de quimica       calculo 2a                              246m23   2022_2
samambaia  ciencia da computacao      calculo 2a                              246m45   2022_2
samambaia  engenharia de alimentos    calculo 2a                              246m23   2022_2
samambaia  ciencia da computacao      calculo 1a                              246m45   2022_2
samambaia  gestao da informacao       estatistica 1                           246m23   2022_2
samambaia  ciencias economicas        probabilidade e estatistica b           46m45    2022_2
samambaia  instituto de quimica       calculo 1b                              24m23    2022_2
samambaia  instituto de fisica        calculo 1a                              246m45   2022_2
samambaia  instituto de quimica       calculo 2b                              24m23    2022_2
samambaia  ciencia da computacao      algebra linear                          24m45    2022_2
samambaia  instituto de quimica       edo                                     24m23    2022_2
samambaia  ciencia da computacao      edo                                     24m45    2022_2
samambaia  ciencia da computacao      probabilidade e estatistica a           24m23    2022_2
samambaia  ciencia da computacao      calculo numerico                        24m45    2022_2
samambaia  engenharia de alimentos    algebra linear                          35m23    2022_2
samambaia  ciencias contabeis         calculo 1c                              35m45    2022_2
samambaia  instituto de quimica       estatistica                             35m23    2022_2
samambaia  gestao da informacao       introducao a probabilidade              35m23    2022_2
samambaia  ciencias economicas        calculo 2b                              46m23    2022_2
samambaia  farmacia                   calculo 1c                              46m45    2022_2
samambaia  ciencia da computacao      geometria analitica                     46m23    2022_2
samambaia  instituto de quimica       algebra linear                          46m45    2022_2
samambaia  ciencias contabeis         nocoes de atuaria                       6m23     2022_2
samambaia  instituto de fisica        calculo 2a                              246t12   2022_2
samambaia  instituto de fisica        calculo 2a                              246t34   2022_2
samambaia  engenharia mecanica        calculo 2a                              246t12   2022_2
samambaia  engenharia mecanica        algebra linear                          24t34    2022_2
samambaia  matematica                 probabilidade                           246t12   2022_2
samambaia  agronomia                  calculo 2b                              46t23    2022_2
samambaia  agronomia                  calculo 2b                              46t45    2022_2
samambaia  agronomia                  calculo 1b                              25t23    2022_2
samambaia  agronomia                  calculo 1b                              25t45    2022_2
samambaia  instituto de fisica        algebra linear                          24t12    2022_2
samambaia  instituto de fisica        algebra linear                          24t34    2022_2
samambaia  engenharia florestal       calculo 2b                              24t23    2022_2
samambaia  inteligencia artificial    algebra linear                          24t23    2022_2
samambaia  gestao da informacao       estatistica 1                           35t23    2022_2
samambaia  instituto de quimica       calculo 3a                              35t45    2022_2
samambaia  engenharia de alimentos    calculo numerico                        36t23    2022_2
samambaia  matematica                 estatistica                             35t34    2022_2
samambaia  engenharia mecanica        calculo numerico                        35t12    2022_2
samambaia  estatistica                geometria analitica                     35t34    2022_2
samambaia  engenharia mecanica        probabilidade e estatistica a           35t12    2022_2
samambaia  instituto de fisica        calculo 1a                              246n23   2022_2
samambaia  sistemas de informacao     algebra linear                          24n23    2022_2
samambaia  engenharia de software     algebra linear                          24n45    2022_2
samambaia  engenharia de software     probabilidade e estatistica a           24n23    2022_2
samambaia  sistemas de informacao     probabilidade e estatistica a           24n45    2022_2
samambaia  administracao              calculo 2b                              35n23    2022_2
samambaia  instituto de quimica       calculo 2b                              35n45    2022_2
samambaia  ciencias contabeis         calculo 1c                              35n23    2022_2
samambaia  administracao              calculo 1b                              35n45    2022_2
samambaia  instituto de fisica        calculo 3a                              35n23    2022_2
samambaia  instituto de fisica        edo                                     35n45    2022_2
samambaia  ciencias economicas        calculo 2b                              46n23    2022_2
samambaia  ciencias economicas        probabilidade e estatistica b           46n45    2022_2
samambaia  administracao              estatistica descritiva e probabilidade  46n23    2022_2
samambaia  administracao              estatistica inferencial                 46n45    2022_2
samambaia  ciencias contabeis         nocoes de atuaria                       6n23     2022_2
samambaia  matematica                 estatistica                             35n34    2022_2
samambaia  sistemas de informacao     matematica financeira                   35n45    2022_2
samambaia  matematica                 probabilidade                           35n45    2022_2
aparecida  engenharia de materiais    calculo 1a                              246m23   2023_1
aparecida  engenharia de materiais    calculo 1a                              246m45   2023_1
aparecida  engenharia de materiais    calculo 1a                              246t23   2023_1
aparecida  engenharia de materiais    calculo 1a                              246t45   2023_1
aparecida  engenharia de transportes  geometria analitica                     24m23    2023_1
aparecida  engenharia de producao     geometria analitica                     24m45    2023_1
aparecida  engenharia de materiais    geometria analitica                     24t23    2023_1
aparecida  engenharia de materiais    calculo 3a                              24m45    2023_1
aparecida  engenharia de transportes  calculo 3b                              24t23    2023_1
aparecida  engenharia de producao     calculo 3b                              24t45    2023_1
aparecida  engenharia de transportes  probabilidade e estatistica a           24m23    2023_1
aparecida  engenharia de materiais    probabilidade e estatistica a           24m45    2023_1
aparecida  engenharia de producao     probabilidade e estatistica a           24t23    2023_1
aparecida  engenharia de materiais    probabilidade e estatistica a           24t45    2023_1
colemar    engenharia civil           calculo 2a                              246m12   2023_1
colemar    engenharia de computacao   calculo 2a                              246m34   2023_1
colemar    engenharia eletrica        calculo 1a                              246m12   2023_1
colemar    engenharia de computacao   calculo 1a                              246m34   2023_1
colemar    engenharia eletrica        calculo 3                               24m12    2023_1
colemar    engenharia civil           algebra linear                          24m34    2023_1
colemar    engenharia de computacao   algebra linear                          24m56    2023_1
colemar    engenharia civil           edo                                     24m12    2023_1
colemar    engenharia eletrica        edo                                     24m34    2023_1
colemar    engenharia ambiental       edo                                     24m56    2023_1
colemar    engenharia de computacao   probabilidade e estatistica a           46m12    2023_1
colemar    engenharia ambiental       probabilidade e estatistica a           46m34    2023_1
colemar    engenharia civil           probabilidade e estatistica a           46m56    2023_1
colemar    engenharia eletrica        geometria analitica                     35m12    2023_1
colemar    engenharia eletrica        calculo numerico                        35m34    2023_1
colemar    engenharia civil           calculo 1a                              246t12   2023_1
colemar    engenharia ambiental       calculo 1a                              246t34   2023_1
colemar    engenharia eletrica        calculo 2a                              246t12   2023_1
colemar    engenharia civil           calculo 3a                              24t34    2023_1
colemar    engenharia eletrica        algebra linear                          35t12    2023_1
colemar    engenharia civil           calculo numerico                        35t12    2023_1
colemar    psicologia                 estatistica 1                           35t56    2023_1
colemar    engenharia eletrica        probabilidade e estatistica a           46t34    2023_1
colemar    engenharia civil           geometria analitica                     46t56    2023_1
colemar    farmacia                   bioestatistica                          46t23    2023_1
colemar    nutricao                   bioestatistica                          46t45    2023_1
colemar    medicina                   bioestatistica 1                        4t12     2023_1
colemar    medicina                   bioestatistica 1                        6t12     2023_1
colemar    engenharia de computacao   calculo 1a                              246n23   2023_1
colemar    engenharia de computacao   edo                                     46n45    2023_1
colemar    engenharia de computacao   matematica discreta                     35n23    2023_1
colemar    engenharia de computacao   calculo numerico                        35n45    2023_1
colemar    engenharia de computacao   calculo 3a                              35n45    2023_1
samambaia  engenharia de alimentos    calculo 1a                              246m23   2023_1
samambaia  ciencia da computacao      calculo 1a                              246m45   2023_1
samambaia  instituto de quimica       calculo 1a                              246m23   2023_1
samambaia  engenharia de alimentos    geometria analitica                     46m45    2023_1
samambaia  instituto de quimica       calculo 2a                              246m23   2023_1
samambaia  ciencia da computacao      calculo 2a                              246m45   2023_1
samambaia  gestao da informacao       estatistica 2                           246m23   2023_1
samambaia  ciencias contabeis         estatistica                             46m45    2023_1
samambaia  instituto de quimica       calculo numerico                        24m23    2023_1
samambaia  ciencia da computacao      calculo numerico                        24m45    2023_1
samambaia  ciencias economicas        algebra linear                          24m23    2023_1
samambaia  ciencia da computacao      algebra linear                          24m45    2023_1
samambaia  relacoes internacionais    probabilidade e estatistica             24m23    2023_1
samambaia  relacoes publicas          introducao a estatistica                24m45    2023_1
samambaia  ciencia da computacao      probabilidade e estatistica a           24m23    2023_1
samambaia  inteligencia artificial    probabilidade e estatistica a           24m45    2023_1
samambaia  ciencia da computacao      edo                                     24m45    2023_1
samambaia  instituto de quimica       estatistica                             35m23    2023_1
samambaia  engenharia de alimentos    calculo 3a                              35m23    2023_1
samambaia  ciencia da computacao      geometria analitica                     46m23    2023_1
samambaia  instituto de quimica       algebra linear                          46m45    2023_1
samambaia  ciencias economicas        calculo 1b                              46m23    2023_1
samambaia  engenharia florestal       calculo 1b                              46m45    2023_1
samambaia  instituto de quimica       calculo 1b                              46m23    2023_1
samambaia  farmacia                   calculo 1c                              46m45    2023_1
samambaia  instituto de quimica       calculo 2b                              46m23    2023_1
samambaia  comunicacao social         estatistica                             46m45    2023_1
samambaia  engenharia mecanica        calculo 1a                              246t12   2023_1
samambaia  instituto de fisica        calculo 1a                              246t34   2023_1
samambaia  instituto de fisica        calculo 1a                              246t56   2023_1
samambaia  matematica                 analise real 1                          246t34   2023_1
samambaia  matematica                 estatistica                             246t56   2023_1
samambaia  zootecnia                  calculo 1c                              24t23    2023_1
samambaia  ciencias biologicas        calculo 1c                              24t45    2023_1
samambaia  agronomia                  calculo 1b                              25t23    2023_1
samambaia  agronomia                  calculo 1b                              25t45    2023_1
samambaia  instituto de fisica        geometria analitica                     24t12    2023_1
samambaia  engenharia mecanica        geometria analitica                     24t34    2023_1
samambaia  instituto de fisica        probabilidade e estatistica a           24t12    2023_1
samambaia  instituto de fisica        edo                                     24t34    2023_1
samambaia  engenharia mecanica        edo                                     24t56    2023_1
samambaia  engenharia mecanica        calculo 3a                              24t34    2023_1
samambaia  instituto de fisica        calculo 3a                              24t56    2023_1
samambaia  instituto de quimica       calculo 3a                              35t23    2023_1
samambaia  arquitetura                calculo 1c                              35t45    2023_1
samambaia  engenharia de alimentos    edo                                     35t23    2023_1
samambaia  instituto de fisica        calculo numerico                        35t34    2023_1
samambaia  biomedicina                calculo 1c                              46t23    2023_1
samambaia  biotecnologia              calculo 1c                              46t45    2023_1
samambaia  agronomia                  calculo 2b                              46t23    2023_1
samambaia  agronomia                  calculo 2b                              46t45    2023_1
samambaia  ciencias ambientais        calculo 1c                              46t23    2023_1
samambaia  engenharia de software     calculo 1a                              246n23   2023_1
samambaia  sistemas de informacao     calculo 1a                              246n45   2023_1
samambaia  instituto de fisica        calculo 2a                              246n23   2023_1
samambaia  ciencias economicas        algebra linear                          24n45    2023_1
samambaia  administracao              calculo 2b                              35n23    2023_1
samambaia  instituto de quimica       calculo 1b                              35n45    2023_1
samambaia  instituto de fisica        geometria analitica                     35n45    2023_1
samambaia  ciencias economicas        calculo 1b                              35n23    2023_1
samambaia  administracao              calculo 1b                              35n45    2023_1
samambaia  administracao              estatistica descritiva e probabilidade  46n23    2023_1
samambaia  ciencias contabeis         estatistica                             46n45    2023_1
samambaia  administracao              estatistica inferencial                 46n45    2023_1
aparecida  engenharia de materiais    calculo 1a                              246m23   2023_2
aparecida  geologia                   calculo 1a                              246m45   2023_2
aparecida  engenharia de producao     inferencia                              24m23    2023_2
aparecida  engenharia de materiais    probabilidade e estatistica a           24m45    2023_2
aparecida  engenharia de producao     algebra linear                          24m45    2023_2
aparecida  engenharia de producao     calculo 2a                              246t12   2023_2
aparecida  engenharia de transportes  calculo 2a                              246t34   2023_2
aparecida  engenharia de transportes  calculo numerico                        24m45    2023_2
aparecida  engenharia de producao     calculo numerico                        24t12    2023_2
colemar    engenharia eletrica        calculo 1a                              246m12   2023_2
colemar    engenharia de computacao   calculo 1a                              246m34   2023_2
colemar    engenharia civil           edo                                     24m12    2023_2
colemar    engenharia eletrica        edo                                     24m34    2023_2
colemar    engenharia eletrica        calculo 3a                              24m12    2023_2
colemar    engenharia de computacao   calculo 3a                              24m34    2023_2
colemar    engenharia civil           calculo 2a                              246m12   2023_2
colemar    engenharia civil           algebra linear                          24m34    2023_2
colemar    engenharia de computacao   matematica discreta                     24m12    2023_2
colemar    engenharia de computacao   calculo numerico                        35m12    2023_2
colemar    engenharia eletrica        calculo numerico                        35m34    2023_2
colemar    engenharia eletrica        geometria analitica                     35m12    2023_2
colemar    engenharia eletrica        calculo 2a                              246t12   2023_2
colemar    engenharia civil           geometria analitica                     46t34    2023_2
colemar    engenharia ambiental       calculo 2a                              246t34   2023_2
colemar    engenharia civil           calculo 1a                              246t12   2023_2
colemar    engenharia ambiental       calculo 1a                              246t34   2023_2
colemar    engenharia ambiental       algebra linear                          24t12    2023_2
colemar    engenharia de computacao   calculo 2a                              246t34   2023_2
colemar    engenharia eletrica        probabilidade e estatistica a           46t34    2023_2
colemar    farmacia                   bioestatistica                          46t23    2023_2
colemar    nutricao                   bioestatistica                          46t45    2023_2
colemar    medicina                   bioestatistica 2                        4t12     2023_2
colemar    fisioterapia               bioestatistica                          46t45    2023_2
colemar    medicina                   bioestatistica 2                        6t12     2023_2
colemar    engenharia eletrica        algebra linear                          35t12    2023_2
colemar    engenharia de computacao   algebra linear                          35t34    2023_2
colemar    engenharia civil           calculo numerico                        35t12    2023_2
colemar    biotecnologia              bioestatistica                          35t45    2023_2
colemar    psicologia                 estatistica 2                           24n23    2023_2
colemar    engenharia de computacao   probabilidade e estatistica a           24n45    2023_2
samambaia  instituto de quimica       calculo 1a                              246m23   2023_2
samambaia  inteligencia artificial    calculo 1a                              246m45   2023_2
samambaia  instituto de quimica       calculo 2a                              246m23   2023_2
samambaia  ciencia da computacao      calculo 2a                              246m45   2023_2
samambaia  engenharia de alimentos    calculo 2a                              246m23   2023_2
samambaia  ciencia da computacao      calculo 1a                              246m45   2023_2
samambaia  engenharia de computacao   edo                                     24m56    2023_2
samambaia  engenharia civil           probabilidade e estatistica a           46m56    2023_2
samambaia  engenharia civil           calculo 3a                              24t56    2023_2
samambaia  gestao da informacao       estatistica 1                           246m23   2023_2
samambaia  ciencias economicas        probabilidade e estatistica b           46m45    2023_2
samambaia  instituto de quimica       calculo 1b                              24m23    2023_2
samambaia  instituto de fisica        calculo 1a                              246m45   2023_2
samambaia  instituto de quimica       calculo 2b                              24m23    2023_2
samambaia  ciencia da computacao      algebra linear                          24m45    2023_2
samambaia  instituto de quimica       edo                                     24m23    2023_2
samambaia  ciencia da computacao      edo                                     24m45    2023_2
samambaia  ciencia da computacao      probabilidade e estatistica a           24m23    2023_2
samambaia  ciencia da computacao      calculo numerico                        24m45    2023_2
samambaia  ciencias contabeis         calculo 1c                              35m23    2023_2
samambaia  engenharia de alimentos    algebra linear                          35m23    2023_2
samambaia  instituto de quimica       estatistica                             35m23    2023_2
samambaia  engenharia de materiais    edo                                     35m45    2023_2
samambaia  gestao da informacao       introducao a probabilidade              35m23    2023_2
samambaia  ciencias economicas        calculo 2b                              46m23    2023_2
samambaia  farmacia                   calculo 1c                              46m45    2023_2
samambaia  ciencia da computacao      geometria analitica                     46m23    2023_2
samambaia  instituto de quimica       algebra linear                          46m45    2023_2
samambaia  ciencias contabeis         nocoes de atuaria                       6m23     2023_2
samambaia  engenharia mecanica        probabilidade e estatistica a           24t12    2023_2
samambaia  matematica                 probabilidade                           246t34   2023_2
samambaia  engenharia florestal       calculo 2b                              24t23    2023_2
samambaia  inteligencia artificial    algebra linear                          24t23    2023_2
samambaia  engenharia mecanica        calculo 2a                              246t34   2023_2
samambaia  matematica                 calculo integral                        246t34   2023_2
samambaia  matematica                 geometria diferencial                   246t34   2023_2
samambaia  matematica                 calculo diferencial                     246t34   2023_2
samambaia  matematica                 analise real 2                          24t34    2023_2
samambaia  matematica                 fundamentos de analise                  246t34   2023_2
samambaia  agronomia                  calculo 1b                              25t23    2023_2
samambaia  agronomia                  calculo 1b                              25t45    2023_2
samambaia  engenharia de materiais    algebra linear                          35t12    2023_2
samambaia  instituto de fisica        algebra linear                          35t34    2023_2
samambaia  geologia                   algebra linear                          35t12    2023_2
samambaia  engenharia de materiais    geometria analitica                     35t12    2023_2
samambaia  engenharia mecanica        algebra linear                          35t34    2023_2
samambaia  matematica                 teoria de grupos                        35t34    2023_2
samambaia  matematica                 matematica financeira                   35t34    2023_2
samambaia  engenharia mecanica        calculo numerico                        35t12    2023_2
samambaia  instituto de quimica       calculo 3a                              35t45    2023_2
samambaia  matematica                 estatistica 1                           35t34    2023_2
samambaia  matematica                 introducao a analise no rn              35t34    2023_2
samambaia  engenharia de alimentos    calculo numerico                        36t23    2023_2
samambaia  agronomia                  calculo 2b                              46t23    2023_2
samambaia  agronomia                  calculo 2b                              46t45    2023_2
samambaia  instituto de fisica        calculo 1a                              246n23   2023_2
samambaia  matematica                 calculo integral                        246n45   2023_2
samambaia  matematica                 algebra linear 1                        246n23   2023_2
samambaia  matematica                 fundamentos de analise                  246n45   2023_2
samambaia  matematica                 calculo diferencial                     246n23   2023_2
samambaia  sistemas de informacao     algebra linear                          24n23    2023_2
samambaia  engenharia de software     algebra linear                          24n45    2023_2
samambaia  engenharia de software     probabilidade e estatistica a           24n23    2023_2
samambaia  sistemas de informacao     probabilidade e estatistica a           24n45    2023_2
samambaia  administracao              calculo 2b                              35n23    2023_2
samambaia  instituto de quimica       calculo 2b                              35n45    2023_2
samambaia  matematica                 geometria espacial                      35n23    2023_2
samambaia  matematica                 matematica financeira                   35n45    2023_2
samambaia  ciencias contabeis         calculo 1c                              35n23    2023_2
samambaia  administracao              calculo 1b                              35n45    2023_2
samambaia  instituto de fisica        calculo 3a                              35n23    2023_2
samambaia  instituto de fisica        edo                                     35n45    2023_2
samambaia  matematica                 estatistica 1                           35n45    2023_2
samambaia  ciencias economicas        calculo 2b                              46n23    2023_2
samambaia  ciencias economicas        probabilidade e estatistica b           46n45    2023_2
samambaia  administracao              estatistica descritiva e probabilidade  46n23    2023_2
samambaia  administracao              estatistica inferencial                 46n45    2023_2
samambaia  matematica                 equacoes diferenciais parciais          246t56   2023_2
samambaia  matematica                 algebra linear 1                        246t56   2023_2
samambaia  instituto de fisica        calculo 2a                              246t56   2023_2
samambaia  estatistica                geometria analitica                     46t56    2023_2
samambaia  matematica                 calculo vetorial                        24t56    2023_2
samambaia  matematica                 algebra linear 2                        24t56    2023_2
samambaia  matematica                 geometria espacial                      35t56    2023_2
samambaia  ciencias contabeis         nocoes de atuaria                       6n23     2023_2
aparecida  engenharia de materiais    calculo 1a                              246t12   2024_1
aparecida  engenharia de materiais    calculo 1a                              246t34   2024_1
aparecida  engenharia de transportes  geometria analitica                     24m23    2024_1
aparecida  engenharia de producao     geometria analitica                     24m45    2024_1
aparecida  engenharia de materiais    calculo 3a                              24m45    2024_1
aparecida  engenharia de transportes  calculo 3b                              24t12    2024_1
aparecida  engenharia de transportes  probabilidade e estatistica a           24m23    2024_1
aparecida  engenharia de materiais    probabilidade e estatistica a           24m45    2024_1
colemar    engenharia eletrica        calculo 1a                              246m12   2024_1
colemar    engenharia de computacao   calculo 1a                              246m34   2024_1
colemar    engenharia civil           calculo 2a                              246m12   2024_1
colemar    engenharia civil           algebra linear                          24m34    2024_1
colemar    engenharia de computacao   edo                                     24m56    2024_1
colemar    engenharia eletrica        calculo 3                               24m12    2024_1
colemar    engenharia de computacao   calculo 3a                              24m34    2024_1
colemar    engenharia civil           edo                                     24m12    2024_1
colemar    engenharia eletrica        edo                                     24m34    2024_1
colemar    engenharia ambiental       edo                                     24m56    2024_1
colemar    engenharia de computacao   probabilidade e estatistica a           46m12    2024_1
colemar    engenharia ambiental       probabilidade e estatistica a           46m34    2024_1
colemar    engenharia civil           probabilidade e estatistica a           46m56    2024_1
colemar    engenharia eletrica        geometria analitica                     35m12    2024_1
colemar    engenharia eletrica        calculo numerico                        35m34    2024_1
colemar    engenharia de computacao   matematica discreta                     35m56    2024_1
colemar    nutricao                   bioestatistica                          6m123    2024_1
colemar    engenharia civil           calculo 1a                              246t12   2024_1
colemar    engenharia ambiental       calculo 1a                              246t34   2024_1
colemar    engenharia civil           calculo 3a                              24t56    2024_1
colemar    engenharia eletrica        calculo 2a                              246t12   2024_1
colemar    engenharia de computacao   calculo 2a                              246t34   2024_1
colemar    engenharia eletrica        algebra linear                          35t12    2024_1
colemar    engenharia civil           calculo numerico                        35t12    2024_1
colemar    engenharia civil           geometria analitica                     46t34    2024_1
colemar    engenharia de computacao   algebra linear                          46t56    2024_1
colemar    engenharia eletrica        probabilidade e estatistica a           46t34    2024_1
colemar    farmacia                   bioestatistica                          46t23    2024_1
colemar    medicina                   bioestatistica 1                        4t12     2024_1
colemar    medicina                   bioestatistica 1                        6t12     2024_1
colemar    psicologia                 estatistica 1                           35n34    2024_1
colemar    engenharia de computacao   calculo numerico                        35n45    2024_1
samambaia  engenharia de alimentos    calculo 1a                              246m23   2024_1
samambaia  ciencia da computacao      edo                                     24m45    2024_1
samambaia  quimica bacharelado        calculo 1a                              246m23   2024_1
samambaia  quimica bacharelado        algebra linear                          46m45    2024_1
samambaia  quimica bacharelado        calculo 2a                              246m23   2024_1
samambaia  ciencia da computacao      calculo 2a                              246m45   2024_1
samambaia  gestao da informacao       estatistica 2                           246m23   2024_1
samambaia  ciencias contabeis         estatistica                             46m45    2024_1
samambaia  engenharia quimica         calculo 1a                              246m23   2024_1
samambaia  ciencia da computacao      calculo numerico                        24m45    2024_1
samambaia  ciencias economicas        algebra linear                          24m23    2024_1
samambaia  ciencia da computacao      algebra linear                          24m45    2024_1
samambaia  engenharia quimica         calculo numerico                        24m23    2024_1
samambaia  relacoes internacionais    probabilidade e estatistica             24m23    2024_1
samambaia  relacoes publicas          introducao a estatistica                24m45    2024_1
samambaia  ciencia da computacao      probabilidade e estatistica a           24m23    2024_1
samambaia  inteligencia artificial    probabilidade e estatistica a           24m45    2024_1
samambaia  engenharia quimica         geometria analitica                     35m23    2024_1
samambaia  ciencia da computacao      geometria analitica                     35m45    2024_1
samambaia  quimica bacharelado        estatistica                             35m23    2024_1
samambaia  engenharia de materiais    geometria analitica                     35m23    2024_1
samambaia  engenharia de alimentos    calculo 3a                              35m23    2024_1
samambaia  engenharia de materiais    calculo numerico                        35m45    2024_1
samambaia  ciencia da computacao      geometria analitica                     46m23    2024_1
samambaia  engenharia de alimentos    geometria analitica                     46m45    2024_1
samambaia  ciencias economicas        calculo 1b                              46m23    2024_1
samambaia  engenharia florestal       calculo 1b                              46m45    2024_1
samambaia  quimica licenciatura       calculo 1b                              46m23    2024_1
samambaia  farmacia                   calculo 1c                              46m45    2024_1
samambaia  quimica licenciatura       calculo 2b                              46m23    2024_1
samambaia  comunicacao social         estatistica                             46m45    2024_1
samambaia  estatistica                calculo diferencial                     246t12   2024_1
samambaia  engenharia mecanica        calculo 1a                              246t34   2024_1
samambaia  instituto de fisica        calculo 1a                              246t56   2024_1
samambaia  matematica                 analise real                            246t34   2024_1
samambaia  zootecnia                  calculo 1c                              24t23    2024_1
samambaia  ciencias biologicas        calculo 1c                              24t45    2024_1
samambaia  instituto de fisica        probabilidade e estatistica a           24t12    2024_1
samambaia  instituto de fisica        edo                                     24t34    2024_1
samambaia  engenharia mecanica        edo                                     24t56    2024_1
samambaia  engenharia mecanica        calculo 3a                              24t34    2024_1
samambaia  instituto de fisica        calculo 3a                              24t56    2024_1
samambaia  agronomia                  calculo 1b                              25t23    2024_1
samambaia  agronomia                  calculo 1b                              25t45    2024_1
samambaia  engenharia mecanica        geometria analitica                     35t12    2024_1
samambaia  instituto de fisica        geometria analitica                     35t34    2024_1
samambaia  engenharia de producao     probabilidade e estatistica a           35t12    2024_1
samambaia  estatistica                algebra linear                          35t34    2024_1
samambaia  instituto de fisica        calculo numerico                        35t34    2024_1
samambaia  engenharia quimica         calculo 3a                              35t23    2024_1
samambaia  arquitetura                calculo 1c                              35t23    2024_1
samambaia  biomedicina                calculo 1c                              35t45    2024_1
samambaia  engenharia de alimentos    edo                                     35t23    2024_1
samambaia  ciencias ambientais        calculo 1c                              46t23    2024_1
samambaia  biotecnologia              calculo 1c                              46t45    2024_1
samambaia  agronomia                  calculo 2b                              46t23    2024_1
samambaia  agronomia                  calculo 2b                              46t45    2024_1
samambaia  engenharia de software     calculo 1a                              246n23   2024_1
samambaia  sistemas de informacao     calculo 1a                              246n45   2024_1
samambaia  instituto de fisica        calculo 2a                              246n23   2024_1
samambaia  ciencias economicas        algebra linear                          24n45    2024_1
samambaia  administracao              calculo 2b                              35n23    2024_1
samambaia  quimica licenciatura       calculo 1b                              35n45    2024_1
samambaia  instituto de fisica        geometria analitica                     35n45    2024_1
samambaia  ciencias economicas        calculo 1b                              35n23    2024_1
samambaia  administracao              calculo 1b                              35n45    2024_1
samambaia  administracao              estatistica descritiva e probabilidade  46n23    2024_1
samambaia  ciencias contabeis         estatistica                             46n45    2024_1
samambaia  administracao              estatistica inferencial                 46n45    2024_1
aparecida  engenharia de materiais    geometria analitica                     24m23    2024_2
aparecida  engenharia de producao     algebra linear                          24m45    2024_2
aparecida  engenharia de materiais    edo                                     24m23    2024_2
aparecida  engenharia de producao     calculo numerico                        24m45    2024_2
aparecida  engenharia de producao     inferencia                              24m23    2024_2
aparecida  engenharia de materiais    probabilidade e estatistica a           24m45    2024_2
aparecida  engenharia de materiais    calculo 1a                              246t12   2024_2
aparecida  geologia                   calculo 1a                              246t34   2024_2
aparecida  engenharia de producao     calculo 2a                              246t12   2024_2
aparecida  engenharia de transportes  calculo 2a                              246t34   2024_2
colemar    engenharia eletrica        calculo 1a                              246m12   2024_2
colemar    engenharia de computacao   calculo 1a                              246m34   2024_2
colemar    engenharia civil           edo                                     24m12    2024_2
colemar    engenharia eletrica        edo                                     24m34    2024_2
colemar    engenharia de computacao   edo                                     24m56    2024_2
colemar    engenharia civil           calculo 2a                              246m12   2024_2
colemar    engenharia civil           algebra linear                          24m34    2024_2
colemar    engenharia eletrica        calculo 3a                              24m12    2024_2
colemar    engenharia de computacao   calculo 3a                              24m34    2024_2
colemar    engenharia de computacao   calculo numerico                        35m12    2024_2
colemar    engenharia eletrica        calculo numerico                        35m34    2024_2
colemar    engenharia de computacao   matematica discreta                     35m56    2024_2
colemar    engenharia eletrica        geometria analitica                     35m12    2024_2
colemar    nutricao                   bioestatistica                          6m123    2024_2
colemar    engenharia civil           probabilidade e estatistica a           46m56    2024_2
colemar    engenharia eletrica        calculo 2a                              246t12   2024_2
colemar    engenharia ambiental       calculo 2a                              246t34   2024_2
colemar    engenharia civil           calculo 3a                              24t56    2024_2
colemar    engenharia civil           calculo 1a                              246t12   2024_2
colemar    engenharia ambiental       calculo 1a                              246t34   2024_2
colemar    engenharia civil           geometria analitica                     46t34    2024_2
colemar    engenharia de computacao   algebra linear                          46t56    2024_2
colemar    engenharia ambiental       algebra linear                          24t12    2024_2
colemar    engenharia de computacao   calculo 2a                              246t34   2024_2
colemar    engenharia eletrica        algebra linear                          35t12    2024_2
colemar    engenharia civil           calculo numerico                        35t12    2024_2
colemar    biotecnologia              bioestatistica                          35t45    2024_2
colemar    farmacia                   bioestatistica                          46t23    2024_2
colemar    fisioterapia               bioestatistica                          46t45    2024_2
colemar    medicina                   bioestatistica 2                        4t12     2024_2
colemar    engenharia eletrica        probabilidade e estatistica a           46t34    2024_2
colemar    medicina                   bioestatistica 2                        6t12     2024_2
colemar    psicologia                 estatistica 2                           24n23    2024_2
colemar    engenharia de computacao   probabilidade e estatistica a           24n45    2024_2
samambaia  quimica bacharelado        calculo 1a                              246m23   2024_2
samambaia  inteligencia artificial    calculo 1a                              246m45   2024_2
samambaia  engenharia quimica         calculo 2a                              246m23   2024_2
samambaia  ciencia da computacao      calculo 2a                              246m45   2024_2
samambaia  engenharia de alimentos    calculo 2a                              246m23   2024_2
samambaia  instituto de quimica       algebra linear                          46m45    2024_2
samambaia  gestao da informacao       estatistica 1                           246m23   2024_2
samambaia  ciencias economicas        probabilidade e estatistica b           46m45    2024_2
samambaia  ciencia da computacao      algebra linear                          24m23    2024_2
samambaia  ciencia da computacao      algebra linear                          24m45    2024_2
samambaia  quimica licenciatura       calculo 1b                              24m23    2024_2
samambaia  ciencia da computacao      calculo numerico                        24m45    2024_2
samambaia  quimica licenciatura       calculo 2b                              24m23    2024_2
samambaia  ciencia da computacao      edo                                     24m45    2024_2
samambaia  engenharia quimica         edo                                     24m23    2024_2
samambaia  ciencia da computacao      probabilidade e estatistica a           24m23    2024_2
samambaia  ciencias contabeis         calculo 1c                              35m23    2024_2
samambaia  engenharia de alimentos    algebra linear                          35m23    2024_2
samambaia  quimica bacharelado        estatistica                             35m23    2024_2
samambaia  engenharia quimica         probabilidade e estatistica a           35m23    2024_2
samambaia  gestao da informacao       introducao a probabilidade              35m23    2024_2
samambaia  ciencias economicas        calculo 2b                              46m23    2024_2
samambaia  farmacia                   calculo 1c                              46m45    2024_2
samambaia  ciencias contabeis         nocoes de atuaria                       6m23     2024_2
samambaia  engenharia mecanica        probabilidade e estatistica a           24t12    2024_2
samambaia  engenharia mecanica        calculo 2a                              246t34   2024_2
samambaia  engenharia fisica          calculo 2a                              246t56   2024_2
samambaia  fisica bacharelado         calculo 1a                              246t34   2024_2
samambaia  fisica bacharelado         calculo 2a                              246t56   2024_2
samambaia  matematica                 fundamentos de analise                  246t34   2024_2
samambaia  estatistica                geometria analitica                     24t56    2024_2
samambaia  inteligencia artificial    algebra linear                          24t23    2024_2
samambaia  engenharia florestal       calculo 2b                              24t23    2024_2
samambaia  ciencia da computacao      geometria analitica                     25t45    2024_2
samambaia  agronomia                  calculo 2b                              46t23    2024_2
samambaia  agronomia                  calculo 2b                              46t45    2024_2
samambaia  agronomia                  calculo 1b                              25t23    2024_2
samambaia  agronomia                  calculo 1b                              25t45    2024_2
samambaia  engenharia de materiais    algebra linear                          35t12    2024_2
samambaia  fisica bacharelado         algebra linear                          35t34    2024_2
samambaia  geologia                   algebra linear                          35t12    2024_2
samambaia  engenharia fisica          algebra linear                          35t34    2024_2
samambaia  engenharia mecanica        calculo numerico                        35t12    2024_2
samambaia  engenharia mecanica        algebra linear                          35t34    2024_2
samambaia  engenharia de alimentos    calculo numerico                        36t23    2024_2
samambaia  quimica bacharelado        calculo 3a                              35t45    2024_2
samambaia  fisica licenciatura        calculo 1a                              246n23   2024_2
samambaia  matematica                 fundamentos de analise                  246n23   2024_2
samambaia  sistemas de informacao     algebra linear                          24n23    2024_2
samambaia  engenharia de software     algebra linear                          24n45    2024_2
samambaia  engenharia de software     probabilidade e estatistica a           24n23    2024_2
samambaia  sistemas de informacao     probabilidade e estatistica a           24n45    2024_2
samambaia  engenharia de software     probabilidade e estatistica             24n23    2024_2
samambaia  administracao              calculo 2b                              35n23    2024_2
samambaia  quimica licenciatura       calculo 2b                              35n45    2024_2
samambaia  ciencias contabeis         calculo 1c                              35n23    2024_2
samambaia  administracao              calculo 1b                              35n45    2024_2
samambaia  fisica licenciatura        calculo 3a                              35n23    2024_2
samambaia  fisica licenciatura        edo                                     35n45    2024_2
samambaia  ciencias economicas        calculo 2b                              46n23    2024_2
samambaia  ciencias economicas        probabilidade e estatistica b           46n45    2024_2
samambaia  administracao              estatistica descritiva e probabilidade  46n23    2024_2
samambaia  administracao              estatistica inferencial                 46n45    2024_2
samambaia  matematica                 educacao matematica inclusiva           5n45     2024_2
samambaia  ciencias contabeis         nocoes de atuaria                       6n23     2024_2
aparecida  engenharia de materiais    geometria analitica                     24m23    2025_1
aparecida  engenharia de materiais    geometria analitica                     24m45    2025_1
aparecida  engenharia de materiais    probabilidade e estatistica a           24m23    2025_1
aparecida  engenharia de materiais    probabilidade e estatistica a           24m45    2025_1
aparecida  engenharia de materiais    calculo 3a                              24m45    2025_1
aparecida  engenharia de producao     calculo 3b                              24t12    2025_1
aparecida  engenharia de materiais    calculo 1a                              246t12   2025_1
aparecida  engenharia de materiais    calculo 1a                              246t34   2025_1
aparecida  engenharia de materiais    calculo 2a                              246t34   2025_1
colemar    engenharia eletrica        calculo 1a                              246m12   2025_1
colemar    engenharia de computacao   calculo 1a                              246m34   2025_1
colemar    engenharia civil           calculo 2a                              246m12   2025_1
colemar    engenharia civil           algebra linear                          24m34    2025_1
colemar    engenharia eletrica        calculo 3                               24m12    2025_1
colemar    engenharia de computacao   calculo 3a                              24m34    2025_1
colemar    engenharia de computacao   edo                                     24m56    2025_1
colemar    engenharia civil           edo                                     24m12    2025_1
colemar    engenharia eletrica        edo                                     24m34    2025_1
colemar    engenharia ambiental       edo                                     24m56    2025_1
colemar    engenharia de computacao   probabilidade e estatistica a           46m12    2025_1
colemar    engenharia ambiental       probabilidade e estatistica a           46m34    2025_1
colemar    engenharia civil           probabilidade e estatistica a           46m56    2025_1
colemar    engenharia eletrica        geometria analitica                     35m12    2025_1
colemar    engenharia eletrica        calculo numerico                        35m34    2025_1
colemar    engenharia de computacao   matematicadiscreta                      35m56    2025_1
colemar    nutricao                   bioestatistica                          6m123    2025_1
colemar    engenharia civil           calculo 1a                              246t12   2025_1
colemar    engenharia ambiental       calculo 1a                              246t34   2025_1
colemar    engenharia civil           calculo 3a                              24t56    2025_1
colemar    engenharia eletrica        calculo 2a                              246t12   2025_1
colemar    engenharia de computacao   calculo 2a                              246t34   2025_1
colemar    engenharia eletrica        algebra linear                          35t12    2025_1
colemar    engenharia civil           calculo numerico                        35t12    2025_1
colemar    engenharia civil           geometria analitica                     46t34    2025_1
colemar    engenharia de computacao   algebra linear                          46t56    2025_1
colemar    engenharia eletrica        probabilidade e estatistica a           46t34    2025_1
colemar    farmacia                   bioestatistica                          46t23    2025_1
colemar    medicina                   bioestatistica 1                        46t12    2025_1
colemar    psicologia                 estatistica aplicada a psicologia       35n23    2025_1
colemar    engenharia de computacao   calculo numerico                        35n45    2025_1
samambaia  engenharia de alimentos    calculo 1a                              246m23   2025_1
samambaia  ciencia da computacao      calculo 1a                              246m45   2025_1
samambaia  quimica bacharelado        calculo 1a                              246m23   2025_1
samambaia  engenharia de alimentos    geometria analitica                     46m45    2025_1
samambaia  instituto de fisica        calculo 1a                              246m23   2025_1
samambaia  instituto de fisica        calculo 1a                              246m45   2025_1
samambaia  engenharia quimica         calculo 1a                              246m23   2025_1
samambaia  instituto de fisica        geometria analitica                     46m45    2025_1
samambaia  quimica bacharelado        calculo 2a                              246m23   2025_1
samambaia  ciencia da computacao      calculo 2a                              246m45   2025_1
samambaia  gestao da informacao       estatistica 2                           246m23   2025_1
samambaia  ciencias contabeis         estatistica                             46m45    2025_1
samambaia  engenharia quimica         edo                                     24m23    2025_1
samambaia  ciencia da computacao      edo                                     24m45    2025_1
samambaia  engenharia quimica         calculo numerico                        24m23    2025_1
samambaia  ciencia da computacao      calculo numerico                        24m45    2025_1
samambaia  ciencias economicas        algebra linear                          24m23    2025_1
samambaia  ciencia da computacao      algebra linear                          24m45    2025_1
samambaia  ciencia da computacao      probabilidade e estatistica a           24m23    2025_1
samambaia  inteligencia artificial    probabilidade e estatistica a           24m45    2025_1
samambaia  relacoes internacionais    probabilidade e estatistica             24m23    2025_1
samambaia  engenharia quimica         geometria analitica                     35m23    2025_1
samambaia  ciencia da computacao      geometria analitica                     35m45    2025_1
samambaia  quimica bacharelado        estatistica                             35m23    2025_1
samambaia  engenharia de materiais    calculo numerico                        35m45    2025_1
samambaia  ciencias economicas        calculo 1b                              46m23    2025_1
samambaia  engenharia florestal       calculo 1b                              46m45    2025_1
samambaia  quimica licenciatura       calculo 1b                              46m23    2025_1
samambaia  farmacia                   calculo 1c                              46m45    2025_1
samambaia  quimica licenciatura       calculo 2b                              46m23    2025_1
samambaia  quimica bacharelado        algebra linear                          46m45    2025_1
samambaia  relacoes publicas          introducao a estatistica                46m23    2025_1
samambaia  comunicacao social         estatistica                             46m45    2025_1
samambaia  engenharia mecanica        calculo 1a                              246t34   2025_1
samambaia  zootecnia                  calculo 1c                              24t23    2025_1
samambaia  ciencias biologicas        calculo 1c                              24t45    2025_1
samambaia  instituto de fisica        probabilidade e estatistica a           24t56    2025_1
samambaia  instituto de fisica        edo                                     24t34    2025_1
samambaia  engenharia mecanica        edo                                     24t56    2025_1
samambaia  instituto de fisica        calculo 3a                              24t12    2025_1
samambaia  engenharia mecanica        calculo 3a                              24t34    2025_1
samambaia  agronomia                  calculo 1b                              25t23    2025_1
samambaia  agronomia                  calculo 1b                              25t45    2025_1
samambaia  engenharia mecanica        geometria analitica                     35t12    2025_1
samambaia  engenharia de materiais    geometria analitica                     35t34    2025_1
samambaia  engenharia quimica         calculo 3a                              35t23    2025_1
samambaia  engenharia de alimentos    calculo 3a                              35t45    2025_1
samambaia  arquitetura                calculo 1c                              35t23    2025_1
samambaia  biomedicina                calculo 1c                              35t45    2025_1
samambaia  engenharia de alimentos    edo                                     35t23    2025_1
samambaia  instituto de fisica        calculo numerico                        35t56    2025_1
samambaia  ciencias ambientais        calculo 1c                              46t23    2025_1
samambaia  biotecnologia              calculo 1c                              46t45    2025_1
samambaia  agronomia                  calculo 2b                              46t23    2025_1
samambaia  agronomia                  calculo 2b                              46t45    2025_1
samambaia  instituto de fisica        calculo 2a                              246n23   2025_1
samambaia  sistemas de informacao     calculo 1a                              246n45   2025_1
samambaia  ciencias economicas        algebra linear                          24n45    2025_1
samambaia  ciencias economicas        calculo 1b                              35n23    2025_1
samambaia  quimica licenciatura       calculo 1b                              35n45    2025_1
samambaia  administracao              calculo 2b                              35n23    2025_1
samambaia  instituto de fisica        geometria analitica                     35n45    2025_1
samambaia  administracao              calculo 1b                              35n45    2025_1
samambaia  administracao              estatistica descritiva e probabilidade  46n23    2025_1
samambaia  ciencias contabeis         estatistica                             46n45    2025_1
samambaia  administracao              estatistica inferencial                 46n45    2025_1
