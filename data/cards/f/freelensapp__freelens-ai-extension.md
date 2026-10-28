# freelensapp/freelens-ai-extension

⭐ 37 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/freelensapp/freelens-ai-extension) · [官网](https://freelens.app/) · 组织维护

**Freelens 的 Kubernetes AI 助手扩展：自然语言读写集群**

Freelens（Kubernetes 桌面客户端）的 AI 扩展：以聊天形式用自然语言查询、解释并在用户批准后修改 Kubernetes 资源。本体是 LLM API 客户端，自身不运行模型；agent 逻辑（LangGraph supervisor、集群工具、结构化输出、human-in-the-loop 审批）在 Freelens 主进程内运行，仅模型推理委托给 provider。当前仅内置 OpenAI provider（基于 OpenAI 兼容 Chat Completions API），Google/Gemini 暂时禁用；可通过 LiteLLM 等网关或 Ollama（本地 11434 端点）接入其他模型，模型须支持 tool calling。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意资源类型（含 CRD）的 list/get/create/update/patch/delete 集群工具操作
- 每次变更需用户审批，变更前展示当前状态备份
- DeepSeek/Qwen 等 thinking 模型的 DSML tool-call 与 tool_choice 特殊处理
- 本地 Ollama 直连（无需网关），含 token 计数与会话自动压缩

## 适用场景

- 在 Kubernetes 管理界面里用对话查询和解释集群资源
- 让 AI 代为执行扩缩容、重启等操作并逐项审批
- 通过 LiteLLM 网关或本地 Ollama 使用自选模型管理集群

## 场景标签

`AI 助手` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L78: Freelens AI is a **client of a large language model API**. It does not run a
> L212: Talk to your cluster in natural language. The agent reads, explains, and (with

## 星数曲线

```mermaid
xychart-beta
    title "freelensapp/freelens-ai-extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5150988f25b4` · [字段定义](../../DATASET.md)*
