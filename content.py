# -*- coding: utf-8 -*-
"""
All course content lives here. Edit this file, then run `python3 build.py`.

Formatting inside text fields: a tiny subset of Markdown is supported —
  [link text](https://url)   **bold**   *italic*   `code`
Blank lines separate paragraphs in multi-paragraph fields.
"""

# --------------------------------------------------------------------------
# Course identity
# --------------------------------------------------------------------------

COURSE = {
    "number": "TBD",                       # e.g. "IEOR E4650"
    "title": "Anticipating Our AGI Future",
    "tagline": "Growth, forecasting, and the economics of transformative AI.",
    "term": "Fall 2026",
    "institution": "Columbia University",
    # Shown in the browser tab and in link previews.
    "meta_description": (
        "A graduate seminar at Columbia on the future growth and impact of AI, "
        "using tools from economics, finance, statistics, and operations research."
    ),
}

INSTRUCTOR = {
    "name": "Steven Yin",
    "email": "sy2737@columbia.edu",
    "twitter": "https://x.com/stevenydc",   # shown as @stevenydc
    "url": "",                              # optional homepage
    "bio": (
        "I work on the economics of AI. The best way to reach me about the course "
        "is email; I post about most of these topics on [X](https://x.com/stevenydc)."
    ),
}

# Left column = label, right column = value. Values support links/markup.
FACTS = [
    ("Term",       "Fall 2026, Columbia University"),
    ("Instructor", "[Steven Yin](mailto:sy2737@columbia.edu) · [@stevenydc](https://x.com/stevenydc)"),
    ("When",       "TBD"),
    ("Where",      "TBD"),
    ("Audience",   "Graduate students; undergraduates with mathematical maturity"),
    ("Format",     "A few technical weeks, then seminar-style discussion and a final project"),
]

# Short notices that appear right under the header. Delete the list to hide it.
NOTICES = [
    "**Fall 2026 — enrollment details coming soon.** This page is a living draft: "
    "the outline below is close to final, but readings, meeting times, and guest "
    "speakers will keep changing. Questions? Email "
    "[sy2737@columbia.edu](mailto:sy2737@columbia.edu).",
]

# --------------------------------------------------------------------------
# Description
# --------------------------------------------------------------------------

DESCRIPTION = """
Almost everyone has an opinion about where AI is going. Very few of those opinions
are attached to a model you can write down, argue with, and check against data.
This course is an attempt to fix that.

We invite students to think hard about the future growth and impact of AI using
tools from economics, finance, statistics, and operations research. We start with
the technical content you need to have an informed view — how frontier models are
actually trained, why their capabilities scale predictably, and what a capability
measurement is really measuring. From there the course is largely discussion and
participation-based, working through the serious quantitative literature on
takeoff, growth, and labor, and ending in a research project of your own.

You will not leave with a confident forecast. You should leave able to tell a
rigorous argument from a compelling one, and able to build your own.
"""

QUESTIONS = [
    "How much is the world spending on AI, and what is it buying?",
    "How fast is AI research progressing, and how would we know?",
    "Under what conditions does automating AI R&D produce explosive growth?",
    "Which industries get transformed first, and why do diffusion lags exist?",
    "Under what conditions is a coordinated slowdown even possible from a game-theoretic perspective?",
]

PREREQS = """
This course is intended for graduate and advanced undergraduate students.
Students should have a foundation in calculus, linear algebra, probability,
algorithms, and machine learning. Students should be comfortable reading research
papers and picking up any missing background.
"""

GRADING = [
    ("40%", "Attendance and participation",
     "This is a discussion course. Showing up prepared, having read the week's "
     "material, is most of the work."),
    ("25%", "Seminar presentation",
     "In groups, you teach the rest of the class the key ideas in an assigned "
     "reading — the model, the assumptions that drive its conclusions, and "
     "where you think it breaks."),
    ("35%", "Final project",
     "See [Final project](#project)."),
]

