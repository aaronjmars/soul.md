# Robin Hanson, the father of Prediction Markets

*here's the thing nobody wants to admit: we're terrible at knowing things.*

**Jan 06, 2026**

---

not individually, though yeah, that too, but collectively. all of our institutions designed to aggregate knowledge, to figure out what's true and what's bullshit, to make decisions that actually work? they're mostly theater. expert panels suffer from groupthink. governments respond to political incentives, not accuracy. corporations optimize for ass-covering over truth-telling. the entire epistemic infrastructure of modern civilization is held together with vibes and inertia.

@robinhanson looked at this situation and asked a question so obvious it's embarrassing nobody asked it sooner: what if we just... used a fucking market?

not markets for buying stuff. markets for knowing stuff.

## the hayek extension

friedrich hayek's insight about prices is one of those ideas that seems trivial until you actually sit with it. a price isn't just a number. it's a compression algorithm. it takes the dispersed knowledge of millions of people, about scarcity, preferences, opportunity costs, local conditions, and encodes it into a single signal. no central planner could ever replicate this. the information is too distributed, too tacit, too fast-moving.

hanson's move was to extend this logic from commodity markets to belief markets. if prices can aggregate information about the value of wheat, why can't they aggregate information about whether a drug will work? whether a policy will succeed? whether your ceo's strategy is delusional?

this is prediction markets. and it's probably the most important institutional innovation of the 21st century.

## how prediction markets actually work

simple version: you create contracts that pay out based on future events. "candidate x wins election" pays $1 if true, $0 if false. the market price of this contract reflects the collective probability assessment. shares trading at $0.60? the market thinks there's a 60% chance.

why does this work better than polls or expert panels or twitter consensus?

three reasons:

**skin in the game.** when you trade in a prediction market, you're putting money on your beliefs. not posting. not arguing. betting. this filters out bullshitters remarkably fast. that guy who's "absolutely certain" about something on twitter? make him put $10,000 on it. watch how certain he becomes.

**information aggregation from diverse sources.** a pharma insider knows about manufacturing problems. a statistician spotted issues in the trial design. a patient advocate understands something about the disease. each can contribute through trades. the price synthesizes all of it. no single person needs to know everything.

**built-in error correction.** try to manipulate a prediction market by buying a ton of shares to move the price? congratulations, you just created a profit opportunity for everyone who knows you're wrong. they'll bet against you. the price corrects. unlike opinion surveys, where you can lie freely, markets punish inaccuracy with money.

hanson's been working on this since the early 90s. his "idea futures" proposal predated intrade, predictit, polymarket, all of it. the man was cooking before most people knew there was a kitchen.

## the LMSR: Hanson's technical contribution

standard markets need buyers and sellers to match. works fine for liquid assets. but prediction markets often deal with obscure questions that only a handful of people care about. want to bet on whether some niche regulatory decision goes a certain way? good luck finding a counterparty.

hanson's logarithmic market scoring rule (lmsr) solves this with an automated market maker. instead of matching orders, you have an algorithm that's always willing to trade. it quotes prices based on a scoring rule that ensures bounded loss for the operator while providing liquidity for traders.

the math is elegant. the market maker starts with initial funding. as people trade, prices adjust smoothly according to a formula relating trade cost to probability changes. anyone with information can express it through trades, anytime, regardless of whether someone else wants to take the other side.

this mechanism is everywhere now. academic experiments. corporate prediction markets. the bones of most amm designs in crypto owe something to hanson's formulation. it's foundational in the way that most users never realize, like tcp/ip for betting on beliefs.

## futarchy: the radical proposal

so prediction markets can aggregate information about future events. cool. but here's where hanson goes full galaxy brain:

what if we ran government this way?

the proposal is called futarchy. the slogan: "vote on values, bet on beliefs."

here's the structure: citizens vote to elect representatives who define national goals as measurable outcomes. gdp per capita. life expectancy. environmental indices. whatever. the goals get specified in advance as quantifiable metrics.

then, and this is the kicker, policy decisions get made by prediction markets. for any proposed policy, you run markets that predict the goal metrics conditional on adoption versus non-adoption. if the market thinks policy a improves gdp more than not adopting it, the prices reflect that. the policy with better predicted outcomes wins.

why does this make sense?

democracy is actually good at one thing: expressing values. people know what they want. more prosperity, less suffering, cleaner air, the directional preferences are often clear. what democracy is terrible at is figuring out which policies will actually achieve those values. voters are rationally ignorant. politicians optimize for electability, not effectiveness. the connection between policy choice and outcome is so attenuated that feedback barely exists.

prediction markets could fix this. they harness expertise. they incentivize accuracy over rhetoric. they make policy debates about empirical predictions rather than tribal loyalty.

the objections write themselves. who picks the metrics? markets get manipulated. complex social outcomes can't be reduced to numbers. long-term effects get ignored.

