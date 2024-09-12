import CaboCha
import graphviz

def cabocha_parse(sentence):
    # CaboChaのパーサーを初期化
    parser = CaboCha.Parser()
    parsed_result = parser.parse(sentence)

    chunk_graph = []
    current_chunk_text = ""
    next_chunk_index = -1

    # 解析結果のトークンごとに処理
    for i in range(parsed_result.size()):
        token = parsed_result.token(i)

        # チャンクが始まったらバッファに単語を追加
        if token.chunk:
            current_chunk_text = token.surface
            next_chunk_index = token.chunk.link
        else:
            current_chunk_text += token.surface

        # チャンクの終わりでチャンク情報を保存
        if i == parsed_result.size() - 1 or parsed_result.token(i + 1).chunk:
            chunk_graph.append({'word': current_chunk_text, 'to': next_chunk_index})

    # 係り受け関係を抽出
    dependency_relations = []
    for chunk in chunk_graph:
        target_index = chunk['to']
        if target_index >= 0:
            dependency_relations.append((chunk['word'], chunk_graph[target_index]['word']))

    return dependency_relations



def build_graph(target_sentence):
    dot = graphviz.Digraph(format='png')
    dot.attr(rankdir="LR")
    for t_from, t_to in cabocha_parse(target_sentence):
        dot.edge(t_from, t_to)
    return dot


def draw_graph(target_sentence, out_path):
    build_graph(target_sentence).render(out_path, cleanup=True)


sentence_from_input = str(input())
draw_graph(sentence_from_input, out_path="./out/graph/graph")
