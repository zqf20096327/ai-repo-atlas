# KazKozDev/cbt-assistant

⭐ 18 · JavaScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/KazKozDev/cbt-assistant) · 个人维护

**本地运行的 CBT 心理健康聊天机器人与自助日志应用**

基于 Ollama 的离线自托管认知行为疗法（CBT）应用：提供结构化思维记录、情绪与睡眠追踪、PHQ-9/GAD-7 等自评量表和引导式 SOS 练习（呼吸、着陆、渐进式肌肉放松），并附带通过 RAG 检索内置 CBT 知识库的本地聊天助手（qwen3.5:9b），引用以 [KB:chunk_id] 标注，低于相似度阈值时转为支持性对话；会话记忆持久化于 SQLite。macOS/Windows 提供启动脚本，Linux 需手动配置；明确声明非医疗设备且不含危机检测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 RAG 检索内置 CBT 知识库并引用出处，检索评测 recall@3 85.7%
- 思维日记、情绪/睡眠日志、PHQ-9/GAD-7 等量表与 SOS 练习
- 个人档案与滚动摘要持久化于 SQLite，跨重启保留记忆
- 核心聊天与日志功能 100% 离线，默认仅绑定 127.0.0.1

## 适用场景

- 在本地离线记录思维日记并追踪情绪与睡眠
- 通过对话让助手代为记录条目或启动 SOS 练习
- 无需云端账号地获得基于 CBT 知识库的自助对话支持

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: An offline, self-hosted cognitive behavioral therapy (CBT) app: structured thought records, mood and sleep tracking,
> L39: - Warm, non-judgmental dialogue with `qwen3.5:9b` running locally — core chat generation never leaves your machine.

## 星数曲线

```mermaid
xychart-beta
    title "KazKozDev/cbt-assistant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8c55ee10ac69` · [字段定义](../../DATASET.md)*
