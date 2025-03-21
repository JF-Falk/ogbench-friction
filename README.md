# Introduction

Train agents on MuJoCo environments using OGBench and optionally provide a multiplier to change the MuJoCo model's friction.

This uses a sparse checkout of [reference implementations from OGBench](https://github.com/seohongpark/ogbench/tree/master?tab=readme-ov-file#reference-implementations "github.com/seohongpark/ogbench") as a base.

## Installation

```bash
pip install -r requirements.txt
```
> compared to the original OGBench requirements, this has a downgraded *matplotlib* version due to an `AttributeError` with `FigureCanvasInterAgg` (see [here](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/issues/2411 "GitHub Issue: \"AttributeError: 'FigureCanvasAgg' object has no attribute 'tostring_rgb'  #2411\""))

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
> run `python3 main_sac.py --help` for default values, notably [`--agent`](data_gen_scripts/main_sac.py#L46)


<br/>
<br/>


# Results

To roughly average out the randomness of the trained agents, ten SAC agents were trained with default friction and $10\%$ increased friction (multiplier $=1.1$) respectively.

Check the [interactive result report](https://api.wandb.ai/links/jf-johs-luh/lvuvteaf "wandb.ai"), or alternatively the following image:

<p align="center">
    <a href="./static/wandb report.pdf">
        <img src="./static/wandb report.png" alt="PNG Report"/>
    </a>
</p>


<br/>
<br/>


# Acknowledgments

- [OGBench](https://github.com/seohongpark/ogbench) for the reference implementations which serve as the core.