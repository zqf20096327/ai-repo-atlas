# TakatoHonda/sui-lang

⭐ 370 · Python · MIT · 推送 2025-12-16 · [GitHub](https://github.com/TakatoHonda/sui-lang) · 个人维护

**面向 LLM 代码生成的结构化伪代码语言（Isu/Sui）**

原本的行式 Sui 语言正在转向 Isu：一种供 LLM 读写的主要产物的结构化伪代码，可确定性解析为封闭词表的 IIR（JSON 兼容 AST），支持规范化与步骤级错误定位/修补流程；后端（Python/Wasm/LLVM IR）仅在规划中，尚未实现。仓库内提供 Isu v0 的解析/规范化/打印/校验流水线与 pytest 往返测试，旧版 Sui（解释器/转译器/wasm 工具/playground）保留于 sui_legacy 目录并标注为 legacy。以仓库本地 Python 包形式从源码运行，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Isu 文本 ⇄ IIR（JSON 兼容 AST）⇄ 规范 Isu 的往返管线
- 封闭词表 AST，支持确定性解析与规范化（AUTO_ID）
- 步骤级错误定位与补丁工作流设计
- 旧版 Sui 保留在 sui_legacy，含解释器、Sui/Python/Wasm 转译器与 playground

## 适用场景

- 让 LLM 以结构化伪代码作为生成代码的中间表示
- 对 LLM 生成的代码做步骤级错误定位与修补
- 研究面向 LLM 的语言设计与确定性解析

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: This repository is shifting its primary focus from the original line-based **Sui** language to **Isu**, a structured
> L14: Isu is the **primary artifact** an LLM reads/writes. It is parsed deterministically into **IIR (Isu Intermediate Re

## 星数曲线

```mermaid
xychart-beta
    title "TakatoHonda/sui-lang 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 369 --> 371
    line [370, 370]
```

2026-10-18 370 → 2026-10-30 370（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2e5eb7d7dbb7` · [字段定义](../../DATASET.md)*
