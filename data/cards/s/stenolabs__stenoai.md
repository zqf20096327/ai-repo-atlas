# stenolabs/stenoai

⭐ 1,394 · Python · MIT · 推送 2026-11-22 · [GitHub](https://github.com/stenolabs/stenoai) · [官网](https://stenoai.co/) · 组织维护

**面向机密会议的本地 AI 记事本与会议记录工具**

隐私优先的桌面端 AI 会议记事本，默认在本机完成录音转写、摘要与问答：实时转写用 Parakeet TDT v3（Apple Silicon/MLX），录音结束后 Whisper 支持最多 99 种语言；摘要与聊天经 Ollama 运行 Gemma、Qwen、gpt-oss 等本地模型。提供说话人分离、自动检测会议、系统音频采集、Markdown 导出与报告模板。云模型（OpenAI/Anthropic/Bedrock/自定义端点）与云转写为可选并需确认。Windows 处于 alpha，macOS 需 Apple Silicon 与 macOS 14.4+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 默认本地 AI：录音、转写、摘要、问答均在设备上处理
- Parakeet 实时转写 25 种欧洲语言，Whisper 支持总计 99 种语言
- /steno agent 技能让 Claude Code/Codex 读取本地笔记并跨会议问答
- 可选云模型：OpenAI、Anthropic、AWS Bedrock 或自定义端点

## 适用场景

- 政府与国防等场景下对机密会议做本地转写与摘要
- 自动检测会议开始并录制、生成会议纪要
- 通过提问检索和汇总跨多次会议的笔记与行动项
- 从 Granola 迁移并同步既有会议笔记

## 场景标签

`知识库管理` `语音识别` · 领域:知识与检索

## 证据(README 行号)

> L15:  StenographAI is a privacy-first AI notepad for confidential conversations. Record, summarise, and query meetings w
> L42: - **Privacy-first**: local AI processes your recordings, transcripts, and summaries on your device. External AI pro
> L165: - `Parakeet TDT v3` (572 MB): Highest quality, supports live transcription, 25 European languages (English, Spanis

## 星数曲线

```mermaid
xychart-beta
    title "stenolabs/stenoai 星数(近 25 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-25", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 1338 --> 1399
    line [1343, 1344, 1347, 1348, 1349, 1350, 1349, 1350, 1351, 1353, 1355, 1348, 1356, 1357, 1358, 1377, 1378, 1381, 1383, 1388, 1390, 1391, 1392, 1393, 1394]
```

2026-10-21 1,343 → 2026-11-23 1,394（+51）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `e51242b2ee44` · [字段定义](../../DATASET.md)*
