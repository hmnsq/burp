%{
/* bengali h2c.uhin: generated from the bengali lexicon by lang/hindawi/tools/complete_cells.py,
   in the form of Chintamani's own transducers. Constructs without a word are in STATUS.tsv. */
%}
%%
\'("\\\'"|.*)*\'                       {printf("%s",yytext);}
\"("\\\""|[^\"^\n]*)*\"                {printf("%s",yytext);}

poorbanir_dhaari_ta              {printf("default");}
poor_nnasa_mkhyaa                 {printf("int");}
_an_tarbhaaga                   {printf("#include");}
na_tubaa_ya_di                   {printf("#elif");}
prakaaralaeekha                   {printf("typedef");}
pra_tij_ynaa                   {printf("assert");}
byak_tiga_ta                   {printf("private");}
_an_ta_hhraeekha                    {printf("inline");}
nirbaachana                    {printf("switch");}
sarbajaneena                    {printf("public");}
surakxi_ta                    {printf("protected");}
kxaee_tra                     {printf("case");}
_dbigu_nna                     {printf("double");}
baa_hyika                     {printf("extern");}
_anya_thaa                      {printf("#else");}
_as_thira                      {printf("volatile");}
kaathaamoa                      {printf("struct");}
_dhrubaka                      {printf("const");}
niban_dha                      {printf("register");}
pra_dhaana                      {printf("main");}
_akxara                       {printf("char");}
_aabhaasee                       {printf("virtual");}
_dashamika                       {printf("float");}
phaa_nakaa                       {printf("NULL");}
bira_ti                       {printf("break");}
muk_ta                       {printf("free");}
shoonya                       {printf("void");}
sa_mkaee_ta                       {printf("signal");}
s_thira                       {printf("static");}
_aakaara                        {printf("sizeof");}
ga_nnanaa                        {printf("enum");}
chaalu                        {printf("continue");}
janya                        {printf("for");}
_toaloa                        {printf("raise");}
phaeera_ta                        {printf("return");}
karoa                         {printf("do");}
yakhana                         {printf("while");}
ya_di                         {printf("#if");}
yaa_oa                         {printf("goto");}
likha                         {printf("write");}
sa_mgha                         {printf("union");}
patha                          {printf("read");}

%%
