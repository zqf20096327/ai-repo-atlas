# doronp/gitmemory

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/doronp/gitmemory) · 个人维护

**为 AI agent 保存压缩丢失上下文的 git 版本化记忆工具**

面向使用本地追加式 transcript 文件的 AI 编码 agent（Claude Code、pi 等已适配）的记忆层：watcher 监听 transcript 增长，把新增字节作为连续段提交到本地 git 仓库，verify 命令校验段落无洞无重叠并比对摘要，recall 基于 SQLite FTS5 的 BM25 检索按字节偏移取回原始对话轮。运行时无 LLM、无网络调用、核心零依赖。可选 hook shim、key ideas/决策图推导与 Datasette 仪表盘。需 Python 3.13+ 与 git，经 uv/pipx 从 git 仓库安装。

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

- transcript 字节级捕获进 git，verify 提供无洞无重叠的连续性证明
- BM25/SQLite FTS5 检索，运行时无 LLM、无网络调用、核心零依赖
- 470 个 LongMemEval 跨压缩边界实例上轮次召回 0.7456（对照 live window 0.0000）
- Claude Code 可作为插件安装并附加 /gitmemory:recall 技能

## 适用场景

- agent 压缩上下文后找回被丢弃的历史对话轮
- 本地留存并审计完整的 agent 会话记录
- 对 agent 会话做带出处（字节偏移）的检索

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L20: When an agent compacts its context, everything behind the boundary drops out of
> L235: gitmemory works with any agent whose history is a **local, append-only file
> L91: |`gitmemory recall "<query>"`|Searches the index and prints one line per turn, dated, the user's own words newest f

## 星数曲线

```mermaid
xychart-beta
    title "doronp/gitmemory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a4da3b3adb54` · [字段定义](../../DATASET.md)*
