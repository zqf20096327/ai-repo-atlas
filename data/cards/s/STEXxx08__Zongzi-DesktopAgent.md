# STEXxx08/Zongzi-DesktopAgent

⭐ 5 · Python · NOASSERTION · 推送 2026-11-20 · [GitHub](https://github.com/STEXxx08/Zongzi-DesktopAgent) · [官网](https://space.bilibili.com/35778513) · 个人维护 · 中文 README

**桌面 AI 陪伴客户端与可替换组件的 Agent 集成框架**

由 Bot 与 Core 两部分组成：Bot 是 PySide6 桌宠客户端（纯 CPU），负责对话编排、语音与屏幕感知、自研四层长期记忆、工具/Skills/MCP 运行时；Core 把 ASR/LLM/MLLM/TTS/OCR 等封装为统一 HTTP 服务，可本机或跨机部署。本地模型与云端 API 可自由混搭，零显卡可用云端 API 打字聊天。面向想拥有桌面 AI 伙伴的个人用户与二次开发者；人设立绘可整体替换，兼作组件解耦的集成框架。安装需 Miniconda 多环境与 pip 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- Bot/Core HTTP 解耦架构，模型服务跨机部署，model_id 无白名单限制
- 全链路流式语音：流式 ASR→LLM 分句→流式 TTS，TurnSense ONNX 语义断点检测
- 四层长期记忆：快照抽取、离线合并、BGE ONNX 向量检索召回
- 兼容 SKILL.md 的 Skills 框架、HTTP MCP 客户端、内置联网检索与文件沙箱

## 适用场景

- 在桌面上拥有可听可看可对话的 AI 陪伴角色
- 零显卡环境下用云端 API 快速跑通打字聊天
- 替换人设与立绘做自己的桌宠 Agent
- 本地部署 ASR+TTS 做低延迟语音对话

## 场景标签

`AI 助手` `语音 Agent` `Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6: **一个跑在自己电脑上的 AI 桌面伙伴，也是一个组件全可替换的桌面 Agent 集成框架。**
> L10: **她叫「粽子」**——一位能驻留在你桌面上的 AI 伙伴（默认人设是有猫耳和猫尾的猫娘）：**听得见你说话、看得见你屏幕上在发生什么、记得住你们聊过的内容，还能自己调工具帮你查资料干活**。无论是陪你打游戏、看视频，还是顺手查天
> L12: 把「粽子」的人设与立绘换掉，它本身是一套**高自由度、全组件解耦的桌面 Agent 框架**：

## 星数曲线

```mermaid
xychart-beta
    title "STEXxx08/Zongzi-DesktopAgent 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-10-23 5 → 2026-11-25 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `27064890399d` · [字段定义](../../DATASET.md)*
