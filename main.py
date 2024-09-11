import CaboCha
import graphviz

def cabocha_parse(received_sentence):
    cabocha_parser = CaboCha.Parser()
    parsed_res =  cabocha_parser.parse(received_sentence)
    ch_graph = []
    buf = ""
    next_i = -1
    for i in range(parsed_res.size()):
        t = parsed_res.token(i)
        buf = t.surface if t.chunk else (buf + t.surface)
        next_i = t.chunk.link if t.chunk else next_i
        if i == parsed_res.size() - 1 or parsed_res.token(i + 1).chunk:
            ch_graph.append({'word': buf, 'to': next_i})

    results = []
    for ch in ch_graph:
        next_id = ch['to']
        if next_id >= 0:
            results.append((ch['word'], ch_graph[next_id]['word']))
    return results


def build_graph(target_sentence):
    dot = graphviz.Digraph(format='png')
    dot.attr(rankdir="LR")
    for t_from, t_to in cabocha_parse(target_sentence):
        dot.edge(t_from, t_to)
    return dot


def draw_graph(target_sentence, out_path):
    build_graph(target_sentence).render(out_path, cleanup=True)


sentence = str(input())
draw_graph(sentence, out_path="./out/graph/graph")
