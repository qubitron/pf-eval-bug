## Repro steps

Copy .env.sample to .env and fill in env variables

```
pip install -r requirements txt
```

```
python evaluate-fast.py
```

output:
```
Starting evaluate...
[{'gpt_relevance': 1.0, 'gpt_fluency': 5.0, 'gpt_coherence': 5.0, 'gpt_groundedness': 3.0}, {'gpt_relevance': 1.0, 'gpt_fluency': 1.0, 'gpt_coherence': 3.0, 'gpt_groundedness': 5.0}, {'gpt_relevance': 3.0, 'gpt_fluency': 3.0, 'gpt_coherence': 1.0, 'gpt_groundedness': 3.0}]
Finished evaluate in 11.045098304748535s
```

then try prompt flow:
```
pf evaluate-pf.py
```

Takes about 113 seconds:
```
======= Run Summary =======

Run name: "pf_eval_bug_git_variant_0_20240512_170106_452482"
Run status: "Completed"
Start time: "2024-05-12 17:01:06.452482"
Duration: "0:01:52.694595"
Output path: "C:\Users\dantaylo\.promptflow\.runs\pf_eval_bug_git_variant_0_20240512_170106_452482"

Finished evaluate in 113.05101656913757s
```
