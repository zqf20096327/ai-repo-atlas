# LiBinZyu/VAI

⭐ 25 · C# · 推送 2026-01-29 · [GitHub](https://github.com/LiBinZyu/VAI) · 个人维护 · 中文 README

**给 Unity 开发者：在项目中实现唤醒词→语音识别→意图匹配→工具调用的语音控制**

面向 Unity 项目的语音控制系统：流水线包含自定义唤醒词检测、阿里云 Paraformer v2 语音转文本、本地 bge-small-zh-v1.5 embedding 意图匹配（中英双语）、通义千问 LLM 生成结构化 JSON tool_call 并自动映射执行 Unity 内注册函数。本地意图匹配可拦截约 80% 调用、降低 LLM 频次与成本。开发者通过 Startup()/Shutdown() 集成，函数在 JSON 注册表中定义。限制：dashscope ASR 仅限中国地区注册；Android 不支持自定义唤醒词与环境变量 API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 唤醒词→ASR→本地意图匹配→LLM tool_call 全流程
- 本地 0.1B embedding（bge-small-zh-v1.5）意图匹配减少 LLM 调用
- LLM 输出自动映射到 JSON 注册的 Unity 函数执行
- Startup()/Shutdown() API 集成到既有 Unity 项目

## 适用场景

- 在 Unity 游戏中用自然语言语音控制场景物体与操作
- 为 Unity 应用加入'唤醒词+指令'的免手操作交互
- 混合本地/云端模式降低语音指令的响应延迟与调用成本

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L12: `VAI (Unity Voice AI Assistant)` is a **lightweight, low-dependency, and API-key based** system for implementing vo
> L21: * **High-Accuracy Multilingual ASR**: Integrates Alibaba Cloud Paraformer v2 for reliable speech-to-text conversion
> L25: * **LLM-Powered High-Accuracy Intent Parsing**: Utilizes Qwen LLM to interpret natural language and convert it into

## 星数曲线

```mermaid
xychart-beta
    title "LiBinZyu/VAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `50ad5fe28b27` · [字段定义](../../DATASET.md)*
