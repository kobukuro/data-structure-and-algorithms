graph = node(also called vertex) + edges

- directed graph
  > a→c\
  a可以到c，但是c不能到a
  
  > a→c\
    ↓&nbsp;&nbsp;&nbsp;&nbsp;↓\
    b←e\
  > ↓\
  > d←f\
  > 當我們現在在a時，b和c稱為neighbor nodes(accessible)\
  > 利用程式表達這個圖的話，會用adjacency list
  >```text
  >{
  >   a:[b, c],
  >   b:[d],
  >   c:[e],
  >   d:[],
  >   e:[b],
  >   f:[d]
  >}
  >```
  >這裡的keys為此graph的所有nodes
  - depth first traversal
    - ex. starting at a: **a,b,d**,...
  - breadth first traversal
    - ex. starting at a: **a,b,c**,...

  
- undirected graph
  > a—c\
  a可以到c，c也可以到a