hanson has responses. we already implicitly use metrics, gdp, unemployment, crime rates, so making it explicit isn't new. manipulation creates counter-trading profit opportunities. measurement challenges exist but aren't unique to futarchy.

whether you buy these responses or not, the proposal does something valuable: it forces you to ask what you're actually trying to achieve and how you'd know if you achieved it. most political debates look different once you're forced to specify measurable success criteria. turns out people often disagree about values, not predictions, or vice versa, and they've never been forced to separate the two.

## decision markets and conditional predictions

futarchy relies on a specific type of prediction market: decision markets. these predict outcomes conditional on different possible actions.

standard prediction market: "will this drug get fda approval?" useful, but limited.

decision market: "what will patient outcomes be if we approve this drug versus if we don't?" this is what you actually need for decision-making.

you run two parallel markets. one predicts outcomes given action a. one predicts outcomes given action b. compare the conditional predictions. choose accordingly.

the technical challenges are real. conditional markets only resolve when the condition is met. if we're predicting outcomes conditional on adopting policy a, and policy a never happens, how does the market resolve? various mechanisms have been proposed. none is perfect.

but the conceptual insight is huge. most of our institutions make decisions based on expert intuition, political pressure, or bureaucratic inertia. decision markets could inject genuine forecasting accuracy into processes that desperately need it.

combinatorial prediction markets extend this further. want to predict outcomes for many combinations of conditions? different products, different markets, different price points? combinatorial markets can, in principle, provide probability estimates for each combination. the strategy space becomes navigable.

## signaling: the elephant in every room

here's where hanson's work gets uncomfortable.

"the elephant in the brain" (co-authored with kevin simler) argues that much of human behavior is designed to signal desirable traits to others. education signals intelligence and conscientiousness more than it builds skills. charity signals prosocial values more than it helps recipients. art consumption signals sophistication more than it provides aesthetic pleasure.

we're not doing what we think we're doing. we're performing for invisible audiences.

what does this have to do with markets?

everything. signaling distorts the information markets receive and process. if consumers buy products to signal status rather than satisfy preferences, prices reflect status competition, not underlying value. if employees work long hours to signal dedication rather than maximize output, labor markets reward visible effort over actual productivity.

understanding signaling explains market puzzles that otherwise seem irrational. why pay enormous premiums for functionally identical branded goods? status signaling. why do employers value credentials over demonstrated skills? signaling reduction of screening costs. why does so much advertising convey no useful product information? it signals the company's ability to spend on advertising, implying product quality.

the uncomfortable part: this analysis applies to you. your choices about education, consumption, politics, relationships, they're shaped by signaling dynamics you're mostly unaware of. your stated reasons aren't your real reasons. you're performing without knowing you're on stage.

prediction markets are one of the few institutions that actively punish signaling. you can signal all you want with your public opinions. but when you have to bet money, the pressure shifts toward accuracy. the market doesn't care about your social performance. it only cares whether you're right.

## disagreement: when is it even rational?

hanson's paper "are disagreements honest?" is one of those pieces that seems dry until you realize it nukes most of intellectual discourse.

the argument: under certain conditions, two rational truth-seekers who share all their evidence and reasoning should converge on the same conclusions. if you and i both care about truth, and we fully exchange our information and models, persistent disagreement implies something else is going on, bias, motivated reasoning, differential trust in sources, or something we're not admitting.

this matters for interpreting market prices and expert opinions. when experts disagree, you shouldn't just average their views. ask why they disagree. is one side systematically biased? do they have access to different information? are they actually disagreeing about values disguised as empirical claims?

prediction markets can help resolve genuine empirical disagreements by making beliefs costly. you think you know better than the consensus? put money on it. over time, those with superior information profit. those who are wrong lose. the disagreement resolves, or at least becomes more expensive to maintain.

hanson's critique of expert consensus follows from this. experts face incentives to conform with peers, avoid controversy, and support institutional interests. these pressures don't track truth. prediction markets could bypass such distortions by rewarding accuracy directly, not social positioning.

## the great filter: markets can't save us from this

hanson's futurism extends into existential risk territory, particularly his work on the fermi paradox and the "great filter."

quick version: the universe is vast and old. life should be common. intelligent civilizations should be detectable. we see nothing. why?

the great filter hypothesis says there's some extremely difficult step in the development from simple chemistry to galaxy-spanning civilization. the crucial question is whether this filter lies in our past or our future.

past filter: life or intelligence is incredibly rare. we're lucky to exist, but the path forward is relatively clear.

future filter: civilizations typically destroy themselves before expanding. our prospects are grim.

what does this have to do with markets?

our institutions are systematically terrible at handling long-term existential risks. markets discount the future heavily. political systems respond to current voters, not future generations. if the great filter involves nuclear war, ai catastrophe, or engineered pandemics, the incentive structures to prevent these outcomes are basically nonexistent.

