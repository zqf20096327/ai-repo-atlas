# SynaLinks/synalinks-skills

⭐ 908 · Python · Apache-2.0 · 推送 2026-09-28 · [GitHub](https://github.com/SynaLinks/synalinks-skills) · [官网](https://synalinks.github.io/synalinks/) · 个人维护

**教编码代理正确使用 Synalinks 框架的 Agent Skill**

收录单个 SKILL.md 格式技能 synalinks 的仓库：通过可复用指令教编码代理（Claude Code、Codex、OpenCode、pi 等）按惯例使用 Synalinks 神经符号框架，避免模型混用 Keras/LangChain/DSPy 语法。SKILL.md 按框架切片组织（核心、程序、模块、控制流、代理、知识、训练、奖励、优化器、Provider 等），每节指向可运行脚本与参考文档。通过官方 skills CLI（npx skills）安装，不支持语义化版本，跟踪仓库 main 分支并以 skills-lock.json 锁定内容哈希。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个技能覆盖 Synalinks 全框架，按 11 个切片组织
- 支持 70+ 编码代理（Claude Code、Codex、OpenCode、Cursor 等），内容同一份
- skills-lock.json 以 SHA-256 内容哈希实现可复现安装
- 提供 Claude.ai/Desktop 的 .skill 归档打包方式

## 适用场景

- 让我使用的编码代理写出地道的 Synalinks 代码
- 团队与 CI 中以锁文件固定同一份技能内容
- 在多个代理客户端间共享同一技能

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: This repository contains skills for coding agents that read the open Agent
> L17: The goal of Synalinks skills is to teach coding agents to use the Synalinks

## 星数曲线

```mermaid
xychart-beta
    title "SynaLinks/synalinks-skills 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 906 --> 909
    line [907, 908, 908]
```

2026-10-18 907 → 2026-10-31 908（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `154774d542a0` · [字段定义](../../DATASET.md)*
