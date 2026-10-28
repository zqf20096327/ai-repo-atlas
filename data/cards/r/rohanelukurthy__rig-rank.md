# rohanelukurthy/rig-rank

⭐ 21 · Go · MIT · 推送 2026-02-24 · [GitHub](https://github.com/rohanelukurthy/rig-rank) · 个人维护

**通过 Ollama 在本机硬件上评测本地 LLM 性能的 Go CLI**

Go 编写的命令行工具，通过连接本地 Ollama 实例测量指定模型在用户硬件上的实际性能：吞吐量（tokens/sec）、首 token 延迟（TTFT）、提示处理速度与模型加载时间。包含原子检查、代码生成、长文生成、摘要、推理 5 个阶段的基准套件，自动检测 CPU 核数、RAM 与 GPU VRAM，输出人读报告卡与机器可读 JSON。仅测量性能，不评估模型准确性。前置条件为已安装并运行 Ollama 且至少拉取一个模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 测量 TTFT、生成/提示处理吞吐与模型加载时间
- 5 阶段基准套件（原子检查/代码/长文/摘要/推理）
- 自动检测 CPU、RAM 类型（macOS）与 GPU VRAM
- 输出 Report Card 与 JSON 报告，支持静默等待系统空闲

## 适用场景

- 购买或升级硬件前测试本地模型能否流畅运行
- 对比不同模型或量化配置在自己机器上的速度
- 在量化程度与响应速度之间做取舍决策

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: RigRank is a CLI tool written in Go that benchmarks how well Large Language Models (LLMs) run on **your specific ha
> L34: - **Ollama Integration**: Seamlessly connects to your local Ollama instance.

## 星数曲线

```mermaid
xychart-beta
    title "rohanelukurthy/rig-rank 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9f8f34557e4a` · [字段定义](../../DATASET.md)*
