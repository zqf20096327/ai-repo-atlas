# thc1006/qwen3.6-speculative-decoding-rtx3090

⭐ 35 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/thc1006/qwen3.6-speculative-decoding-rtx3090) · 个人维护

**单卡 RTX 3090 上 llama.cpp 投机解码的实测基准与审计数据集**

在一张 RTX 3090 上对 Qwen3.6-35B-A3B UD-Q4_K_XL 量化模型测量 llama.cpp 投机解码吞吐的基准研究仓库，分存档层（v1-v3 一次性运行）与受控层（A-W2，3002 次 arm-run）两级数据。所有公布数值由 checker 从已提交数据重新推导，漂移即失败；覆盖探针报告覆盖率，ERRATA.md 列出本研究自行撤回的结论（如撤销 100% 接受率的 MoE 病理机制解释）。提供历史脚本、精确 commit 锁定的复现步骤与校正后的 bench/retest_runner.py 测试框架。结论限于所列模型、commit、硬件与负载，不代表其他配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 公布数值由 checker 从提交数据重推导，漂移即失败
- 两级数据：存档层 v1-v3 与 3002 次 arm-run 的受控层 A-W2
- ERRATA.md 自行撤回此前头条结论（100% 接受率机制为计数伪象）
- 按 commit 锁定二进制、SHA256 校验模型文件的复现流程

## 适用场景

- 查阅单卡 RTX 3090 上各投机解码方法（DFlash/MTP/n-gram）的实测吞吐对比
- 复现锁定 commit 的 llama.cpp 投机解码基准测量
- 参考受控基准设计（拉丁方、ABBA 排序、块内配对分析）

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # Archived and re-measured: llama.cpp speculative decoding for Qwen3.6-35B-A3B UD-Q4_K_XL on one RTX 3090
> L6: > **Audited 2026-08-25, extended through 2026-08-28.** This repository now holds two
> L16: > The **controlled tier** is runs A to W2, 3002 arm-runs in 74 directories,

## 星数曲线

```mermaid
xychart-beta
    title "thc1006/qwen3.6-speculative-decoding-rtx3090 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-26 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `326bb827b03f` · [字段定义](../../DATASET.md)*
