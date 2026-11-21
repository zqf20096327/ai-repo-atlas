# hrabanazviking/WYRD-Protocol-World-Yielding-Real-time-Data-AI-world-model

⭐ 10 · Python · 推送 2026-11-18 · [GitHub](https://github.com/hrabanazviking/WYRD-Protocol-World-Yielding-Real-time-Data-AI-world-model) · 个人维护

**给 AI 角色提供确定性世界状态的外部世界模型协议**

以 Python 实现的确定性世界模型架构：将 LLM 上下文窗口之外的世界状态置于 ECS（实体-组件-系统）中，通过只读的 Passive Oracle 向 LLM 提供 WorldContextPacket 结构化快照，含 Yggdrasil 空间层级、Bifrost 引擎桥接抽象与六种记忆存储（wyrdforge）。面向 AI 游戏、沉浸式 RPG 与自主角色系统开发者，支持与 Unity、Unreal、SillyTavern 等平台集成。1.5.0 版本报告 2,284 项测试通过。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 只读 Oracle 输出 WorldContextPacket 结构化世界快照，不调用 LLM
- Yggdrasil 空间层级与 PositionComponent 半径/最近/距离查询
- BifrostBridge 统一契约对接 Unity、OpenSim、CryEngine、O3DE 等引擎适配器
- wyrdforge 六种记忆存储（Hugin/Munin/Mimir/Wyrd/Orlog/Seidr）

## 适用场景

- 为 AI 驱动的 RPG 角色维护持久一致的世界状态
- 在 VR 或 3D 引擎中接入确定性世界数据层
- 构建需要环境追踪外置以减少幻觉的 AI 角色系统

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L63: * **Passive Oracle Model** — The Oracle is **read-only**. It reports ground truth — it never decides, never writes,
> L64: * **ECS Entity-Component System** — World state lives in typed components attached to entities. The LLM receives a 
> L66: * **Bifrost Bridge Abstraction** — All engine adapters implement the same `BifrostBridge` ABC — ensuring every inte


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `fee9a1c9b8ff` · [字段定义](../../DATASET.md)*
