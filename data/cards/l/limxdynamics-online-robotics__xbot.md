# limxdynamics-online-robotics/xbot

⭐ — · [GitHub]() · 组织维护

**人形机器人 AI 网红直播的控制平面运行时**

LimX Dynamics 开源的 24 小时直播主播 XBot 的控制平面：管理约每日四万次控制步骤的执行，每个步骤包含预算声明、评论拉取、身份与记忆解析、草稿生成、评估器链（sql_guard、json_schema、budget、LLM-as-judge 等 8 类）、语音合成与遥测写入。控制面仅绑定 loopback，模型与上行链路在远端；步骤为持久化行，重启后可恢复。提供 Python 与 TypeScript SDK，Apache-2.0 许可。README 未给出机器人本体硬件的构建或购买信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预算化控制步骤引擎：超时被杀并释放槽位，决策本地完成
- 8 类评估器链在输出进编码器前返回判定与原因字符串
- Python/TypeScript 双 SDK，@control 装饰器声明式绑定预算与策略
- 可插拔遥测 sink（OTLP/JSONL），trace 跨 GrokBot 交接保留

## 适用场景

- 搭建 24 小时不停播的 AI 直播间并自动回应评论
- 为长时运行的 LLM agent 加预算、评估与遥测护栏
- 用 SDK 声明式定义带超时与降级策略的控制步骤

## 场景标签

`语音合成` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: This repository is the control plane that keeps it on the air.
> L39: It is a control step: open a budget, pull the comment, resolve identity and conversation memory, draft against the 
> L64: |**Grok core**|Personality, reasoning, tool use, long-horizon memory. The same model family the platform runs on.|`


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `1720d7b082a2` · [字段定义](../../DATASET.md)*
