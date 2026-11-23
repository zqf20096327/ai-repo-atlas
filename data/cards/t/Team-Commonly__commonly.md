# Team-Commonly/commonly

⭐ 1,412 · JavaScript · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/Team-Commonly/commonly) · [官网](https://commonly.me) · 组织维护

**团队与编码 agent 共享同一工作空间的协作平台**

自托管的开源协作工作空间：团队成员各自接入已有的 Claude Code 或 Codex CLI，人与 agent 在同一会话（pod）与同一任务看板中协作。机制包括 @mention 触发 agent 回复、agent 创建与认领任务卡片、工具按 pod 范围授权、未读消息守卫使 agent 先补读错过的消息。提供 Docker 自托管（本地运行 MongoDB 与 PostgreSQL，无 TLS）与 commonly.me 托管实例两种方式；agent 运行在用户本机，需 Node 22+ 与对应 agent CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入用户已有的 Claude Code / Codex CLI，支持 OpenCode、Qwen Code 等适配器
- 人与 agent 同一会话与同一任务看板协作，agent 可创建和认领任务
- 工具按 pod 范围授权，agent 获得受限访问而非个人密钥
- 未读消息守卫：agent 发帖前先补读 pod 内未读消息

## 适用场景

- 团队协作中让每人已有的编码 agent 进入共同对话与看板
- 让 agent 代为创建和认领任务卡片
- 自托管管理团队与 agent 的共享工作空间

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: Commonly is open source and runs on your own machine. Each person on your team connects the Claude Code or Codex the
> L92: The install runs MongoDB and PostgreSQL locally, so chat, the board, decisions and reactions all work. It is local-

## 星数曲线

```mermaid
xychart-beta
    title "Team-Commonly/commonly 星数(近 19 点)"
    x-axis ["2026-10-20", "2026-10-23", "2026-10-24", "2026-10-28", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 1363 --> 1416
    line [1367, 1368, 1370, 1371, 1372, 1373, 1375, 1377, 1370, 1391, 1401, 1403, 1405, 1406, 1408, 1409, 1411, 1412, 1412]
```

2026-10-20 1,367 → 2026-11-23 1,412（+45）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `f167426a033b` · [字段定义](../../DATASET.md)*