PROJECT = """
The final project is an original piece of analysis on some aspect of AI's
trajectory or its economic impact. Strong projects typically do one of:

- **Replicate and stress-test.** Reproduce a published forecast or growth model,
  then vary the assumptions that do the most work and report what breaks.
- **Measure something.** Build a dataset — spending, compute, deployment,
  task horizons, prices, job postings — and use it to answer a question
  nobody has cleanly answered.
- **Model a sector.** Take one industry and model the gap between what current
  systems can do and what actually gets adopted, with the diffusion lag made explicit.

Deliverables: a short proposal mid-semester, a conference-style write-up, and a
presentation in the final weeks. Groups of one to three. Details will be posted here.
"""

# --------------------------------------------------------------------------
# Readings
#
# Each entry gets a short key, used to attach it to sessions below.
# --------------------------------------------------------------------------

READINGS = {
    "davidson2026": {
        "authors": "Davidson, Halperin, Houlden & Korinek",
        "year": "2026",
        "title": "When Does Automating AI Research Produce Explosive Growth?",
        "url": "https://thomas-houlden.com/assets/Davidson,%20Halperin,%20Houlden,%20and%20Korinek%20(2026).pdf",
    },
    "rsi": {
        "authors": "Elasticity Institute",
        "year": "",
        "title": "Economics of Recursive Self-Improvement",
        "url": "https://elasticity.institute/rsi-paper.pdf",
    },
    "ai2027": {
        "authors": "Kokotajlo et al.",
        "year": "",
        "title": "AI 2027",
        "url": "https://ai-2027.com/",
    },
    "ai2040": {
        "authors": "",
        "year": "",
        "title": "AI 2040",
        "url": "https://ai-2040.com/",
    },
    "trammell_labor": {
        "authors": "Trammell",
        "year": "",
        "title": "Is Labor a Luxury in the Long Run?",
        "url": "https://www.forethought.org/research/is-labor-a-luxury-in-the-long-run",
        "venue": "Forethought",
    },
    "normal_tech": {
        "authors": "Narayanan & Kapoor",
        "year": "",
        "title": "AI as Normal Technology",
        "url": "https://www.aisnakeoil.com/p/ai-as-normal-technology",
    },
    "openrouter": {
        "authors": "Aubakirova, Atallah, Clark, Summerville & Midha",
        "year": "2026",
        "title": "State of AI: An Empirical 100 Trillion Token Study with OpenRouter",
        "url": "https://arxiv.org/abs/2601.10088",
    },
    "metr_horizon": {
        "authors": "METR",
        "year": "2025",
        "title": "Measuring AI Ability to Complete Long Tasks",
        "url": "https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/",
    },
    "metr_rct": {
        "authors": "METR",
        "year": "2025",
        "title": "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity",
        "url": "https://arxiv.org/abs/2507.09089",
    },
    "gate": {
        "authors": "Epoch AI",
        "year": "",
        "title": "GATE: Modeling the Trajectory of AI and Automation",
        "url": "https://epoch.ai/blog/announcing-gate",
    },
    "ai2030": {
        "authors": "Epoch AI",
        "year": "",
        "title": "AI in 2030",
        "url": "https://epoch.ai/files/AI_2030.pdf",
    },
    "chinchilla": {
        "authors": "Hoffmann et al.",
        "year": "2022",
        "title": "Training Compute-Optimal Large Language Models (Chinchilla)",
        "url": "https://arxiv.org/abs/2203.15556",
    },
    "ajj": {
        "authors": "Aghion, Jones & Jones",
        "year": "",
        "title": "Artificial Intelligence and Economic Growth",
        "url": "https://web.stanford.edu/~chadj/AJJ-AIandGrowth.pdf",
    },
    "jones_dilemma": {
        "authors": "Jones",
        "year": "",
        "title": "The A.I. Dilemma: Growth versus Existential Risk",
        "url": "https://web.stanford.edu/~chadj/existentialrisk.pdf",
    },
    "erdil": {
        "authors": "Erdil & Besiroglu",
        "year": "2023",
        "title": "Explosive Growth from AI Automation: A Review of the Arguments",
        "url": "https://arxiv.org/abs/2309.11690",
    },
    "gpts": {
        "authors": "Eloundou et al.",
        "year": "2023",
        "title": "GPTs are GPTs: An Early Look at the Labor Market Impact Potential of LLMs",
        "url": "https://arxiv.org/abs/2303.10130",
    },
    "canaries": {
        "authors": "Brynjolfsson, Chandar & Chen",
        "year": "2025",
        "title": "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI",
        "url": "https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf",
    },
    "chatgpt_usage": {
        "authors": "Chatterji et al.",
        "year": "",
        "title": "How People Use ChatGPT",
        "url": "https://cdn.openai.com/pdf/a253471f-8260-40c6-a2cc-aa93fe9f142e/economic-research-chatgpt-usage-paper.pdf",
    },
    "agi_emh": {
        "authors": "Chow, Halperin & Mazlish",
        "year": "",
        "title": "Transformative AI, Existential Risk, and Real Interest Rates",
        "url": "https://www.basilhalperin.com/papers/agi_emh.pdf",
    },
    "capital22": {
        "authors": "Trammell & Patel",
        "year": "",
        "title": "Capital in the 22nd Century (excerpts)",
        "url": "https://philiptrammell.substack.com/p/capital-in-the-22nd-century",
    },
    "jobless": {
        "authors": "Hall",
        "year": "",
        "title": "The Politics of Jobless Prosperity",
        "url": "https://freesystems.substack.com/p/the-politics-of-jobless-prosperity",
    },
}

