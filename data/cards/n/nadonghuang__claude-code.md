# nadonghuang/claude-code

⭐ 26 · TypeScript · 推送 2026-08-13 · [GitHub](https://github.com/nadonghuang/claude-code) · 个人维护

**Claude Code CLI v2.1.76 的反混淆 TypeScript 源码，供学习研究**

对 Anthropic 官方 npm 包 @anthropic-ai/claude-code v2.1.76 反向工程得到的可读源码仓库：将单个约 12MB 的 cli.js 压缩包还原为 1,884 个 TS/TSX 文件与模块结构，附注释与类型标注。面向学习、安全研究与架构研究用途，明确声明不用于再分发或绕过官方许可。README 记录构建系统（Bun、React Compiler）、内部功能开关、仅限 Anthropic 员工的功能及已知缺失的约 10 个文件，需 Bun 与 Node.js 环境，部分 stub 需自行补齐方可构建。

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

- 1,884 个 TS/TSX 文件、35MB 源码、5,066 个打包模块的反混淆还原
- 记录内部 feature flags（PROACTIVE/KAIROS/AGENT_TRIGGERS 等）与 ant-only 工具
- 列出已知缺失文件清单及所需 stub（@ant/* 包、REPLTool 等）
- 声明仅供教育与研究用途，知识产权归 Anthropic

## 适用场景

- 研究 Claude Code 的内部架构与工具系统实现
- 对 AI 编码 agent 做安全研究与代码审计
- 学习大型 CLI 应用（Bun 打包、TUI 状态管理）的工程组织方式

## 场景标签

 · 领域:AI 工具源码/逆向工程研究

## 证据(README 行号)

> L19: This repository contains the **reverse-engineered TypeScript source code** from Anthropic's Claude Code CLI tool.
> L21: The official npm package ships as a single minified `cli.js` bundle (~12MB); this repo **restores the original modu
> L23: > 🎓 Built for **learning, security research, and architectural curiosity** — not for redistribution or bypassing th

## 星数曲线

```mermaid
xychart-beta
    title "nadonghuang/claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `35325a7e9531` · [字段定义](../../DATASET.md)*
