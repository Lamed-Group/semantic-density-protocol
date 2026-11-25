# Semantic Density Protocol v0.1

Status: **experimental pilot specification**

Normative terms such as MUST, SHOULD and MAY are used in their ordinary technical sense.

## 1. Measurement object

The protocol does not assign an observer-independent density to a text. It records an observation:

    O = (construct, lens, context, time)

and computes:

    P_observed(O) = N(O) * E(O) / D(batch)

The unit of comparison is therefore an observation made under declared conditions.

## 2. Core variables

### 2.1 Semantic nodes: N

A semantic node is a proposition, distinction, relation, question, metaphor or operational instruction that can be paraphrased but cannot be removed without losing part of the construct's function.

For each observation:

    N = number of annotated semantic nodes

The annotation MUST preserve the node list, not only the count.

### 2.2 Resonance energy: E

For the pilot:

    E = reflection_seconds / reading_seconds

Reading time MUST be greater than zero. Reflection time is the measured or self-reported time during which the observer continues actively processing the construct after the initial reading.

Estimated times MUST be marked as estimates. Prospective studies SHOULD use measured times.

### 2.3 Interpretive dispersion: D

D is a batch-level property. A cohort of observers is asked to summarize the construct in one sentence without seeing other answers. Responses are clustered by materially distinct interpretation.

Pilot definition:

    D = number of distinct interpretation clusters

An answer such as "I cannot determine the meaning" MUST be retained as a valid category. It MUST NOT be replaced with another participant.

Future versions may replace the simple count with normalized entropy or agreement statistics.

### 2.4 Observed density: P_observed

For every observation j in a batch:

    P_observed_j = N_j * E_j / D_batch

P_observed is meaningful only together with the lens, context, node list, timing method, dispersion procedure and protocol version.

## 3. Lens

Every observation MUST identify a lens profile. At minimum:

- lens type: human, language model, hybrid or unknown;
- language;
- relevant domain familiarity;
- prior familiarity with the construct;
- context level;
- annotation mode;
- for AI: model label, date, system or role instructions when available, and context summary.

The lens is not assigned a numeric multiplier in v0.1.

## 4. Context

Context MUST be one of:

- none;
- minimal;
- full;
- trained or calibrated;
- custom, with a description.

The same construct MAY be evaluated under several context levels. Context changes create new observations rather than overwriting earlier ones.

## 5. Ashby constraint

The protocol treats requisite variety as a measurement constraint:

    if V_lens < V_required_by_construct,
    then part of the construct is not distinguishable by that lens.

No numeric value for V_lens or V_construct is required in v0.1. The constraint is represented through lens metadata, missed nodes, non-answers and cross-lens spread.

## 6. Aggregation

A report SHOULD include:

- median P_observed;
- minimum and maximum P_observed;
- interquartile range when the sample permits;
- lens groups;
- node agreement;
- interpretation-cluster count;
- non-answer rate;
- measured versus estimated timing rate.

A single mean score MUST NOT be presented as the intrinsic density of the text.

## 7. Historical records

Calculations made before v0.1 MAY be retained with:

- record_type = historical;
- the original formula inputs;
- the original source URL;
- explicit notes about estimated values and evolving scales.

Historical records MUST NOT be mixed into a calibrated benchmark without re-annotation.

## 8. Non-core dimensions

Longevity, instrumentality, archetypal closure, metaphor strength, autobiographical authenticity, strategic operability and the "GY" coefficient are extensions. They MUST be reported separately from core P_observed in v0.1.

## 9. Prohibited interpretations

P_observed MUST NOT be described as a direct measure of:

- truth;
- factual accuracy;
- moral value;
- intelligence;
- consciousness;
- safety;
- literary quality;
- author importance.

It is an operational indicator of how much semantic structure became distinguishable and resonant under recorded conditions.

