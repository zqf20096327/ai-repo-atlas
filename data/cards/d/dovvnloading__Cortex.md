# dovvnloading/Cortex

⭐ 37 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/dovvnloading/Cortex) · 个人维护

**Windows 本地优先 AI 聊天工作区，本地跑模型不外发数据**

面向 Windows 用户的本地 AI 对话工作区：通过 Ollama 或自带的托管 llama.cpp 运行时加载 GGUF 模型，对话与记忆存于本地 SQLite/JSON。界面为 pywebview/WebView2 内嵌 React/TypeScript 前端，提供模型选择、逐会话生成参数、命令面板、推理与来源披露等。特色机制：模型提出的代码需通过受限 Python 子集验证并经用户一次性批准后才在隔离 worker 中执行；模型下载仅限 https 公网地址。限制：仅 Windows，llama.cpp GPU 后端支持 Vulkan/CPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两种本地运行时：Ollama 或自带托管 llama.cpp（GGUF，二进制经 SHA-256 校验）
- 审批门控的受限 Python 执行：受限子集验证、隔离 worker、时限/内存/网络限制
- 逐会话覆盖生成参数，响应附 token 计数与 tokens/sec
- 数据本地存储：线程存 SQLite，记忆存本地 JSON，API 绑定 loopback

## 适用场景

- 在 Windows 上与本地模型对话且数据不出机器
- 用自有 GGUF 文件或从 Hugging Face 下载模型进行本地聊天
- 让模型在受控沙箱中执行已批准的计算任务

## 场景标签

`聊天机器人` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Cortex is a local-first AI workspace for Windows. It runs models on the machine
> L4: -- either through Ollama or by loading a local `.gguf` file with its own managed
> L77: - **Local chat.** Stream responses from a local model with Markdown,

## 星数曲线

```mermaid
xychart-beta
    title "dovvnloading/Cortex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `68c8334a9bb5` · [字段定义](../../DATASET.md)*
