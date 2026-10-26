# google-marketing-solutions/ariel

⭐ 66 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/google-marketing-solutions/ariel) · [官网](https://github.com/google-marketing-solutions/ariel) · 组织维护

**广告视频 AI 配音翻译工具：上传视频生成多语言配音**

Google gTech 出品的视频语音翻译重配音工具：通过 Web 界面上传视频，用 audio-separator（默认 BS-RoFormer）分离人声与背景音，调用 Gemini 模型完成转写、翻译与 TTS 配音，支持多说话人声音选择、语速匹配、时间线与逐句译文编辑。部署在 Google Cloud（Vertex AI、Cloud Storage、Cloud Run、IAP），由 setup.sh/deploy.sh 脚本自动化配置，也可 run_locally.sh 本地运行。数据仅经 Gemini 全球区域处理，严格数据驻留需求需自行改造。

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

- 人声/背景音分离（BS-RoFormer 等多种可选模型）
- Gemini Pro/Flash 可切换，支持自定义翻译与配音指令
- 逐句译文编辑、时间线拖拽、语速自动匹配
- setup.sh/deploy.sh 一键部署到 Cloud Run，亦可本地运行

## 适用场景

- 为数字广告视频制作多语言配音版本
- 编辑与校正 AI 生成的翻译和语音时间轴
- 在 Google Cloud 上部署供团队通过 IAP 访问使用

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L10: Ariel is a tool for translating video voice tracks. It provides an easy to use
> L127: Ariel is initially deployed to use the most recent, generally available Gemini model as of the last update to the 
> L137: Ariel uses `audio-separator` to split the original video's audio into vocals (speech) and background (music and so

## 星数曲线

```mermaid
xychart-beta
    title "google-marketing-solutions/ariel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-26 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4472f55b3768` · [字段定义](../../DATASET.md)*
