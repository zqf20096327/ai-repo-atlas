# eogee/any4any

⭐ 73 · Python · MIT · 推送 2025-11-10 · [GitHub](https://github.com/eogee/any4any) · [官网](https://eogee.com) · 组织维护 · 中文 README

**企业级多模态 AI 平台：LLM 对话、数字人、NL2SQL、语音与知识库**

any4any 是自托管的多模态 AI 系统，集成大语言模型对话（支持 OpenAI、通义千问等兼容 API 接入）、Any4DH 实时数字人（WebRTC/Wav2Lip 唇形同步）、8 步骤 NL2SQL 智能查询（仅允许 SELECT）、基于 BGE+ChromaDB 的向量知识库、双引擎 TTS（EdgeTTS/IndexTTS-1.5）与语音识别，并通过 MCP 协议、钉钉机器人及 OpenAI 兼容 API 对外提供服务。部署需 Python 3.10+、Conda、MySQL 与 FFmpeg，Windows 下需 WSL2；模型文件约需 20GB 存储，通过 git clone 源码方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Any4DH 数字人系统：WebRTC 实时音视频流与 Wav2Lip 唇形同步
- NL2SQL 智能查询：8 步骤工作流、追问识别、多层 SQL 安全验证（仅 SELECT）
- OpenAI 兼容 API：对话/语音合成/语音识别/嵌入/重排端点，可接入模型管理应用
- 知识库系统：BGE-Small-ZH 嵌入 + ChromaDB 向量检索 + 重排序

## 适用场景

- 企业内自建多模态 AI 交互平台，含对话、语音与数字人
- 用自然语言查询业务数据库并生成自然语言回答
- 搭建基于自有文档的知识库问答，并以 OpenAI 兼容 API 供其他应用调用
- 通过 MCP 协议或钉钉机器人接入智能回复

## 场景标签

`数据分析` `语音合成` `文档问答` `语音 Agent` · 领域:效率与自动化

## 证据(README 行号)

> L8: any4any是一个企业级多模态AI系统，提供完整的智能交互解决方案。集成了大语言模型对话、数字人系统、智能SQL查询、语音处理、知识库系统等核心功能，支持OpenAI兼容API接口，可无缝集成到各类AI应用中。
> L14: - **知识库系统**：基于向量检索的智能知识管理和问答
> L15: - **语音处理**：高质量的语音识别和合成
> L23: - **实时数字人交互**：基于WebRTC的实时音视频流处理

## 星数曲线

```mermaid
xychart-beta
    title "eogee/any4any 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 71 --> 74
    line [72, 73, 73]
```

2026-10-18 72 → 2026-10-30 73（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a028a7332a47` · [字段定义](../../DATASET.md)*
