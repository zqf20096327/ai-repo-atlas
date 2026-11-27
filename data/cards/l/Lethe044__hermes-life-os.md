# Lethe044/hermes-life-os

⭐ 247 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/Lethe044/hermes-life-os) · 个人维护

**本地优先的个人生活管理 OS：记录并关联情绪、睡眠、习惯与任务**

基于 Python 的本地优先个人生活管理系统：追踪情绪、睡眠、营养、习惯、任务、支出等 14 类数据，通过自然语言调用 320 个内置工具完成记录、日程规划与周回顾；关联引擎计算指标间的 Pearson 相关（含 1-2 天滞后分析）并自动检测模式。通过 Cron 定时生成晨间简报与晚间反思，支持加密、多档案隔离与多用户账号；LLM 后端可自动检测，也可完全脱离语言模型从命令行直接运行工具，并提供插件系统扩展自定义工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 320 个自然语言可调用工具，覆盖记录、规划、实验与回顾
- 关联引擎计算 Pearson 相关与滞后预测分析，无外部依赖
- 支持 Ollama 本地运行（免 API key）与 Docker 部署
- 多档案/多用户数据隔离，Salted PBKDF2 存储用户密钥

## 适用场景

- 用自然语言记录睡眠、饮食、情绪等日常数据并自动追踪习惯
- 让系统分析睡眠与情绪等指标之间的关联模式
- 每天自动生成简报与周回顾，规划一天的安排
- 家庭多人共用一套实例但各自数据隔离

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L12: **The personal OS that grows with you.** Track how you feel, plan your day, keep your life
> L117: `demo/analytics.py` computes real Pearson correlation coefficients between
> L169: Every tool also runs straight from the shell, with no language model and no API key:

## 星数曲线

```mermaid
xychart-beta
    title "Lethe044/hermes-life-os 星数(近 18 点)"
    x-axis ["2026-10-25", "2026-10-27", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-27"]
    y-axis "stars" 218 --> 249
    line [220, 221, 222, 223, 227, 229, 220, 236, 237, 239, 241, 242, 243, 244, 245, 246, 247, 247]
```

2026-10-25 220 → 2026-11-27 247（+27）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `2743f592e6f0` · [字段定义](../../DATASET.md)*
