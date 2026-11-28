# Niruthiya04/echomind-voice-assistant

⭐ 16 · HTML · 推送 2026-11-27 · [GitHub](https://github.com/Niruthiya04/echomind-voice-assistant) · 个人维护

**本地优先的语音转录与 RAG 记忆问答桌面助手**

本地运行的桌面应用：实时捕获语音并流式转录，将定稿文本切片、用本地嵌入模型索引到 SQLite 向量记忆库，再通过检索增强聊天接口回答问题，答案引用所依据的转录片段并可回溯到录制时间。默认路径全部本地推理（ASR、嵌入、GGUF 聊天模型），无嵌入模型时提供确定性词法回退；可选云端语音处理仅在用户提供凭据后启用。提供 PowerShell 安装脚本与 Docker 部署方式，当前参考运行环境为 Apple Silicon macOS，Windows/Linux 标注为 planned。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时本地 ASR 流式转录，定稿段落带时间戳写入 SQLite 记忆库
- 检索增强聊天答案引用转录出处，无相关内容时报告而非编造
- 可插拔本地模型后端：Whisper 系转录、本地嵌入、GGUF 聊天模型
- 无嵌入模型时的确定性词法回退保证检索可用

## 适用场景

- 把会议/讲座内容录成可检索的语音记忆库
- 对本人的历史发言用自然语言提问并获得带出处回答
- 需要离线运行且语音数据不出本地的转录与问答

## 场景标签

`聊天机器人` `RAG` `语音识别` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L7: EchoMind Voice Assistant is a local-first desktop application that captures spoken input, transcribes it in real tim
> L44: **3. Memory indexing.** Finalized transcript segments are chunked, embedded with a local embedding model, and writt
> L46: **4. Retrieval-augmented chat.** When you ask a question, EchoMind embeds the query, retrieves the most relevant tr


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `617a4d0e6021` · [字段定义](../../DATASET.md)*
