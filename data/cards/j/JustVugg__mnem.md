# JustVugg/mnem

⭐ 66 · Python · MIT · 推送 2026-07-06 · [GitHub](https://github.com/JustVugg/mnem) · 个人维护

**面向 AI agent 的零依赖记忆库：状态化 Markdown 文件存储**

为 AI agent 提供记忆层的纯 Python 库（Python 3.9+，无运行时依赖）。核心机制是把记忆当作演化的状态而非相似度检索索引：语句归入主题，新语句覆盖旧值（信念修正），过期值不再返回；私有事实仅存于内存不落盘。全部数据存放在一个 Markdown 文件中，兼作存储、人工编辑接口、审计日志与可版本控制对象，并可编译为 token 预算内的 prompt 块。检索默认为词法匹配，可开启内置 n-gram 语义模式或传入外部 embed 函数。尚未发布到 PyPI，需从 GitHub 安装。

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

- 记忆以 Markdown 文件为唯一存储，支持直接编辑与 git 版本控制
- 主题级信念修正：新语句覆盖旧值，过期值不再返回
- 私有事实（private=True）只存内存、不写入磁盘
- 零依赖；内置语义模式或可接入任意 embed 函数

## 适用场景

- 给对话 agent 加一层会记住用户偏好最新值的记忆
- 用 git/PR 审查和回溯 agent 记忆的演变
- 在无向量库、无模型的环境下给 agent 提供可移植记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L13: `mnem` treats memory as evolving **state** instead of a search index:
> L20: It is **deterministic**, **dependency-free**, and tiny — an in-process state machine,

## 星数曲线

```mermaid
xychart-beta
    title "JustVugg/mnem 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-24 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `a15b4301af00` · [字段定义](../../DATASET.md)*
