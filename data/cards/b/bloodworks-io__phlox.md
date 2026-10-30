# bloodworks-io/phlox

⭐ 109 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/bloodworks-io/phlox) · [官网](https://phlox.bloodworks.io) · 组织维护

**面向临床医生的本地优先 AI 医疗速记与患者管理系统**

开源 AI 医疗速记（scribe）应用，本地运行于自有硬件，数据不出本机（静态加密、默认无遥测）。功能包括环境音自动生成结构化病历笔记、实时 Live Agent 边问诊边起草、多语言转录、患者信函与表单生成、基于本地知识库的 AI 助手、MCP 服务器扩展与临床任务清单。架构为 React/FastAPI/SQLCipher/sqlite-vec/Tauri，桌面版捆绑 llama.cpp 与 parakeet.cpp 推理引擎，Docker 版需自备 OpenAI 兼容端点。明确声明非认证医疗器械，输出须医生复核，合规性取决于部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 环境音逐句转录并按模板字段生成结构化笔记（JSON 约束 + 风格精炼）
- Live Agent 模式：端上 VAD 分段 + 单 token 分类（NOTE/ACT/SKIP）实时起草
- 桌面版捆绑 llama.cpp LLM 与 parakeet.cpp 转录引擎，模型应用内下载
- 支持 MCP 外部工具服务器接入本地知识库 agent

## 适用场景

- 诊疗过程中自动生成病历笔记与患者信函，替代 SaaS 医疗速记服务
- 在自有硬件上本地保存患者数据以满足隐私要求
- 通过本地知识库 agent 检索医学文献辅助诊疗

## 场景标签

`语音识别` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L13: Phlox is a free, open-source, AI scribe with a built-in patient management system and agentic AI capabilities. It's
> L18: - **🌍 Multilingual:** Transcribe and generate notes and letters in multiple languages.
> L20: - **⚡ Live Agent:** Drafts the note in realtime while you consult.

## 星数曲线

```mermaid
xychart-beta
    title "bloodworks-io/phlox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-18 109 → 2026-10-30 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8eb4f0294d9f` · [字段定义](../../DATASET.md)*
