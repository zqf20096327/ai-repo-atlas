# Plural-Organization/Plural

⭐ 5 · Python · GPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/Plural-Organization/Plural) · [官网](https://plrl.host/) · 组织维护

**为编码 agent 提供多人共享会话与权限门的协作 CLI**

在宿主机上以宿主密钥运行一个编码 agent，队友通过终端或 web 应用加入房间并提交提示；写与执行类工具调用始终等待宿主批准，guest 发起的运行不能被规则直接放行。提供 open/review 两种提示模式、每轮的参与者归属、事件溯源日志（重连/回放/审计）、自托管 relay 选项。单二进制分发，安装脚本同时下载 plural 客户端与内置 Python 及 SDK 的 plural-host。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多人实时共享同一 agent 会话，含提示队列与每轮归属
- 写/执行工具调用经权限门，guest 运行不可被规则放行
- 支持 Claude Code、Codex、API key、openai 兼容端点及本地模型
- 事件溯源 append-only 日志，支持重连、回放与审计

## 适用场景

- 团队结伴使用同一台机器上的编码 agent 并共享可见性
- review 模式下宿主逐条审批他人对 agent 的提示
- 需要审计每次工具调用与 diff 的协作开发会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L16: - **a shared live session** — the host runs the agent on their machine with their own credentials. teammates join f
> L23: - **your model, your login** — Claude Code, Codex, an API key, any openai-compatible endpoint, or a local model (ol

## 星数曲线

```mermaid
xychart-beta
    title "Plural-Organization/Plural 星数(近 3 点)"
    x-axis ["2026-11-02", "2026-11-15", "2026-11-27"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-02 4 → 2026-11-27 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `6182784e614b` · [字段定义](../../DATASET.md)*
