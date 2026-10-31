# y5862000/threaddeck-for-codex

⭐ 14 · JavaScript · MIT · 推送 2026-09-08 · [GitHub](https://github.com/y5862000/threaddeck-for-codex) · [官网](https://threaddeck.dev/) · 个人维护

**在 Stream Deck 上监控与操控 Codex 任务的 macOS 物理面板**

面向 Codex Desktop 用户的 Elgato Stream Deck 插件：在实体按键上显示最多 8 个任务的实时卡片（活动、标题、队列、目标、推理强度），支持点击切换本地或固定的远程任务、调整 Effort 等级、切换 Fast 模式、长按任务键语音听写并自动提交跟进。机制上优先使用 Codex 自身 Micro 渲染器事件与内部命令，缺失时回退到 Accessibility 与快捷键路径；仅读取未公开的本地元数据，不写入 Codex 数据库。限制：需 macOS 13+、Stream Deck 7.4+、Stream Deck Neo 设备，Codex 更新可能临时破坏读取路径。

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

- 8 任务实时卡片监控（队列计数、目标徽章、Effort/Fast 状态）
- 长按任务键 0.55s 触发语音听写并自动提交跟进
- 优先使用 Codex 原生内部命令，回退到 Accessibility/快捷键验证路径
- 英语/韩语/俄语本地化，无需单独语言构建

## 适用场景

- 在实体按键上一眼掌握多个 Codex 任务的运行状态
- 不碰鼠标即可切换任务并语音口述跟进指令
- 快速调整推理 Effort 等级与 Fast 模式

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5:  An open-source physical dashboard for Codex on Stream Deck.
> L21: ThreadDeck turns a Stream Deck into a physical Codex task monitor and controller. It is inspired by the compact har

## 星数曲线

```mermaid
xychart-beta
    title "y5862000/threaddeck-for-codex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `2725cdc7407a` · [字段定义](../../DATASET.md)*