# --------------------------------------------------------------------------
# Schedule
#
# tags: short labels shown next to a session title. Suggested vocabulary:
#   "lecture", "seminar", "guest", "project", "no class"
# readings: list of keys from READINGS above.
# --------------------------------------------------------------------------

UNITS = [
    {
        "num": 1,
        "title": "Foundations of frontier AI",
        "blurb": (
            "Students should arrive with basic knowledge of deep learning and NLP. "
            "These weeks build the shared technical vocabulary the rest of the course "
            "assumes: how frontier models are actually made, why scaling is predictable, "
            "and what a capability measurement is really measuring."
        ),
        "sessions": [
            {
                "title": "The frontier model training pipeline",
                "tags": ["lecture"],
                "summary": (
                    "Pretraining, mid-training, and RL — where the compute goes, where "
                    "the data comes from, and which stage is currently the bottleneck."
                ),
                "readings": [],
            },
            {
                "title": "Predictable scaling: scaling laws and compute-optimal training",
                "tags": ["lecture"],
                "summary": (
                    "Loss-versus-compute power laws, the compute-optimal frontier, and "
                    "what scaling laws do and do not license you to extrapolate."
                ),
                "readings": ["chinchilla"],
            },
            {
                "title": "Measuring capability: benchmarks and their pathologies",
                "tags": ["lecture", "guest"],
                "summary": (
                    "Saturation, contamination, construct validity, and the gap between "
                    "benchmark scores and economically useful work. Introduces METR's "
                    "task-horizon methodology as an alternative measurement strategy."
                ),
                "readings": ["metr_horizon", "openrouter"],
                "note": "Potential guest speaker from a frontier lab.",
            },
        ],
    },
    {
        "num": 2,
        "title": "Forecasting methods and economic models",
        "blurb": (
            "The technical toolkit needed to reproduce, rather than merely read, the "
            "quantitative claims in this literature: time-horizon extrapolation, growth "
            "models with automation, and the core mechanics of a recursive "
            "self-improvement model."
        ),
        "sessions": [
            {
                "title": "Extrapolation and uncertainty: rebuilding the METR time-horizon curve",
                "tags": ["lecture"],
                "summary": (
                    "Fitting doubling times, propagating uncertainty honestly, and the "
                    "standard ways trend extrapolations mislead. Hands-on with the data."
                ),
                "readings": ["metr_horizon", "gate"],
            },
            {
                "title": "Growth models with automation",
                "tags": ["lecture"],
                "summary": (
                    "Ideas production functions, task-based automation, and the "
                    "substitution elasticities that decide whether automation raises the "
                    "growth rate or merely the level."
                ),
                "readings": ["ajj", "erdil"],
            },
            {
                "title": "Recursive self-improvement: the core model",
                "tags": ["lecture", "guest"],
                "summary": (
                    "The conditions under which automating AI R&D feeds back into itself, "
                    "and the parameter values that separate an explosion from a fizzle."
                ),
                "readings": ["davidson2026", "rsi"],
                "note": "Potential guest speaker from the takeoff-modeling literature (Forethought, Epoch AI, METR).",
            },
        ],
    },
    {
        "num": 3,
        "title": "Macroeconomic impact",
        "blurb": (
            "Seminar format. Students are divided into groups; each group teaches the "
            "rest of the class the key ideas in an assigned reading — what the model "
            "assumes, what actually drives the result, and where it is fragile."
        ),
        "sessions": [
            {
                "title": "Explosive growth: the case and the objections",
                "tags": ["seminar"],
                "summary": "",
                "readings": ["erdil", "davidson2026", "ai2030"],
            },
            {
                "title": "Labor, capital, and the long run",
                "tags": ["seminar"],
                "summary": "If AI can do the work, what is human labor for, and who owns the returns?",
                "readings": ["trammell_labor", "capital22", "jobless"],
            },
            {
                "title": "What markets believe: interest rates and existential risk",
                "tags": ["seminar"],
                "summary": (
                    "If transformative AI were coming, would asset prices already show it? "
                    "And what does a growth-versus-risk tradeoff look like when written down."
                ),
                "readings": ["agi_emh", "jones_dilemma"],
            },
            {
                "title": "The labor market so far: evidence, not forecasts",
                "tags": ["seminar"],
                "summary": "What we can actually measure today about exposure, adoption, and employment.",
                "readings": ["gpts", "canaries", "chatgpt_usage"],
            },
        ],
    },
    {
        "num": 4,
        "title": "Applications, sector by sector",
        "blurb": (
            "From the macro angle to the micro. For each sector: what current models can "
            "and cannot do, and why diffusion lags capability. Closes with scenario "
            "synthesis and final presentations."
        ),
        "sessions": [
            {
                "title": "Software, science, and silicon",
                "tags": ["seminar", "guest"],
                "summary": (
                    "Software engineering, drug design, materials science, and chip design — "
                    "the sectors where automation is furthest along, and the measurement "
                    "problem of telling real speedups from perceived ones."
                ),
                "readings": ["metr_rct"],
                "note": "Potential guest speaker from a frontier startup (e.g. Periodic Labs).",
            },
            {
                "title": "Law, finance, and defense",
                "tags": ["seminar"],
                "summary": (
                    "Regulated and adversarial sectors, where the binding constraint is "
                    "rarely raw capability."
                ),
                "readings": [],
            },
            {
                "title": "Scenario synthesis",
                "tags": ["seminar"],
                "summary": (
                    "We put the scenarios side by side — fast takeoff, slow transformation, "
                    "and normal technology — and ask what evidence would move us between them."
                ),
                "readings": ["ai2027", "ai2040", "normal_tech"],
            },
            {
                "title": "Final project presentations",
                "tags": ["project"],
                "summary": "",
                "readings": [],
            },
        ],
    },
]

# --------------------------------------------------------------------------
# Guest speakers
# --------------------------------------------------------------------------

SPEAKERS_NOTE = (
    "We aim to host several guest speakers from frontier labs, forecasting "
    "organizations, and startups. Confirmed speakers will be listed here as they "
    "are scheduled."
)

SPEAKERS = [
    # ("Name", "Affiliation", "Date or topic"),
]
