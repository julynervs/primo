#!/usr/bin/env python
# coding: utf-8

# ## Sistemas Lineares

# ### <font color='red'> 1.  #Relembrando </font> (2 incógnitas) 
# 
# <font color='blue'>Exemplo 1.1</font>
# 
# $$
# \left\{
#     \begin{array}\\
#        x + y = 4 \\
#        2x - 3y = 3
#         {}
#     \end{array}
# \right.
# $$
# 
# Solução 1: Adição
# 
# $$
# \left\{
#     \begin{array}\\
#        -2x - 2y = -8 \\
#        2x - 3y = 3
#         {}
#     \end{array}
# \right.
# $$
# 
# $$ 0x - 5y = -5   \Longrightarrow y = 1 $$
# 
# $$ x + 1 = 4  \Longrightarrow x = 3 $$
# 
# Solução 2: Substituição
# 
# $$
# \left\{
#     \begin{array}\\
#        x + y = 4 \\
#        2x - 3y = 3
#         {}
#     \end{array}
# \right.
# $$
# 
# $$ y = 4 - x$$
# 
# $$ 2x - 3(4 - x) = 3 \\ 2x - 12 + 3x = 3 \\ 5x = 15 \Longrightarrow x = 3 $$
# 
# $$ y = 4 - 3 \Longrightarrow y = 1 $$
# 
# Solução $$ S = {(3 , 1)} $$

# <font color='blue'> Exemplo 1.2 </font>
# 
# $$
# \left\{
#     \begin{array}\\
#        x - 2y = -1 \\
#        - 2x + 4y = 2
#         {}
#     \end{array}
# \right.
# $$
# 
# Por Adição:
# 
# $$
# \left\{
#     \begin{array}\\
#        2x - 4y = 2 \\
#        - 2x + 4y = 2
#         {}
#     \end{array}
# \right .
# $$
# 
# $$ 0x + 0y = 0 \\ 0 = 0 $$
# 
# É verdade, mas <b>não</b> resolve! <br>
# O sistema admite infinitas soluções.
# 
# $$ S = \left\{
#     \begin{array}\\
#     {{(1,1);(-1,0);(7,4); ... }}
#     {}
#     \end{array}
#     \right\} $$
#     
# <font color='blue'> Exemplo 1.3 </font>
#  
# $$
# \left\{
#     \begin{array}\\
#        x + y = 5 \\
#        x + y = 8
#         {}
#     \end{array}
# \right.
# $$
# 
# Por Adição:
# 
# $$
# \left\{
#     \begin{array}\\
#        -x -y = -5 \\
#        x + y = 8
#         {}
#     \end{array}
# \right .
# $$
# 
# $$ 0x + 0y = 3 \\ 0 = 3 $$
# 
# Não é verdade! <br> O sistema <font color='red'>NÃO</font> admite soluções.
# 
# $$ S = 
#     \left\{
#         \begin{array}\\ 
#         \end{array}
#     \right\} $$

# ### <font color='red'> 2. Classificação de Sistemas </font>
# #### <font color='red'> 2.1 Sistema Possível e Determinado (SPD) </font>
# $$ \Longrightarrow \mbox{Admite uma ÚNICA solução como em Exemplo 1.1} $$
# #### <font color='red'> 2.2 Sistema Possível e Indeterminado (SPI) </font>
# $$ \Longrightarrow \mbox{Admite INFINITAS soluções como em Exemplo 1.2} $$
# #### <font color='red'> 2.3 Sistema Impossível (SI) </font>
# $$ \Longrightarrow \mbox{NÃO admite solução como em Exemplo 1.3} $$

