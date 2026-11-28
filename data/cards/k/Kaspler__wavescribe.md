# Kaspler/wavescribe

⭐ 5 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/Kaspler/wavescribe) · 个人维护

**给需要收听广播的用户：离线转写翻译电台内容并可告警**

运行在 Apple Silicon Mac 上的本地语音工具：同时跟随多个电台（互联网电台或经 RTL-SDR 接收器的 FM 等），将语音转写为文本并翻译，全部内容可搜索；支持关键词、正则与自然语言规则的告警，可通过 webhook、JSON feed 与 MCP server 供自动化系统或 AI agent 使用。全部处理在本机完成，无云服务与账号。为早期 alpha，作者声明不可作为安全系统。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 多电台同时转写与翻译，25 种欧洲语言（默认模型）
- 关键词、regex 与 LLM 规则三类告警，支持 webhook 与 macOS 通知
- MCP server 与 /feed/v1 文本feed 供 agent 与其他程序读取
- FM 频段扫描、RDS 站名识别与频谱调谐

## 适用场景

- 不懂当地语言时阅读本地新闻与官方广播并收到告警
- 记者或 OSINT 分析员跟踪多语言电台并检索问答
- 为聋哑及听障人士以文字逐句呈现电台内容
- 无网络环境下（船只/露营）依靠接收器离线收听转写

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L6: and with FM and other radio through an inexpensive RTL-SDR receiver. Everything runs on your Mac,
> L14: Early alpha, for macOS on Apple Silicon.
> L145: - Transcribes speech in 25 European


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `843c9ece4a23` · [字段定义](../../DATASET.md)*