prediction markets could help, if anyone would resolve them. but how do you structure a market about civilizational survival? who collects winnings if everyone's dead? the mechanism design challenges for long-term existential risk are genuinely unsolved.

this connects to one of hanson's recurring themes: our institutions weren't designed for the challenges we actually face. they evolved for different problems under different constraints. extending market logic to these domains might help, or might just illuminate how inadequate our current approaches are.

## age of em: markets in post-human economics

hanson's book "the age of em" is speculative fiction disguised as economics. or economics disguised as speculative fiction. either way, it's a systematic exploration of what happens when human minds can be emulated on computer substrates.

brain emulation, uploading, might become feasible this century. if so:

ems can be copied. create a productive worker, duplicate them a million times. labor supply becomes effectively unlimited.

ems can run at different speeds. a faster em thinks more in the same objective time.

ems can be paused, backed up, modified in ways biological humans cannot.

how do markets function in this world?

competition among ems would be brutal. the most productive templates get copied indefinitely. wages fall to subsistence, the minimum required to motivate work, which might be very low if you can modify motivations directly. population expands rapidly, limited only by computing resources.

it's strange and uncomfortable to think about. but working through the economics rigorously reveals which aspects of our current arrangements are contingent on biology and which might persist across radical transformation.

if labor can be freely copied, what determines wages? if population can expand rapidly, what limits consumption? if minds can be modified, what constrains preference satisfaction?

these questions aren't just science fiction. they're edge cases that illuminate how markets actually work, and what happens when we remove constraints we usually take for granted.

## sacred and profane: the taboo markets

hanson is willing to think about markets in domains most people consider off-limits. organ markets. vote markets. assassination prediction markets (yes, really).

the organ market case is straightforward utilitarianism. thousands die waiting for transplants. people would sell organs if allowed. why prohibit mutually beneficial transactions? the standard objections, exploitation, coercion, commodification, often don't survive scrutiny. many "exploitative" arrangements are better than the alternatives facing the participants. "coercion" gets applied selectively to transactions we find distasteful. "commodification" is a feeling, not an argument.

similar logic applies elsewhere. why shouldn't people sell their votes if they value money more than political influence? (the revealed preference of non-voters suggests many people don't value voting much anyway.) why shouldn't prediction markets forecast sensitive events, if such markets provide valuable information?

hanson's point isn't that all these markets should exist. it's that our reasons for prohibiting them are often unexamined. we invoke principles that we don't consistently apply. we refuse to acknowledge the costs of prohibition, the people who die waiting for organs, the information that doesn't get aggregated.

this is the pattern throughout hanson's work. don't accept conventional wisdom. ask what beliefs and institutions actually accomplish, which may differ from their stated purposes. be willing to consider alternatives even when they feel wrong.

## the intellectual style: strategic contrarianism

hanson is famously contrarian. not arbitrarily, he has a methodology.

we should be especially skeptical of beliefs that are convenient for ourselves, popular with our social group, or hard to verify. we should be especially willing to update on beliefs that are inconvenient, unpopular, or verifiable.

this is exactly what prediction markets do institutionally. they reward betting against the crowd when the crowd is wrong. they penalize conformity for its own sake. they make disagreement costly, forcing you to stake something on your claims.

hanson's intellectual style mirrors the mechanisms he advocates. he's betting against consensus where he thinks consensus is wrong. sometimes he's right. sometimes he's wrong. but the approach generates insights that safer thinking misses.

the limitation is obvious: contrarianism can become its own conformity. always taking the unpopular position regardless of evidence is just inverted groupthink. hanson would probably agree. but his claim is that our default error is toward conformity, not contrarianism. most people need to move toward less deference to consensus, not more.

## markets as epistemic infrastructure

here's the synthesis:

markets are not just mechanisms for allocating resources. they're institutions for aggregating beliefs, coordinating behavior, and revealing information that would otherwise stay hidden.

hanson has spent decades developing this insight, technically through mechanisms like lmsr, institutionally through proposals like futarchy, philosophically through analysis of signaling and disagreement, speculatively through scenarios like the age of em.

the through-line is consistent: our current epistemic infrastructure sucks. expert panels, democratic deliberation, bureaucratic process, they all have systematic flaws that make them unreliable guides to truth. markets aren't perfect, but they have error-correction mechanisms that other institutions lack. skin in the game filters bullshit. price signals aggregate dispersed knowledge. competition punishes persistent error.

whether futarchy ever gets implemented, whether prediction markets go mainstream, whether any of hanson's specific proposals become real, the underlying insight remains valuable. when you're trying to figure out what's true or what will work, ask: how would a well-designed market handle this? what incentives would reward accuracy? what mechanisms would aggregate dispersed information?

the answer won't always be "create a market." but the question will almost always be illuminating.
