# deepanwadhwa/samosa-chat

⭐ 55 · JavaScript · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/deepanwadhwa/samosa-chat) · 个人维护

**本地大模型聊天应用与 HTTP 网关：私有运行 Qwen 等模型**

本地优先的模型应用与 HTTP 网关：通过浏览器界面或终端命令从经过校验的目录下载、验证并加载模型（Qwen3.6 35B A3B、Maple、Bonsai、Ornith 等），在 16 GB 内存机器上运行大模型。提供图像/PDF 经本地 OCR 与视觉专家的自动路由、无需 API key 的联网搜索、Chutni 文件夹记忆、对话压缩与最长 262K 的硬件感知上下文分配，以及 OpenAI 兼容的本地网关 API。macOS/Linux 需从源码构建安装，终端对话仅限 Qwen 后端，多模型功能需源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 GB 内存机器上经 SSD 专家流式加载运行 Qwen3.6 35B A3B
- 可恢复且经 SHA-256 校验的模型下载，支持目录与终端拉取
- 硬件感知上下文分配（最高 262,144 tokens）与自动对话压缩
- OpenAI 兼容本地网关 API 与免 API key 联网搜索

## 适用场景

- 在 16 GB 内存的 Mac 上本地运行大型 MoE 模型聊天
- 不依赖云账号与遥测的私有本地模型对话与文档问答
- 通过 OpenAI 兼容 API 为本机应用提供模型服务

## 场景标签

`聊天机器人` `文档问答` `OCR` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L11: Samosa is a local model application and HTTP gateway. Models can be downloaded, verified, and loaded directly throu
> L233: |`POST /v1/chat/completions`|OpenAI-compatible chat completions|

## 星数曲线

```mermaid
xychart-beta
    title "deepanwadhwa/samosa-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-31 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `309624bf5973` · [字段定义](../../DATASET.md)*
