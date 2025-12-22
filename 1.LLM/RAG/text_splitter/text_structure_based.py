'''
recursive text spliter
in this method the splitter doesnt try to split on the bases of 
character so it doesnt cut the words form middle 
we as an argumrnt give the chunk size limit as a limit which is caracter limit 
so it tries to split the text on the bases of 
"\n\n" paragrapgh break
if the splits are more than chunk limit than it breaks on the bases of 
"\n" line if than also it is more than limit then it breaks on the beses of 
" " word space and if in this whole prcess after spliting i tries to join splits again 
so if it is in the limit they can be considered as a chunk 
for example if the pwrd split happens with limit equal to 20 and a sentence split to 
4 words of 5-5 charectors than the recursive spliter will will try to join them 
and on chunk will be 3 word plus two spaces so 17 characters and one word of 
five charectors 
and this joining can happen between paragraph line or words or character
chunking can be visualized here "https://chunkviz.up.railway.app/"
'''

text = '''
The morning light filtered through the half-open window, settling gently on the desk where unfinished notes lay scattered. Outside, the city moved at its usual pace, unaware of the small pauses happening indoors. Time felt stretched, not slow, just deliberately unhurried, as if the day itself was waiting for instructions.

Ideas rarely arrive fully formed. More often, they emerge as fragments—half-sentences, vague intuitions, or questions without answers. It is only through repetition and revision that these fragments assemble into something coherent. The process is less about sudden inspiration and more about patience.

The library was quiet, but not silent. Pages turned softly, chairs shifted, and distant footsteps echoed in long corridors. In that subdued atmosphere, concentration felt easier, almost automatic, as though the space itself demanded attention and rewarded it with clarity.

Technology tends to promise efficiency, yet it often introduces new forms of complexity. Tools meant to simplify tasks require learning, maintenance, and adaptation. Still, once mastered, they reshape habits so completely that it becomes difficult to imagine working without them.

Not every decision needs urgency. Some benefit from distance—time enough for initial excitement to fade and for consequences to come into focus. Deliberation, though slower, often leads to outcomes that feel more stable and intentional.'''

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

# print(len(chunks))
print(chunks[0])