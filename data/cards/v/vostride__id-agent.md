# vostride/id-agent

⭐ 81 · TypeScript · MIT · 推送 2026-06-03 · [GitHub](https://github.com/vostride/id-agent) · [官网](https://vostride.com/) · 组织维护

**面向 AI agent 的词组式 ID 生成库，替代 UUID 省约 token**

为 AI agent 场景提供基于英文单词的紧凑 ID：默认 8 词约 96 bits 熵、约 14 tokens，相比 UUID v4 约 23 tokens 减少 token 消耗；词表 4096 词，每词在 o200k_base 分词器下恰为 1 个 BPE token。支持随机 ID（密码学安全随机）、基于 HMAC-SHA256 的确定性 ID、解析、校验、双向别名映射（用于上下文 token 压缩）与重复 ID 检测。以 JavaScript/TypeScript 与 Python 双语言包提供，熵可通过词数 1-16 配置（约 12-192 bits）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 词组 ID 默认 8 词约 96 bits 熵、约 14 tokens，低于 UUID v4 的约 23 tokens
- 4096 词表，每词恰为 o200k_base 的 1 个 BPE token
- 随机 ID 与 HMAC-SHA256 确定性 ID、解析、校验、别名映射、重复检测
- JavaScript/TypeScript 与 Python 双实现共享同一词表与熵模型

## 适用场景

- 我在 agent 的工具调用、日志与记忆传递中用可读 ID 替代 UUID 以省 token
- 把长 ID 映射为短词组别名压缩 LLM 上下文
- 按业务规模（测试/团队/生产）选择不同词数控制碰撞概率

## 场景标签

 · 领域:LLM 基础设施/开发者库

## 证据(README 行号)

> L22: AI agents pass IDs through prompts, tool calls, logs, traces, and memory. UUIDs are great for databases, but they a
> L24: Where UUIDs cost about 23 tokens and get hallucinated by LLMs, id-agent produces memorable word-based IDs at about 
> L129: id-agent is implemented as first-class packages for:

## 星数曲线

```mermaid
xychart-beta
    title "vostride/id-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 79 --> 82
    line [80, 81, 81]
```

2026-10-18 80 → 2026-10-29 81（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `54bbe2ef656a` · [字段定义](../../DATASET.md)*
