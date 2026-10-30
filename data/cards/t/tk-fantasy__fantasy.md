# tk-fantasy/fantasy

⭐ 16 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/tk-fantasy/fantasy) · 个人维护 · 中文 README

**接入 Home Assistant 的智能家居 AI 管家应用**

Aether 是面向家庭用户的智能家居 AI 管家：通过自然语言对话控制 Home Assistant 接入的设备，支持多路 RTSP/USB 摄像头的视觉感知与运动检测触发推理、自然语言生成 cron 定时任务与条件自动化规则、基于 faiss 向量检索的 RAG 语义知识图谱（3D 可视化）。对话/视觉/嵌入模型可分别配置不同供应商（OpenAI、Claude、DeepSeek 等），每账号独立 Key。以 Docker Compose 四服务（应用、HA、Mosquitto、模拟器）部署，自带 11 个虚拟演示设备；远程访问推荐 Tailscale。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言控制 Home Assistant 设备，调用前走 verify_action 只读校验
- 多路 RTSP/USB 摄像头视觉感知，运动检测触发推理与按路配置关注项
- 自然语言生成 cron 定时任务与多条件自动化规则
- faiss 向量检索 + 实体共现构图的 RAG 语义知识图谱，3D 可视化
- MCP 工具生态：内置天气/搜索/设备控制工具，可接外部 MCP Server

## 适用场景

- 用一句话控制灯光、空调、窗帘等智能家居设备
- 让 AI 监控摄像头画面，出现关注对象时主动通知
- 通过自然语言创建定时任务和条件联动自动化
- 家庭知识文档向量化检索与 3D 语义图谱浏览

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: **接入大模型的智能家居 AI 管家**
> L22: Aether 的核心交互界面。输入自然语言即可控制家中设备——"把客厅灯关掉"、"空调调到 26 度"，AI 会理解你的意图并执行操作。左侧聊天区域支持多轮对话，快捷斜杠命令帮你快速跳转到设备管理、定时任务等功能。
> L88: - **🧠 AI 对话控制设备** —— 对接 Home Assistant，自然语言开灯 / 调空调 / 拉窗帘，调用前先走 `verify_action` 只读校验

## 星数曲线

```mermaid
xychart-beta
    title "tk-fantasy/fantasy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `931ac555aa52` · [字段定义](../../DATASET.md)*
