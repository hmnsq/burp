%{
/* bengali c2h.uhin: generated from the bengali lexicon by lang/hindawi/tools/complete_cells.py,
   in the form of Chintamani's own transducers. Constructs without a word are in STATUS.tsv. */
%}
%%
\'("\\\'"|.*)*\'                       {printf("%s",yytext);}
\"("\\\""|[^\"^\n]*)*\"                {printf("%s",yytext);}

protected                   {printf("×İÏ³èÖÛÂ");}
\#include                   {printf("¤ÆèÂÏèËÚµ");}
continue                    {printf("¸ÚÑİ");}
register                    {printf("ÆÛÊÆèÅ");}
volatile                    {printf("¤×èÃÛÏ");}
default                     {printf("ÈŞÏèÊÆÛÏèÅÚÏÛÂ");}
private                     {printf("ÊèÍ³èÂÛµÂ");}
typedef                     {printf("ÈèÏ³ÚÏÑá´");}
virtual                     {printf("¥ËÚ×Ü");}
assert                      {printf("ÈèÏÂÛºè¼Ú");}
double                      {printf("ÄèÊÛµİÁ");}
extern                      {printf("ÊÚØèÍÛ³");}
inline                      {printf("¤ÆèÂ£Ïá´");}
public                      {printf("×ÏèÊºÆÜÆ");}
return                      {printf("ÉáÏÂ");}
signal                      {printf("×¢³áÂ");}
sizeof                      {printf("¥³ÚÏ");}
static                      {printf("×èÃÛÏ");}
struct                      {printf("³Ú¾ÚÌå");}
switch                      {printf("ÆÛÏèÊÚ¸Æ");}
\#elif                      {printf("ÆÂİÊÚ_ÍÄÛ");}
\#else                      {printf("¤ÆèÍÃÚ");}
break                       {printf("ÊÛÏÂÛ");}
const                       {printf("ÅèÏİÊ³");}
float                       {printf("ÄÕÌÛ³");}
raise                       {printf("ÂåÑå");}
union                       {printf("×¢¶");}
while                       {printf("Í´Æ");}
write                       {printf("ÑÛ´");}
NULL                        {printf("ÉÚ¡³Ú");}
case                        {printf("³èÖáÂèÏ");}
char                        {printf("¤³èÖÏ");}
else                        {printf("¤ÆèÍÃÚ");}
enum                        {printf("µÁÆÚ");}
free                        {printf("Ìİ³èÂ");}
goto                        {printf("ÍÚ°");}
main                        {printf("ÈèÏÅÚÆ");}
read                        {printf("È¾");}
void                        {printf("ÕŞÆèÍ");}
\#if                        {printf("ÍÄÛ");}
for                         {printf("ºÆèÍ");}
int                         {printf("ÈŞÏèÁ×¢´èÍÚ");}
do                          {printf("³Ïå");}
if                          {printf("ÍÄÛ");}
[A-Za-z__][A-Za-z0-9_]*      {printf("%s",yytext);}
%%
