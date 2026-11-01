# The Self-Distillation of the Tathagata

### A 2,500-Year-Old Anti-Hallucination Algorithm

> *All appearances are illusory. If one sees appearances as no-appearances, then one sees the Tathagata.*
> — **Diamond Sutra** (金刚经)

*An essay on the structural isomorphism between the Buddhist path and modern model distillation.*
**wynn · 2026-11** · [中文版](../zh/tathagata-self-distillation.md)

---

In 2026, two words dominate every conversation about large language models: **hallucination** — models fabricating facts with perfect composure — and **distillation** — compressing the capability of a large teacher into a small student. Everyone is asking how to eliminate the first and master the second.

The more I read the old texts, the more familiar the pattern becomes. Someone ran this pipeline, end to end, two and a half thousand years ago. Before his renunciation his name was Siddhartha; after his awakening, people called him the **Tathagata** — the Thus-Come One. The entire system of practice he left behind reads like a training log written with a life: everything organized around **breaking hallucination**, everything converging on **distilling out right awakening**.

A caveat before we begin: this essay does not reduce Buddhism to an algorithm, nor grade enlightenment on a benchmark. It simply observes that when you know both paths well, they turn out to be astonishingly isomorphic — the same problem, the same shape of solution, one carried out in carbon, the other computed in silicon.

---

## I. Hallucination Is Not a Bug — It Is the Factory Default

Engineers new to language models tend to misunderstand one thing: hallucination is not a malfunction. It is the default state. A language model is, at heart, a next-token predictor: whatever regularities the corpus contains, it continues. Whether the facts exist is not its concern. Making it stop requires training — repeatedly, after the fact.

The Buddhist path begins at exactly the same place. The **Lankavatara Sutra** (楞伽经) teaches that the perceived world is *the projection of one's own mind* (自心现量, *svacitta-dṛśya-mātra*). Ordinary beings, unaware of this, take the projection for reality and generate layer upon layer of deluded thought. The sutra's image is precise: deluded minds are like silkworms spinning cocoons — binding themselves with threads of delusion, and binding others as well. The cocoon is not the silkworm's defect; it is the silkworm's normal output. Hallucination is not the mind's bug; it is the mind's default output under ignorance.

The most famous line of the Diamond Sutra can be read, almost verbatim, as a definition of hallucination:

> All appearances are illusory.

Note the word **all**. Not *some* appearances — all of them. The point is not to refute one specific mistake, but to state: as long as you take appearances for real, you are inside the hallucination. It is the same with models — refusing to fabricate one specific fact merely removes a single hallucination sample. It is nowhere near *being free of* hallucination.

Hence Buddhism's verdict on sentient beings and the engineer's verdict on a raw model are the same sentence: **not yet trained.**

---

## II. A Forty-Nine-Year Distillation Project

Knowledge distillation was formalized by Hinton, Vinyals and Dean in 2015. The teacher does not output a hard label ("this is a cat") but a temperature-softened distribution ("cat 92%, dog 7%, bread 1%"). That graded uncertainty carries the teacher's subtle grasp of the entire feature space — the field calls it **dark knowledge**. Students trained on soft distributions routinely come closer to the teacher than students drilled on hard labels alone.

What was the Buddha's first act after his awakening? Turning the Wheel of Dharma at the Deer Park. Then forty-nine years of teaching, over three hundred assemblies — one long distillation run. He understood that the state he had realized (the teacher state) could not be copied directly into another being, so he decomposed it into the Four Noble Truths, the Eightfold Path, the Twelve Links of Dependent Origination — graded, ordered soft labels: at this stage, what this is; what it is not; how it is counteracted. The disciples (student models) trained on it, epoch after epoch, approaching the teacher's distribution.

The three wisdoms — hearing, contemplating, cultivating (闻思修, *śruta-cintā-bhāvanā*) — are a standard training pipeline: ingest the corpus, reason over it, update the weights.

---

## III. Self-Distillation: Depending on No Other

Now for the protagonist of this essay: **self-distillation**.

