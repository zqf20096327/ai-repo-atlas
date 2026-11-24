# ArtyomITA/bonsai2-ternary-pascal

⭐ 3 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/ArtyomITA/bonsai2-ternary-pascal) · 个人维护

**让 Ternary Bonsai 2 9B 在 GTX 1080 上解码提速 51% 的 llama.cpp CUDA 补丁**

对 PrismML fork 的 llama.cpp 的一组 CUDA 改动（单文件补丁，+987/-22 行），针对 Pascal 架构（sm_61）优化 Ternary-Bonsai-2-9B（PQ2_0 权重 + MTP draft head）的解码速度，实测 +51% tok/s，且与原版 logits 位级一致。质量门用 KL 散度与 top token 一致率核验，所有融合带回退到原路径的守卫。附 LoRA 训练工具包（在同一张卡上微调）与可复现评测脚本。限制：仅覆盖一种负载、一个模型，需自编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对 Pascal（sm_61）的 PQ2_0 mat-vec 与内核融合，解码 +51%，VRAM -44 MiB
- KL 散度质量门（KLD ≤ 1e-4、top token ≥ 99.5%）保证输出位级一致
- 所有融合路径带守卫，检查失败时回退到原版路径
- 附带同卡 LoRA 微调工具包与评测脚本 eval_bonsai2.py

## 适用场景

- 在没有新卡的情况下本地跑 Ternary Bonsai 2 9B 并提速
- 需要与原版输出完全一致的推理结果时
- 复现或扩展 Pascal 架构上的 CUDA 内核优化

## 场景标签

`模型评测` `微调` `推理引擎` · 领域:评测与运维

## 证据(README 行号)

> L3: A set of CUDA changes to the PrismML fork of llama.cpp that makes
> L109: cmake -S . -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=61-real -DCMAKE_BUILD_TYPE=Release
> L120: The mat-vec alone (change 2) is proposed to the fork in PrismML-Eng/llama.cpp#368.

## 星数曲线

```mermaid
xychart-beta
    title "ArtyomITA/bonsai2-ternary-pascal 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `b556e38a5325` · [字段定义](../../DATASET.md)*
