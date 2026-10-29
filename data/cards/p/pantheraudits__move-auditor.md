# pantheraudits/move-auditor

⭐ 21 · 推送 2026-08-19 · [GitHub](https://github.com/pantheraudits/move-auditor) · [官网](https://pantheraudits.com) · 组织维护

**让 AI 编码 agent 变成 Move 智能合约安全审计员的技能包**

面向 Codex 与 Claude Code 的可移植 skill（SKILL.md 格式），将 AI 编码 agent 转为 Move（Sui/Aptos）智能合约审计工具。内置 220+ 漏洞模式，覆盖链无关、Sui/Aptos 专属与 DeFi 检查；采用 8 阶段审计流水线，含置信度门控与 FP 目录的抗误报机制，并读取构建/测试日志分析算术中止与断言失败。安装方式为 git clone 后复制到 skills/commands 目录。README 声明为候选发现生成器，所有结果需人工验证，不替代深度人工审计。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 220+ 漏洞模式，覆盖 Sui 专属 46 条、Aptos 专属 25 条、DeFi 95 条
- 8 阶段审计流水线：代码库映射到分级报告
- 抗误报机制：置信度门控、证据链、FP 目录、自幻觉检查
- 构建/测试日志分析（算术中止、断言失败、expected_failure 异常）

## 适用场景

- 审计 Sui 或 Aptos 上的 Move 合约安全漏洞
- 在 Claude Code / Codex 会话中用一条命令发起完整审计
- 为 DeFi 协议（借贷/清算/预言机/质押）做安全检查

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L12: A portable skill for Codex and Claude Code that turns your AI coding agent into a Move (Sui & Aptos) smart contract
> L18: - **220+ vulnerability patterns** across chain-agnostic, Sui-specific, Aptos-specific, and DeFi checks

## 星数曲线

```mermaid
xychart-beta
    title "pantheraudits/move-auditor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-29 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9b6fea9add2c` · [字段定义](../../DATASET.md)*