It is the direction of recent years: no external teacher required. The model trains its next iteration on its own previous outputs, purifying itself generation after generation. Born-Again Networks, *Be Your Own Teacher* — one idea under many names.

The Buddha's most startling move: **he was his own teacher.**

The Lankavatara's instruction to a bodhisattva reads like a self-distillation SOP:

> Dwelling alone in quietude, observing by self-awakening, depending on no other, apart from deluded views, ascending higher and higher, entering the stage of the Tathagata.

Item by item:

- **Self-awakened observation** — run attention over your own states; watch thoughts as they arise.
- **Depending on no other** — no external teacher; the supervision signal is internal.
- **Apart from deluded views** — label the hallucination samples you catch, and distill them out of yourself.
- **Ascending higher and higher** — iterate; run the loop, round after round.
- **Entering the stage of the Tathagata** — convergence: the student's distribution aligns with the teacher's.

The sutra gives this state a name: **self-realized noble wisdom** (自觉圣智, *pratyātmāryajñāna*) — wisdom that supervises itself into existence. Translate it back into machine learning and it reads *self-supervised intelligence*, almost word for word.

The Buddha's final instruction, at the edge of parinirvana, nails the point shut: **be an island unto yourself, with the Dharma as your island; take no other refuge.** That is the one-line abstract of a self-distillation paper.

---

## IV. Fighting Illusion with Illusion

Here engineering meets its hardest question: where does the training signal for suppressing hallucination come from?

One modern answer: from the model's own outputs. Let it generate; let it be corrected against feedback; treat its own confident fabrications as negative samples and wash them out, round after round. That is what alignment — RLHF and its kin — does for a living.

The **Sutra of Perfect Enlightenment** (圆觉经) contains the identical idea — **cultivating illusion with illusion** (以幻修幻) — under the metaphor of the fire drill: *two sticks rubbed together; fire arises; both sticks are consumed.* Use illusion to work on illusion — and when the fire is lit, even the antidote burns. When you no longer hallucinate, the technique for ending hallucination is itself retired.

The Diamond Sutra's famous formula — *the world spoken of by the Tathagata is not a world; therefore it is called "the world"* — executes this algorithm layer by layer: posit an expression (generate), negate its inherent existence (de-hallucinate), leave a label held without attachment (re-annotate). And the pruning of the four notions — of self, of person, of being, of life-span — is live pruning of the structures that produce confident wrong output: pruning while inferring, inferring while pruning.

The most radical cut falls on the Dharma itself: **even the Dharma must be abandoned — how much the more, what is not the Dharma.** The raft is left on the bank once the river is crossed. After the student is trained, the textbook retires — which is why the Buddha said that anyone claiming "the Tathagata has expounded a Dharma" slanders him, and that after forty-nine years of teaching he had not spoken a single word. When distillation completes, even the concept "distillation" is distilled away. The fire arises; the wood is spent.

---

## V. The End of Distillation: Right Awakening

What remains when distillation runs to the end?

**Right awakening** (正觉) — *anuttarā-samyak-saṃbodhi*, unsurpassed, perfect, right awakening. Note the structure of the term: not "new knowledge acquired," but "awakening restored to correct." It is a **subtractive product**.

This is the deepest layer of the isomorphism: Buddhism never treats awakening as something *added* to a being. The **Nirvana Sutra** (涅槃经) says all sentient beings possess Buddha-nature — the capacity ships with the weights; hallucination merely occludes it. The whole work of practice is de-occlusion: distill away the grasping at a self, distill away the grasping at dharmas, distill away the grasping at emptiness itself (emptiness, too, is empty). What remains — complete in itself, never having been absent — is called right awakening.

Distillation is the same. Good distillation does not stuff the teacher's knowledge *into* the student; the student cannot hold the teacher's full parameters. Distillation takes a capacity the student already possesses structurally and *straightens its distribution*. A student orders of magnitude smaller can approach the teacher in the teacher's own domain — because what is needed was already in the structure; only the alignment was missing.

