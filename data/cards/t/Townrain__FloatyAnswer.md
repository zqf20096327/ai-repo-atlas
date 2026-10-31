# Townrain/FloatyAnswer

⭐ 14 · Kotlin · AGPL-3.0 · 推送 2026-09-18 · [GitHub](https://github.com/Townrain/FloatyAnswer) · 个人维护 · 中文 README

**安卓悬浮窗截图答题工具：OCR/视觉模型识别题目，LLM 给出答案**

基于 OCR/视觉模型与大语言模型的 Android 答题应用（Fork 自 wb-hwang/AIAnswerer-Android 并独立发展）。通过悬浮球截屏或无障碍读屏采集题目，经本地 ML Kit OCR 或云端 VLM 识别文字，再调用 DeepSeek 等兼容 OpenAI 接口的 LLM 生成答案，支持选择/填空/问答题型、批量录制答题、并行处理与 LLM 工具调用模式的联网搜索。用户提供自己的 API Key，配置保存于本地加密存储。以 APK 形式安装，需 Android 10 及以上系统。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 截图/读屏/录制/多图四种采集答题模式
- 本地 ML Kit OCR + VLM 视觉模型降级识别
- 内置 50+ 厂商预设的 OpenAI 兼容接口配置
- 支持 10 家搜索供应商的 LLM 工具调用联网搜索

## 适用场景

- 练习或自测时悬浮窗快速截题获取解析
- 一页多题的批量录制答题
- 含图或噪音较多的题目用视觉模型识别

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L16: FloatyAnswer 是一款基于 OCR/视觉模型与大语言模型的安卓答题工具。通过悬浮窗截图识别题目，并调用 DeepSeek AI 等兼容 OpenAI 接口的模型为你快速给出答案，适用于练习、查缺补漏或自测场景。
> L37: │ 悬浮球    │──▶│ 采集：截图 / 读屏  │──▶│ OCR / VLM    │──▶│ LLM 答题+联网  │──▶│ 答案卡片  │

## 星数曲线

```mermaid
xychart-beta
    title "Townrain/FloatyAnswer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `47348221a3ac` · [字段定义](../../DATASET.md)*
