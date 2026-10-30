# ymrohit/openscenesense-ollama

⭐ 55 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/ymrohit/openscenesense-ollama) · 个人维护

**本地视频理解库：经 Ollama 视觉模型产出摘要与时间线**

Python 库，通过本地 Ollama 视觉模型分析视频：筛选关键帧后送入视觉模型，可选本地 Whisper 转录音频，返回摘要、时间戳事件、帧级发现与 Ollama 性能遥测。默认安装不依赖 Torch/Transformers，音频栈懒加载。要求 Python 3.10+、FFmpeg/FFprobe 与本地可达的 Ollama，不自动拉取模型。提供动态/均匀/全量帧选择、JSON Schema 结构化输出、缓存续跑与并发模式，另有 CLI 入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 动态帧选择（场景变化峰值检测）+ 逐帧选择理由记录
- JSON Schema 结构化输出与 v1.2 共享结果契约
- 可选本地 Whisper 音频转录，音频栈懒加载、默认安装轻量
- 断点续跑缓存与 Ollama 性能遥测记录

## 适用场景

- 在本地私有分析视频内容并生成摘要与时间线事件
- 教育或媒体场景批量处理视频提取关键信息
- 内容审核中获取帧级发现与音频转录

## 场景标签

`图像视频处理` `语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Private, local video understanding through Ollama—with a lightweight default install.
> L5: OpenSceneSense Ollama selects meaningful video frames, sends them to a local vision model, optionally transcribes au

## 星数曲线

```mermaid
xychart-beta
    title "ymrohit/openscenesense-ollama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-30 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8c03f9f57d6e` · [字段定义](../../DATASET.md)*
