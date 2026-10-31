# niqibiao/unity-cli-skill

⭐ 44 · Python · Apache-2.0 · 推送 2026-09-20 · [GitHub](https://github.com/niqibiao/unity-cli-skill) · 个人维护 · 中文 README

**供 AI agent 控制 Unity Editor 的零配置技能（CLI+命令契约）**

面向 Claude Code、Codex 等 skills 兼容 agent 的 Unity 编辑器控制技能：以 62 个包内建命令（56 个创作命令覆盖 editor/scene/objects/assets/prefabs/capture 六域 + 6 个控制面命令）为主通道，无结构化命令可用时回退到基于 unity-csharpconsole 的 Roslyn C# REPL。服务运行于 Unity Editor 内部，无额外 sidecar 进程，支持运行时/IL2CPP（HybridCLR）与远程 player 调试；命令执行带预检与安全上限（5000 节点、深度 128）。限制：服务绑定所有接口且无鉴权，仅适用于可信局域网；需 Unity 2022、Node.js 与 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 62 个包内建命令覆盖 6 个创作域，带预检与过期契约拒绝
- 无结构化路由时回退到 Roslyn C# REPL，服务内嵌 Unity Editor 无 sidecar
- 渐进式契约发现（Domain Index → Route Cards → Contract Bundle）控制 token 占用
- 支持运行时 player 调试（截图、profiler、cs pull 取回文件）与 HybridCLR/IL2CPP

## 适用场景

- 让 AI coding agent 直接在 Unity 项目里创建对象、操作场景与 prefab
- 通过 agent 运行 Unity 测试、截图与 profiler 录制
- 团队以自定义命令与代码片段库沉淀可复用 Unity 操作

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **AI coding agent skill for Unity Editor — works with any skills-compatible agent (Claude Code, Codex, …)**
> L24: ### ⚡ CLI + Skills
> L26: CLI commands are exposed through the agent's skill system.

## 星数曲线

```mermaid
xychart-beta
    title "niqibiao/unity-cli-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4e4ee77ce774` · [字段定义](../../DATASET.md)*
