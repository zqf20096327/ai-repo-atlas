# botAGI/morpheus-ai

⭐ 19 · Python · MIT · 推送 2026-07-26 · [GitHub](https://github.com/botAGI/morpheus-ai) · [官网](https://github.com/botAGI/morpheus-ai#readme) · 个人维护 · 中文 README

**为编码 agent 编译项目状态（WAKE.md）并核验其声明**

面向使用 AI 编码 agent 的开发者：从项目源码的显式标记（TODO/DECISION/FIXME 等）编译 WAKE.md 项目状态文件，`morpheus check` 在本地将 agent 输出的声明对照源码证据与状态判定为 verified/stale/incorrect/unknown；配合 state.json、evidence.jsonl 与 ed25519 签名收据做可验证溯源。另含实验性自主学习实验室，可基于已接受的声明构建数据集并运行本地 MLX LoRA 训练，激活受评估门控约束。声明 check 默认本地运行，不发送文本到云端。以 PyPI 包（beta 0.2.0b2）提供 uvx/pipx 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- WAKE.md 编译器：从源码显式标记提取决策/任务/证据生成项目状态文件
- `morpheus check` 本地核验 agent 声明，返回 verified/stale/incorrect/unknown
- ed25519 签名收据与 SHA-256 哈希的可验证溯源链
- 实验性学习实验室：由已接受声明构建数据集，本地 MLX LoRA 训练，激活需过评估门控

## 适用场景

- 让编码 agent 开工前读取 WAKE.md 了解项目当前状态，避免冷启动
- 合并前核验 agent 回答中的声明是否与源码一致
- 对 agent 输出做过期/错误声明的持续检测

## 场景标签

 · 领域:开发者工具/LLM 可靠性

## 证据(README 行号)

> L40: Morpheus compiles project state, checks agent text against source-backed
> L144: - **Local claim check**: `morpheus check` verifies agent text from a file or

## 星数曲线

```mermaid
xychart-beta
    title "botAGI/morpheus-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c6241d3be894` · [字段定义](../../DATASET.md)*
