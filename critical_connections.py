from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        # Construir a lista de adjacências
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        # Inicializar arrays de descoberta, menor tempo e visitados
        disc = [-1] * n
        low = [-1] * n
        visited = [False] * n
        time = [0]  # Lista para simular uma variável de tempo mutável
        bridges = []  # Lista para armazenar as pontes
        
        def dfs(u, parent):
            # Marcar o vértice como visitado e definir tempos iniciais
            visited[u] = True
            disc[u] = time[0]
            low[u] = time[0]
            time[0] += 1
            
            # Explorar todos os vizinhos
            for v in adj[u]:
                if v == parent:  # Ignorar o pai
                    continue
                if not visited[v]:  # Vizinho não visitado, continuar DFS
                    dfs(v, u)
                    low[u] = min(low[u], low[v])  # Atualizar low[u] com o menor low[v]
                    if low[v] > disc[u]:  # Verificar se é uma ponte
                        bridges.append([u, v])
                else:  # Vizinho já visitado, atualizar low[u] com disc[v]
                    low[u] = min(low[u], disc[v])
        
        # Chamar DFS para cada vértice não visitado (embora o grafo seja conectado)
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)
        
        return bridges