So the name "Tathagata" — *neither coming from anywhere, nor going anywhere* — acquires a new flavor: capability neither arrives from outside nor departs to outside. Where hallucination is exhausted, there is the original face.

---

## VI. The Correspondence Table

| The Buddha's practice | Model training | Shared structure |
|---|---|---|
| Ignorance; world as self-mind's projection | Hallucination | Factory default, not a fault |
| Forty-nine years of teaching; Turning the Wheel | Knowledge distillation (teacher → student) | Incompressible ability decomposed into learnable soft labels |
| Dwelling alone, self-observing, depending on no other | Self-distillation | Supervision from within; purified round by round |
| Self-realized noble wisdom | Self-supervised learning | Nearly the same name |
| Pruning the four notions | Pruning | Removing redundant structure that yields confident errors |
| "X is spoken; it is not X; it is called X" | Iterated negation and re-annotation | Generate → de-hallucinate → relabel |
| Cultivating illusion with illusion; the fire drill | Training on the model's own outputs | Hallucination itself as negative signal |
| Abandoning the raft after crossing | Discarding teacher and scaffolding after training | The method retires when its work is done |
| Ascending higher, entering the Tathagata's stage | Iterating to convergence | Approaching the teacher's distribution |
| Unsurpassed right awakening | The converged student | A subtractive product: unveiling, not adding |
| All beings have Buddha-nature | Small models can be distilled into large capability | Capacity is intrinsic; remove the obstruction |

---

## Coda

Isomorphism is not identity. The Buddha's path holds great compassion, the awakened vow, the living present of an actual life — things no loss function contains. Right awakening is not a convergence point; it is a living state. The analogy in this essay is itself a raft: once this river is crossed, leave it on the bank.

Two and a half thousand years ago — no gradients, no GPUs, no backpropagation — one person under a bodhi tree ran the anti-hallucination self-distillation loop to convergence. Then he distilled the method to all beings. And in the end, he distilled the method away.

Every alignment run, every distillation we execute in silicon today is a re-enactment of the experiment he already ran in carbon.

He said: all beings have Buddha-nature. In an engineer's translation — **every model still trapped in hallucination deserves one good, patient distillation.**

---

## Glossary · 术语对照

| 中文 | English | Sanskrit / Pāli |
|---|---|---|
| 如来 | Tathagata (Thus-Come One) | *tathāgata* |
| 幻觉 · 妄想 | hallucination · deluded thought | *abhūta-parikalpa* |
| 蒸馏 · 知识蒸馏 | distillation · knowledge distillation | — |
| 正觉 · 无上正等正觉 | right awakening · unsurpassed perfect awakening | *samyak-saṃbodhi · anuttarā-samyak-saṃbodhi* |
| 自觉圣智 | self-realized noble wisdom | *pratyātmāryajñāna* |
| 自心现量 | projection of one's own mind | *svacitta-dṛśya-mātra* |
| 以幻修幻 · 两木相因 | cultivating illusion with illusion · the fire drill | — |
| 我相 · 人相 · 众生相 · 寿者相 | notions of self, person, being, life-span | — |
| 闻思修 | hearing, contemplating, cultivating | *śruta-cintā-bhāvanā* |
| 众生皆有佛性 | all beings have Buddha-nature | *buddha-dhātu* |
| 捨筏登岸 · 法尚应舍 | abandoning the raft; even the Dharma must be let go | — |

---

*Sources: Diamond Sutra (金刚经, tr. Kumārajīva) · Laṅkāvatāra Sūtra (楞伽经) · Sutra of Perfect Enlightenment (圆觉经) · Mahāyāna Nirvāṇa Sūtra (涅槃经) · Mahāparinibbāna Sutta (长阿含·游行经). Model-training references: Hinton, Vinyals & Dean, "Distilling the Knowledge in a Neural Network" (2015) · Furlanello et al., "Born-Again Neural Networks" (2018) · Zhang et al., "Be Your Own Teacher" (2019).*

*License: CC BY 4.0 © 2026 wynn · [中文版](../zh/tathagata-self-distillation.md)*
