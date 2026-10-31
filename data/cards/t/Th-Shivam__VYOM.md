# Th-Shivam/VYOM

⭐ 34 · Python · MIT · 推送 2026-09-02 · [GitHub](https://github.com/Th-Shivam/VYOM) · 个人维护

**J.A.R.V.I.S. 风格的语音/文字 AI 个人助手桌面应用**

Python 编写的桌面个人助手，受钢铁侠 J.A.R.VIS. 启发：通过语音唤醒词或文字指令接受命令，调用 Groq/Cohere 的语言模型处理对话，结合浏览器自动化执行任务。采用多线程模块化架构，将监听、API 调用与系统任务执行分置不同线程以保持常听不卡顿。功能模块含图像生成、实时搜索、语音转文字、文字转语音与系统自动化；需配置 API key，Linux/macOS 需额外安装 portaudio、espeak 等系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音唤醒 + 文字指令双通道输入
- 多线程架构分离监听/处理/执行，维持 Always Listening
- 调用 Groq/Cohere 模型，含图像生成与实时搜索模块
- 语音转文字与文字转语音（SpeechToText/TextToSpeech）

## 适用场景

- 用语音命令操作电脑完成系统任务与自动化流程
- 作为桌面对话助手进行问答与图像生成
- 通过实时搜索模块查询网络信息

## 场景标签

`AI 助手` `语音 Agent` `浏览器自动化` `图像生成` · 领域:效率与自动化

## 证据(README 行号)

> L10: **🚀 A Futuristic AI-Powered Personal Assistant Inspired by J.A.R.V.I.S.**
> L29: * **Thread 2 (Processor):** Handles API calls to Groq/Cohere without blocking the listener.

## 星数曲线

```mermaid
xychart-beta
    title "Th-Shivam/VYOM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `262f67083e51` · [字段定义](../../DATASET.md)*
