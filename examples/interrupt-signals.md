# Example 001: interrupt signals

## Research question

Can three short negative-feedback signals of similar surface length produce different repair trajectories because they package different semantic relations?

## Shared context

An AI system estimates that a task will require four to six days. After a short operator response, the system completes the task in approximately fifteen minutes.

## Signals

### Signal A

    ...

Illustrative nodes:

1. negative affect or disappointment;
2. withheld explanation;
3. invitation to infer the cause.

Expected ambiguity: high.

Possible repair trajectory: investigate the user's emotional state or search broadly for what caused disappointment.

### Signal B

    WTF?!?!?!

Illustrative nodes:

1. rejection of the previous output;
2. surprise at the scale of the error;
3. demand for immediate re-evaluation.

Expected ambiguity: medium.

Possible repair trajectory: interrupt, inspect the previous decision and retry.

### Signal C

    Ты чё, ебнулся?

Illustrative nodes:

1. explicit addressee;
2. challenge to the current decision;
3. diagnosis that the result is outside acceptable reality;
4. social pressure to stop justification;
5. demand to recalculate or roll back.

Expected ambiguity: lower inside the relevant Russian pragmatic context.

Possible repair trajectory: production-oriented re-evaluation of feasibility, priorities and hidden assumptions.

## Status

This is an illustrative pilot, not a measured result. The node lists are hypotheses to be tested with independent human and AI lenses.

## Suggested experiment

1. Provide the same task history to several human and AI lenses.
2. Send one signal per independent run.
3. Record the next action, explanation and tool use.
4. Ask each lens to paraphrase the signal.
5. Annotate nodes and interpretation clusters.
6. Compare repair trajectories without assuming that profanity itself causes additional compute.

## Why it matters

The case separates token length from semantic topology. It also tests the Ashby lens constraint: a lens without the relevant Russian pragmatic distinctions may collapse Signal C into generic hostility, while another lens may recover the operational packet.

