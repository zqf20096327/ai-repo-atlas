# kamwoh/yume

⭐ 25 · GDScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/kamwoh/yume) · [官网](https://github.com/kamwoh/yume/releases/tag/v0.1.0) · 个人维护

**基于 Godot 的可编程显式世界模型引擎，世界以纯 JSON 描述并解释执行**

运行于 Godot 4.6.1 之上的世界模拟引擎：用七个原语（Entity/Tag/Rule/Trigger/Effect/Query/Relation）以纯 JSON 描述世界的实体与规则，固定解释器逐 tick 推进状态，Godot 仅作只读投影层渲染为画面/音频/HUD。仓库由 Claude 编写，推荐通过 Claude Code 以自然语言驱动生成流水线（/yume-design 从散文提案生成完整游戏，/yume-create-scene 生成 3D 场景），也可手写 JSON 或运行内置 Sokoban 等示例，无需 API key。定位为游戏、强化学习/agent 评测测试床与神经世界模型训练数据来源的研究基底。当前为 pre-1.0 实验状态，七原语与 JSON schema 尚未冻结。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 世界状态与转移函数以纯 JSON 表达，固定解释器逐 tick 推进，Godot 只作只读投影
- 七原语词汇表（Entity/Tag/Rule/Trigger/Effect/Query/Relation），引擎不含游戏特定代码
- /yume-design 流水线由 Claude 编排，散文提案端到端生成可玩游戏（含 shooter/racing 等类型专用专家）
- 确定性、可设定种子的 gym 式步进（ADR 0060）与外部 agent IPC 接口（ADR 0020）

## 适用场景

- 用自然语言让 Claude 生成并运行一个小游戏
- 为强化学习与 agent 评测搭建确定性、可复现的环境
- 滚动展开 JSON 世界录制 (state, action, next_state) 轨迹作为神经世界模型训练数据
- 研究 LLM 只生成世界规则（而非引擎代码）的游戏生成路径

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L36: You describe a world in plain English. An LLM writes the JSON. A fixed
> L127: **JSON**, and an LLM (Claude) compiles prose into JSON. The world model is
> L187: > Claude wrote **all of this framework**. The author reviewed the code,

## 星数曲线

```mermaid
xychart-beta
    title "kamwoh/yume 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8a35516835e4` · [字段定义](../../DATASET.md)*
