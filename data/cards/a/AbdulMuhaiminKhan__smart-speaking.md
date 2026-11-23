# AbdulMuhaiminKhan/smart-speaking

⭐ 3 · Python · 推送 2026-11-14 · [GitHub](https://github.com/AbdulMuhaiminKhan/smart-speaking) · 个人维护

**本地运行的免费 AI 演讲教练：录制演讲并给出多维反馈**

录制演讲后生成报告，覆盖语速、停顿、填充词、声音、眼神接触与姿势，并在时间轴上标注问题发生的时刻，附练习建议。架构为 React 前端 + FastAPI 后端，模型全部本地运行：faster-whisper 做转录与填充词计数，MediaPipe 做姿态/面部/手势追踪，wav2vec2 做语音情感与音素识别，Ollama 运行 qwen2.5:7b 生成教练文本（不可用时回退到内置文本）。支持 Docker 部署或原生开发方式，支持英语、德语、乌尔都语三种界面语言，数据不出本机。发音检查仅覆盖英语与德语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七种练习模式（自由演讲、限时 pitch、即兴、电梯演讲、面试问答、Table Topics 等）
- 演讲回放绘制为五线谱形式，每个问题标注在对应类别的谱线上
- faster-whisper + MediaPipe + wav2vec2 + Ollama 全部本地运行，无 API key 与云端账户
- 支持英语/德语/乌尔都语三语界面与 PDF 报告导出

## 适用场景

- 练习公开演讲并获得语速、填充词、眼神与姿势的逐时刻反馈
- 脱稿排练讲稿并回看遗漏或改动的段落
- 追踪长期练习趋势、目标与成就

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L1: SmartSpeaking: a free, private AI public speaking coach
> L5:  with drills to fix it. Everything runs on your own computer, with free open-source models.
> L10:  Stack: React, FastAPI, Whisper, MediaPipe, Ollama


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `38ff046f28fd` · [字段定义](../../DATASET.md)*
