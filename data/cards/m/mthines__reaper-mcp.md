# mthines/reaper-mcp

⭐ 39 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/mthines/reaper-mcp) · [官网](https://reaper-mcp.vercel.app) · 个人维护

**REAPER 内的 MCP 服务器：用对话让 AI 执行混音与母带**

面向 REAPER 用户的 MCP 服务器：在 Claude Code 中用自然语言下达混音、路由、母带指令，服务器读取轨道的 LUFS、真峰值、频谱、立体声宽度等测量数据后，通过用户已安装的插件在打开的会话中实时做出调整，并在每次变更前后保存快照、重新测量验证。记忆层 LoreKit（可选）按插件记录经验与教训；无 LoreKit 时功能仍可用但每次会话从零开始。依赖 REAPER 6+、Claude Code 与 Node.js 20+，支持 macOS/Windows/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 先测量后动手：基于 LUFS/频谱/立体声相关度等数据决策并复核
- 使用用户已安装的插件（如 FabFilter Pro-Q 3 或回退 ReaEQ），自动研究未知插件
- LoreKit 记忆层保存插件记录与纠错教训，且用户层优先于内置知识
- 9 个技能命令：/mixer、/critique、/mastering、/learn-plugin、/make-plugin 等

## 适用场景

- 用对话完成增益分级、人声链、鼓组总线等混音操作
- 按 Spotify 等平台的响度目标做母带处理
- 让 AI 只输出测量报告而不改动工程（/critique）
- 为自己拥有的插件建立可复用的知识记录

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: reaper-mcp — Mix by asking. Type what you hear and an AI mix engineer inside your REAPER session does it.
> L12: REAPER 6+
> L13: Claude Code


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `1d241e57d0b4` · [字段定义](../../DATASET.md)*
