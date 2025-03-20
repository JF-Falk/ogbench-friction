# Introduction

Train agents on MuJoCo environments using OGBench and optionally provide a multiplier to change the MuJoCo model's friction.

This uses a sparse checkout of [reference implementations from OGBench](https://github.com/seohongpark/ogbench/tree/master?tab=readme-ov-file#reference-implementations "github.com/seohongpark/ogbench") as a base.

## Installation

```bash
pip install -r requirements.txt
```
> compared to the original OGBench requirements, this has a downgraded *matplotlib* version due to an `AttributeError` with `FigureCanvasInterAgg`

## Execution

Navigate to the directory and update `PYTHONPATH`:

```bash
cd data_gen_scripts/
export PYTHONPATH="../impls:${PYTHONPATH}"
export PYTHONPATH="../wrappers:${PYTHONPATH}"
```

and run the [OGBench command normally](https://github.com/seohongpark/ogbench/tree/master?tab=readme-ov-file#reproducing-expert-policies "github.com/seohongpark/ogbench"):

```bash
# run without editing friction:
python3 main_sac.py --train_steps=400000 --save_interval=400000

# run with 10% increased friction:
python3 main_sac.py --train_steps=400000 --save_interval=400000 --friction_mult=1.1
```

<br/>
<br/>

# Acknowledgments

- [OGBench](https://github.com/seohongpark/ogbench) for the reference implementations which serve as the core.