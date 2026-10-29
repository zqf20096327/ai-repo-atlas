# luckeyfaraday/athena-code

⭐ 27 · TypeScript · MIT · 推送 2026-07-06 · [GitHub](https://github.com/luckeyfaraday/athena-code) · [官网](https://github.com/luckeyfaraday/athena-code/releases) · 个人维护

**带持久本地记忆与跨会话检索的终端 AI 编程代理**

基于 OpenCode 固定版本的 memory-focused fork：在终端编程代理上增加本地持久记忆层——按生命周期分为全局记忆、项目记忆、会话冻结快照与逐轮召回；用 SQLite FTS5 索引本产品及本机 Claude Code、Codex、opencode、Hermes 的历史会话供跨代理搜索。向模型暴露 memory_write/memory_read/session_recall 等工具，并可 spawn/接管上述代理作为子代理协作。数据默认存本地文件，模型请求经底层 OpenCode 提供商系统发出。自称早期开发阶段，macOS/Windows 二进制未签名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 全局/项目/冻结快照/逐轮召回四层记忆架构，本地 JSONL+SQLite FTS5 存储
- 跨代理（Claude Code/Codex/opencode/Hermes）会话索引与 /find-sessions 搜索
- agent_spawn/agent_takeover 等本地多代理编排工具
- Linux/macOS/Windows x64 与 ARM64 原生发布构建，支持自更新

## 适用场景

- 让编程代理在多会话间保留我的偏好与架构决策
- 搜索并接续上周在其他编程代理里的会话继续工作
- 把子任务委托给本机的 Codex/Claude Code 并取回结果

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **Athena Code is an open-source terminal AI coding agent with persistent memory,
> L30: local-first memory layer directly to the agent loop:
> L42:  `session_recall` to the model.

## 星数曲线

```mermaid
xychart-beta
    title "luckeyfaraday/athena-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `0a39afae4b11` · [字段定义](../../DATASET.md)*
