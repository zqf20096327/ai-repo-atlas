# kimhyeri/FoundationModelsPlayground

⭐ 14 · Swift · MIT · 推送 2026-03-11 · [GitHub](https://github.com/kimhyeri/FoundationModelsPlayground) · 个人维护

**Apple FoundationModels 框架的端侧 AI 示例应用集合（6 个 Demo）**

面向开发者的示例工程合集，基于 Apple 官方 FoundationModels 框架与 SystemLanguageModel 构建六个端侧应用：聊天机器人、英语语法纠错、菜谱生成、健身计划生成、面向儿童的安抚故事生成（含 AVSpeechSynthesizer 语音播放）以及结合自定义天气 Tool 的穿搭建议。各示例演示文本生成、流式输出、结构化输出与自定义 Tool 调用等能力，全部在设备本地运行，不依赖云端推理。README 未给出安装运行命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个基于 SystemLanguageModel 的端侧示例应用
- 演示流式输出、结构化结果与自定义 Tool（get_weather）调用
- CozyTales 集成 AVSpeechSynthesizer 实时语音播放
- 所有示例 100% 本地运行，无需网络

## 适用场景

- 学习 Apple FoundationModels 框架的接入方式与能力边界
- 参考自定义 Tool 调用与结构化输出的实现写法
- 基于示例改造出自己的端侧 AI 应用

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L2: A collection of on-device examples using Apple’s FoundationModels framework
> L8: > ✅ Powered by `SystemLanguageModel`
> L67: FoundationModels is Apple’s official framework for running foundation language models on-device.

## 星数曲线

```mermaid
xychart-beta
    title "kimhyeri/FoundationModelsPlayground 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `d8651aca43cc` · [字段定义](../../DATASET.md)*