# ###  <font color='red'> 3. Regra de Cramer </font>
# 
# Dado o sistema
# 
# $$
# \left\{
#     \begin{array}\\
#        ax + by = k \\
#        cx + dy = n
#         {}
#     \end{array}
# \right.
# $$
# 
# Definimos os determinantes:
# 
# $$ D =
# \begin{vmatrix} a & b \\ c & d \end{vmatrix}
# $$
# 
# 
# $$ D_x =
# \begin{vmatrix} k & b \\ n & d \end{vmatrix}
# $$
# 
# $$ D_y =
# \begin{vmatrix} a & k \\ c & n \end{vmatrix}
# $$
# 
# De modo que:
# $$ x = \frac{D_x}{D} $$
# 
# $$ y = \frac{D_y}{D} $$
#  
# <font color='blue'> Exemplo 1.1 </font>
# 
# $$
# \left\{
#     \begin{array}\\
#        x + y = 4 \\
#        2x - 3y = 3
#         {}
#     \end{array}
# \right.
# $$
# 
# Solução Cramer:
# 
# $$ D =
# \begin{vmatrix} 1 & 1 \\ 2 & -3 \end{vmatrix} = - 3  - 2 = - 5
# $$
# 
# 
# $$ D_x =
# \begin{vmatrix} 4 & 1 \\ 3 & -3 \end{vmatrix} = - 12 - 3 = - 15
# $$
# 
# 
# $$ D_y =
# \begin{vmatrix} 1 & 4 \\ 2 & 3 \end{vmatrix} = 3 - 8 = - 5 
# $$
# 
# Então:
# 
# $$ x = \frac{D_x}{D} = \frac{-15}{-5} = 3 $$
# 
# 
# $$ y = \frac{D_y}{D} = \frac{-5}{-5} = 1 $$
# 
# <font color='blue'> Exemplo 1.2 </font>
# 
# $$
# \left\{
#     \begin{array}\\
#        x - 2y = -1 \\
#        - 2x + 4y = 2
#         {}
#     \end{array}
# \right.
# $$
# 
# Solução Cramer:
# 
# $$ D =
# \begin{vmatrix} 1 & - 2 \\ - 2 & 4 \end{vmatrix} = 4 - 4 = 0
# $$
# 
# 
# $$ D_x =
# \begin{vmatrix} - 1 & -2 \\ 2 & 4 \end{vmatrix} = -4 + 4 = 0
# $$
# 
# 
# $$ D_y =
# \begin{vmatrix} 1 & - 1 \\ -2 & 2 \end{vmatrix} = 2 - 2 = 0 
# $$
# 
# Então:
# 
# $$ x = \frac{D_x}{D} = \frac{0}{0} \Longrightarrow \mbox{Indeterminação} $$
# 
# 
# $$ y = \frac{D_y}{D} = \frac{0}{0} \Longrightarrow \mbox{Indeterminação} $$
# 
# Quando todos os determinantes são iguais a zero, temos um Sistema Possível e Indeterminado (SPI).
# 
# 
# <font color='blue'> Exemplo 1.3 </font>
# 
# $$
# \left\{
#     \begin{array}\\
#        x + y = 5 \\
#        x + y = 8
#         {}
#     \end{array}
# \right.
# $$
# 
# Solução Cramer:
# 
# $$ D =
# \begin{vmatrix} 1 & 1 \\ 1 & 1 \end{vmatrix} = 1 - 1 = 0
# $$
# 
# 
# $$ D_x =
# \begin{vmatrix} 5 & 1 \\ 8 & 1 \end{vmatrix} = 5 - 8 = - 3
# $$
# 
# 
# $$ D_y =
# \begin{vmatrix} 1 & 5 \\ 1 & 8 \end{vmatrix} = 8 - 5 = 3 
# $$
# 
# Então:
# 
# $$ x = \frac{D_x}{D} = \frac{-3}{0} \Longrightarrow \mbox{Impossível} $$
# 
# 
# $$ y = \frac{D_y}{D} = \frac{3}{0} \Longrightarrow \mbox{Impossível} $$
# 
# Quando o Determinante D é igual a zero e pelo menos um dos outros determinantes é diferente de zero, temos um Sistema Impossível (SI).
# 
# ####  <font color='red'> 3.1 Classificação de Sistemas por Cramer </font>
# 
# $$ D \neq 0 \Longrightarrow \mbox{SPD} $$
# 
# $$ D = 0 \mbox{  e  } D_x = 0 \mbox{  e  } D_y = 0 \mbox{  e  } D_z = 0 \mbox{  e  ...   e  } D_n = 0 \Longrightarrow \mbox{SPI} $$
# 
# 
# $$ D = 0 \mbox{  e  } D_x \neq 0 \mbox{  e/ou  } D_y \neq 0 \mbox{  e/ou  } D_z \neq 0 \mbox{  e/ou  ...   e/ou  } D_n \neq 0 \Longrightarrow \mbox{SI} $$
# 
# 
# <font color='blue'> Exemplo 3.1 </font> Classifique e, se possível, resolva o sistema a seguir:
# 
# $$
# \left\{
#     \begin{array}\\
#        x + y + z = 3 \\
#        x - y + z = 1 \\
#        2x -y - z = 0
#         {}
#     \end{array}
# \right.
# $$
# 
# 

# Solução Cramer:
# 
# $$ D =
# \begin{vmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \\ 2 & -1 & -1 \end{vmatrix}  \begin{matrix}  1 & 1 \\  1 & -1 \\ 2 & -1 \end{matrix}  = 1 + 2 +(-1) - (-2) -(-1) -(-1) = 6
# $$
# 
# 
# 
# $$ D_x =
# \begin{vmatrix} 3 & 1 & 1 \\ 1 & -1 & 1 \\ 0 & -1 & -1 \end{vmatrix} = 6
# $$
# 
# 
# $$ D_y =
# \begin{vmatrix} 1 & 3 & 1 \\ 1 & 1 & 1 \\ 2 & 0 & -1 \end{vmatrix} = 6
# $$
# 
# 
# $$ D_z =
# \begin{vmatrix} 1 & 1 & 3 \\ 1 & -1 & 1 \\ 2 & -1 & 0 \end{vmatrix} =  6
# $$
# 
# 
# Então:
# 
# $$ x = \frac{D_x}{D} = \frac{6}{6} = 1 $$
# 
# 
# $$ y = \frac{D_y}{D} = \frac{6}{6} = 1 $$
# 
# 
# $$ z = \frac{D_z}{D} = \frac{6}{6} = 1 $$
# 
# $ \mbox{O Sistema é Possível e Determinado e apresenta a única solução:} $
# 
# $$ S = \left\{
#     \begin{array}\\
#     {{(1, 1, 1) }}
#     {}
#     \end{array}
#     \right\} $$

# <font color='blue'> Exemplo 3.2 </font> Classifique e, se possível, resolva o sistema a seguir:
# 
# $$
# \left\{
#     \begin{array}\\
#        x + y + z = 6 \\
#        x - 2y + z = 0 \\
#        2x -y + 2z = 6
#         {}
#     \end{array}
# \right.
# $$

# $$ D = 0 $$
# 
# 
# $$ D_x = -24 + 6 + 0 + 12 + 6 = 0 $$
# 
# 
# $$ D_y = 0 $$
# 
# 
# $$ D_z = 0 $$
# 
# $ \mbox{O Sistema é Possível e Indeterminado.} $

# <font color='blue'> Exemplo 3.3 </font> Classifique e, se possível, resolva o sistema a seguir:
# 
# $$
# \left\{
#     \begin{array}\\
#        x + y + z = 6 \\
#        x - 2y + z = 0 \\
#        4x -2y + 4z = 3
#         {}
#     \end{array}
# \right.
# $$

# In[ ]:




