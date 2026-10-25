# voice-from-the-outer-world/lisan-bench

⭐ 65 · Python · 推送 2026-05-31 · [GitHub](https://github.com/voice-from-the-outer-world/lisan-bench) · 个人维护

**轻量 LLM 基准：词链变换任务同时考察规划、词汇与长输出**

基于 Lewis Carroll 词梯游戏的开放式变体构建的 LLM 评测基准：模型从起始词出发生成链，每个词与前一词编辑距离为 1、须为词典词且不得重复；主分数为所有起始词最长合法链前缀的有效转移之和。默认 50 个起始词、每词 3 次试验（150 次调用），另提供 15x2 精简预设（30 次调用）。内置 OpenAI、Anthropic、Google、Moonshot、Z.AI、ZenMux、OpenRouter 的 provider 集成，通过 uv 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 词链开放式变体：Levenshtein 距离 1、词典校验、禁止重复
- 默认 50 词 x 3 次试验，另提供 15x2 精简预设（约省 4-5 倍调用）
- 固定 SCOWL/ESDB 词典并校验 SHA-256，缺失时可再生成
- 支持 OpenRouter 及直连 provider 路由与批处理 API

## 适用场景

- 评测 LLM 的规划、词汇与长序列生成能力
- 低成本跑精简基准做模型排序或消融实验
- 自定义起始词集生成并跑基准

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: **LisanBench** is a lightweight, *cheap-to-run* benchmark for large language models that stresses **forward planning
> L122: |`lisanbench/`|Runtime package for benchmark orchestration, CLI parsing, routing, scoring, result storage, reporti

## 星数曲线

```mermaid
xychart-beta
    title "voice-from-the-outer-world/lisan-bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-25 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b1dc989b502d` · [字段定义](../../DATASET.md)*
