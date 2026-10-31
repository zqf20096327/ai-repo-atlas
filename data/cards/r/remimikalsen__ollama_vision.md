# remimikalsen/ollama_vision

⭐ 22 · Python · MIT · 推送 2026-10-04 · [GitHub](https://github.com/remimikalsen/ollama_vision) · 个人维护

**Home Assistant 集成：用本地 Ollama 视觉模型分析图片**

面向 Home Assistant 用户的自定义集成：调用本地 Ollama 服务器上的视觉模型分析图片（HTTP/HTTPS、config 目录本地文件、Frigate、Google Nest 门铃等来源），生成或更新描述传感器，并触发事件供下游自动化使用；可选接入第二个文本模型对视觉描述做润色。通过 HACS 安装，支持多服务器、自定义 prompt 与 keep-alive 配置。注意：动态传感器在 Home Assistant 重启后会显示 unavailable。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用本地 Ollama 视觉模型分析图片并生成动态描述传感器
- 可选第二个文本模型增强描述
- 分析完成时触发 ollama_vision_image_analyzed 事件供下游自动化
- 支持多 Ollama 服务器与多配置实例

## 适用场景

- 门铃或监控检测到人时，让本地视觉模型生成描述并推送到手机
- 在自动化中对 Frigate 等来源的图片做 AI 分析
- 用自定义 prompt 让模型读取车牌等特定目标

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L9: This integration enables you to analyze images using a local Ollama server running a vision-enabled LLM. Optionally,
> L22:  - You must have access to a vision-enabled model running on an Ollama server.
> L80: You can queue images for analysis via the `ollama_vision.analyze_image` service. When called, it generates or updat

## 星数曲线

```mermaid
xychart-beta
    title "remimikalsen/ollama_vision 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `04955bb5832f` · [字段定义](../../DATASET.md)*
