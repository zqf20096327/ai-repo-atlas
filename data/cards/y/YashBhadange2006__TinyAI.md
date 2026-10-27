# YashBhadange2006/TinyAI

⭐ 46 · Kotlin · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/YashBhadange2006/TinyAI) · 个人维护

**Android 端本地 LLM 聊天应用，完全离线推理**

面向终端用户的 Android 应用：通过 MediaPipe GenAI 与 LiteRT-LM 两个本地推理引擎在设备 CPU/GPU 上运行大语言模型，无需 API key 与服务器，模型下载后可完全离线对话。支持 .task 与 .litertlm 格式（不支持 GGUF），可从 Hugging Face 浏览下载模型，具备视觉提示、推理模型 <think> 块分离展示、流式生成、多会话历史与 Markdown/LaTeX 渲染。要求 Android 7.0+，模型体积约 600 MB–2.6 GB。提供 Google Play 安装与源码构建两种途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双本地推理引擎（MediaPipe GenAI / LiteRT-LM）自动选择运行时
- CPU/GPU 后端切换，按模型记忆
- Hugging Face 模型浏览下载与内置精选列表
- 推理模型 <think> 块流式分离展示

## 适用场景

- 在手机上离线与本地 LLM 对话，数据不出设备
- 加载视觉模型进行图文对话
- 运行 DeepSeek-R1、Qwen3 等推理模型并查看思考过程

## 场景标签

`聊天机器人` `多模态` · 领域:对话与助手

## 证据(README 行号)

> L11: **TinyAI** is an Android app for running large language models entirely on-device. No API keys, no servers, no data
> L13: It runs on two local inference engines (Google's MediaPipe GenAI and LiteRT-LM), lets you pull additional compatibl

## 星数曲线

```mermaid
xychart-beta
    title "YashBhadange2006/TinyAI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-27 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d0aed647e809` · [字段定义](../../DATASET.md)*
