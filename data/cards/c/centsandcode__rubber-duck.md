# centsandcode/rubber-duck

⭐ 15 · Python · MIT · 推送 2026-09-04 · [GitHub](https://github.com/centsandcode/rubber-duck) · [官网](https://getrubberduck.online) · 个人维护

**Claude Code 插件：让 AI 以苏格拉底式提问引导用户自行调试**

面向使用编码 agent 的开发者的 Claude Code 插件：激活后 agent 不直接给出修复方案，而是通过提问引导用户自己找到答案，灵感来自橡皮鸭调试法。提供 lite/full/ultra 三档提问强度，仅在显式激活时生效，可用命令或自然语言退出。核心机制是 SKILL.md（Claude Code 加载）与可移植的 AGENTS.md（Cursor、Copilot 等可读取，但未在其他工具测试）。附带 16 例基准测试与复现脚本。

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

- 激活后 agent 以提问代替直接给答案，直到用户显式要求解答
- lite/full/ultra 三档提问强度，按经验调整脚手架量
- AGENTS.md 纯文本规则可被 Cursor/Codex/Copilot/Windsurf 等读取
- 附 16 例基准测试及复现脚本（pip install anthropic 运行）

## 适用场景

- 调试时想让 AI 引导我自己定位 bug 而非直接给修复
- 学习或理解陌生代码库时用提问式脚手架辅助思考
- 在其他编码 agent 中通过 AGENTS.md 尝试同样的提问模式

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: A plugin for Claude Code that inverts the agent's role: instead of handing you
> L41: **Cursor, Codex, Copilot, Windsurf and anything else that reads `AGENTS.md`:**

## 星数曲线

```mermaid
xychart-beta
    title "centsandcode/rubber-duck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `1065eef18a02` · [字段定义](../../DATASET.md)*
