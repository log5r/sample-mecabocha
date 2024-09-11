import CaboCha

sentence = "父が海外出張で手に入れた時計を、祖父が見た目を気に入ったため、私に譲ってくれた。"

cabocha_parser = CaboCha.Parser()
results = cabocha_parser.parse(sentence)

for i in range(results.size()):
    tkn = results.token(i)
    word = tkn.surface
    chunk = tkn.chunk
    print(f"{word=}, {chunk.link if chunk else "None"}")
