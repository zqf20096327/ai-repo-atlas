# GC-RENCAO/microduck-companion

⭐ 3 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/GC-RENCAO/microduck-companion) · 个人维护 · 中文 README

**为 Pollen Robotics Microduck 提供本地 LLM 陪伴的社区项目**

面向 Pollen Robotics Microduck 机器鸭的社区伴侣程序：通过本地 LLM（Ollama，默认 qwen3.5:9b-mlx）进行中英文对话并用工具调用选取动作，浏览器端用 MediaPipe 处理摄像头手势（挥手、招手、竖拇指等映射为指令），含 10 Hz 情绪/能量行为层与基于 A* 的室内路径规划。当前在官方 MuJoCo 模拟器中运行，真机模式仅通过 Hugging Face rendezvous 通道验证过模拟鸭子，未在物理机器人上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 LLM 工具调用选动作、二次调用角色扮演回答，流式输出
- 浏览器端 MediaPipe 手势识别，画面不离开本机
- 从场景文件生成地图并以 A* 规划穿门绕障路径
- 真机模式默认禁用自主行走，仅执行用户指令

## 适用场景

- 在官方模拟器里与机器鸭对话、挥手互动
- 让鸭子在 3D 公寓场景中自主导航到你身边
- 通过 Hugging Face rendezvous 远程连接自己的鸭子
- 在真机上体验聊天、手势、声音等非行走互动

## 场景标签

`聊天机器人` `目标检测` · 领域:对话与助手

## 证据(README 行号)

> L21: - **Talk to it** — natural language (Chinese or English) through a local LLM in Ollama
> L22:  (default `qwen3.5:9b-mlx`). One call picks the actions (tool calling), a second one answers in character, streamed
> L52: the LLM is a **high-level controller off the robot**, reactive behaviour stays local, and `robotd` keeps motor auth

## 星数曲线

```mermaid
xychart-beta
    title "GC-RENCAO/microduck-companion 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `32be5411dee8` · [字段定义](../../DATASET.md)*
