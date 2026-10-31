# InternLM/RNGBench

⭐ 42 · Python · 推送 2026-10-26 · [GitHub](https://github.com/InternLM/RNGBench) · [官网](https://internlm.github.io/RNGBench/) · 组织维护 · 中文 README

**评测多模态大模型在非马尔可夫游戏中记忆-行动能力的基准**

RNG-Bench 是 EMNLP 2026 论文的官方实现，通过两个互补游戏（Matching Pairs 静态分类隐藏状态、3D Maze 动态空间隐藏状态）在闭环中评测多模态大模型从历史重建隐藏状态并据此行动的能力。两游戏共享一个模型注册表与评测框架，支持 OpenAI 兼容端点（含 vLLM/lmdeploy/Ollama 自部署）、Gemini 原生 API、火山方舟。难度可控（棋盘/地图尺寸、模态），最难的配置达到约 128K token 与约 350 张图像输入。提供 git clone 源码 + conda + pip 安装方式，含单人对局、双人对战协议与批量扫描脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两个互补游戏（Matching Pairs 与 3D Maze）共享一套评测框架与严格解析器
- 闭环 remember-to-act 评测：回忆错误会改变后续观察
- 支持 OpenAI 兼容端点、Gemini 原生 API、火山方舟等多种接入
- 难度可控：隐藏状态规模、视觉模式、观测模态可独立调节

## 适用场景

- 我要系统评测多模态大模型的隐藏状态记忆与推理能力
- 我想对比多家前沿模型在长上下文多图输入下的表现
- 我要用双人对战协议测模型利用对手信息的能力

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L37: changes what it sees next. **RNG-Bench** isolates this **remember-to-act** ability
> L47: Both run under one harness and one strict parser, so a score drop reflects
> L110: ├── framework/               # Shared eval harness: LLM client, runner, game, types

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/RNGBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `de01e8ffe9b6` · [字段定义](../../DATASET.md)*
