# yinwenyuan28-afk/pi-memory-system

⭐ 21 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/yinwenyuan28-afk/pi-memory-system) · 个人维护 · 中文 README

**为 Pi 编码代理提供持久记忆的扩展**

面向 Pi coding agent 的持久记忆扩展：从会话中提取项目事实、决策与用户偏好，按 L1 原子记录、L2 场景块、L3 用户画像三层组织存储，后续按需召回注入；支持任务型记忆的 done/drop/reopen 状态管理，并附本地查看器检查记忆数据、处理队列与画像草稿。仅支持 Windows，需 Node.js >= 22.13.0，通过 pi install 从 npm 或本地目录安装；向量检索默认关闭，启用需自行配置嵌入服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三层记忆结构：L1 原子记录 / L2 场景块 / L3 用户画像
- 任务型记忆带 done/drop/reopen 状态流转
- 本地查看器可检查记忆数据、处理队列与画像草稿
- UI 支持中英文双语，跟随系统语言自动切换

## 适用场景

- 让 Pi 编码代理在多轮会话间记住项目决策与我的偏好
- 跟踪待办类记忆的完成与放弃状态
- 通过本地查看器排查记忆提取与召回情况

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Persistent memory for the Pi coding agent. The extension pulls project facts, decisions, and user preferences out of
> L12: - Extracts memories from conversations and retrieves them on demand.
> L13: - Organizes memory in three layers: L1 atomic records, L2 scenario blocks, L3 user profile.

## 星数曲线

```mermaid
xychart-beta
    title "yinwenyuan28-afk/pi-memory-system 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-23 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8f152eef87ce` · [字段定义](../../DATASET.md)*
