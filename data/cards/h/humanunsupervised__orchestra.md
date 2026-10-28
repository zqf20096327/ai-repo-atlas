# humanunsupervised/orchestra

⭐ 29 · NOASSERTION · 推送 2026-10-15 · [GitHub](https://github.com/humanunsupervised/orchestra) · 个人维护

**Rust 终端会话管理器：并行运行多个 AI 编码助手**

面向使用编码 agent 的开发者的终端会话管理器：Claude Code、Codex、OpenCode、开发服务器与 shell 运行在后台服务器（orchestra-ptyd）中，会话在左侧列表并排显示、右侧实时预览，一键切换。会话独立于窗口存活，断开 SSH 或关闭终端后 agent 继续运行，重启后可恢复。内置 MCP 服务器与带 token 保护的本地 HTTP API（127.0.0.1），供 agent 和脚本调用。0.6 起不再依赖 tmux/git/jq，仅需 bash。许可证为专有但个人与商用免费。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 后台服务器持有会话，终端关闭/SSH 断开后 agent 继续运行
- 多会话并排实时预览，识别常见编码 agent 的运行状态
- 内置 MCP 服务器与 token 保护的本地 HTTP API，agent 可驱动
- 0.6 起仅需 bash，无需 tmux/git/jq

## 适用场景

- 同时运行多个编码 agent 并实时查看各自进度
- 断开连接后让 agent 在后台继续跑任务
- 让 agent 通过 MCP 自行创建和管理会话

## 场景标签

 · 领域:开发者工具/终端

## 证据(README 行号)

> L5: Orchestra is a terminal session manager for developers who work with coding agents. Claude Code,
> L57: - **Agents can drive it too.** The MCP server lets agents list projects, start sessions in their

## 星数曲线

```mermaid
xychart-beta
    title "humanunsupervised/orchestra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0d95e0064ea9` · [字段定义](../../DATASET.md)*
