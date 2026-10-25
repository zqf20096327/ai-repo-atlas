# starkdcc/claude-code-source

⭐ 32 · TypeScript · 推送 2026-03-31 · [GitHub](https://github.com/starkdcc/claude-code-source) · 个人维护

**Claude Code CLI 源码快照存档，供安全与架构研究**

由一名大学生维护的 Claude Code 源码快照镜像，来源于 npm 分发包中 source map 暴露（2026-03-31 发现），声明原代码归 Anthropic 所有、非官方仓库。仓库收录约 1,900 文件、51 万+ 行 TypeScript 代码，README 梳理其架构：工具系统（20+ 个工具模块）、斜杠命令、服务层、IDE 桥接、权限系统、feature flags 与 Agent 编排等，供教育、防御性安全研究与软件供应链分析使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 镜像 Claude Code 约 1,900 文件、512,000+ 行 TypeScript 源码快照
- 文档化工具系统、服务层、Bridge、权限系统等架构组成
- 声明用于教育、防御性安全研究与供应链分析，非官方仓库

## 适用场景

- 研究 agentic CLI 系统的架构与实现方式
- 分析软件供应链中的构建产物泄露问题
- 了解 Claude Code 的工具调用与权限模型设计

## 场景标签

 · 领域:开发者工具/安全研究

## 证据(README 行号)

> L3: > This repository mirrors a **publicly exposed Claude Code source snapshot** that became accessible on **March 31, 2
> L14: This archive is intended to support:

## 星数曲线

```mermaid
xychart-beta
    title "starkdcc/claude-code-source 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-25 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9eac68af40c2` · [字段定义](../../DATASET.md)*
