# bopalvelut-prog/autoresearch

⭐ 20 · Python · 推送 2026-03-26 · [GitHub](https://github.com/bopalvelut-prog/autoresearch) · 组织维护

**CPU 上运行的自主 AI 研究循环：本地 LLM 自动调参训练**

karpathy/autoresearch 的分支，面向无 GPU 环境：由小型本地 LLM（Qwen 2.5 0.5B，经 prima.cpp 服务）提出超参修改，train.py 在固定 5 分钟预算内运行训练实验，结果改善则自动提交，循环执行（约每小时 12 次）。指标为 val_bpb，实验记录到 TSV/JSON/CSV 并可生成排行榜。通过 uv 安装运行，支持 Linux/macOS/Windows，自动检测 CPU/Apple Silicon/NVIDIA GPU；代码中说明避开 Ollama 改用 prima.cpp。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 LLM 驱动的超参修改→训练→自动提交闭环
- 无需 GPU，固定 5 分钟实验预算，约每小时 12 次实验
- 实验结果记录为 TSV/JSON/CSV 并带排行榜命令
- 针对强/弱硬件（手机、旧笔记本）提供参数调优建议

## 适用场景

- 在笔记本上过夜跑自主超参搜索实验
- 无 GPU 环境下进行小型 GPT 训练实验
- 查看实验排行榜追踪调参效果

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L7: **An autonomous AI researcher that runs on any computer. No GPU required.**
> L17: 1. A small local LLM (Qwen 2.5 0.5B via **prima.cpp** server) suggests hyperparameter changes
> L19: 3. If the result improves, it's committed automatically

## 星数曲线

```mermaid
xychart-beta
    title "bopalvelut-prog/autoresearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fc54a38dda3c` · [字段定义](../../DATASET.md)*
