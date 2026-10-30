# AbdullahHendy/live-translation

⭐ 17 · Python · MIT · 推送 2026-05-30 · [GitHub](https://github.com/AbdullahHendy/live-translation) · 个人维护

**实时语音转写与翻译的服务器–客户端系统**

基于模块化服务器–客户端架构的实时语音转写翻译系统：客户端经 PyAudio 采集音频，通过全双工 WebSocket 以 Opus 或 raw PCM 流式发送到服务器；服务器用 Silero 做语音活动检测、Whisper 做转写、Helsinki-NLP OpusMT 做翻译，返回带时间戳的 JSON 结构。提供 CLI（live-translate-server/client）与异步 Python API，另有 Node.js/浏览器/C#/Go/Kotlin 客户端示例。README 声明其定位是构建实时翻译体验的基础组件而非即插即用应用。Linux/macOS 需安装 PortAudio 等系统依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全双工 WebSocket 流式音频传输，支持 Opus 编码降低带宽
- Silero VAD + Whisper 转写 + OpusMT 翻译的处理管线
- CLI 与异步 Python API 两种使用方式
- 非 Python 客户端可按 WebSocket 协议（16kHz int16 单声道分块）直接接入

## 适用场景

- 为自有应用搭建实时转写/翻译后端
- 通过浏览器或移动端客户端做实时字幕与翻译
- 用 Python API 把实时翻译嵌入更大系统

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L71: - Speech-to-text transcription using OpenAI's **Whisper**
> L72: - Translation of transcriptions using Helsinki-NLP's **OpusMT**
> L226: - **Receive**: structured ***JSON*** messages with timestamp, transcription and translation fields

## 星数曲线

```mermaid
xychart-beta
    title "AbdullahHendy/live-translation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e17a5b287e99` · [字段定义](../../DATASET.md)*
