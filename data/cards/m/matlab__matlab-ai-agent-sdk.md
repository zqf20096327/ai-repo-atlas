# matlab/matlab-ai-agent-sdk

⭐ 57 · MATLAB · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/matlab/matlab-ai-agent-sdk) · [官网](https://www.mathworks.com/matlabcentral/discussions/ai/) · 组织维护

**MATLAB 中构建与运行 AI agent 的 SDK**

MathWorks 官方的 MATLAB 附加工具，用于在 MATLAB 环境中构建和运行 AI agent：通过 aisdk.LLMClient 连接 OpenAI Chat Completions/Responses API、Ollama 或任意 OpenAI 兼容 API，用 aisdk.AIAgent 创建带系统提示与工具调用的 agent。支持将 MATLAB 函数封装为 LLM 工具，可经 agent workspace 在本地处理大规模数值数据以节省 token，并支持 MCP 服务器连接与多子 agent 编排。要求 MATLAB R2023a 或更新版本；官方声明为 Research Preview，API 可能变化，且不合并外部 pull requests。提供 MATLAB Online 与 git clone 两种使用方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 OpenAI Chat Completions/Responses、Ollama 及 OpenAI 兼容 API 作为 LLM 后端
- 将 MATLAB 函数封装为 LLM 工具（LLMTool/LocalLLMTool/MCPTool）
- agent workspace 机制：数值数据留在本地工作区，仅传递自然语言观察结果以节省 token
- 支持 MCP 服务器工具与多子 agent 编排

## 适用场景

- 在 MATLAB 工作流中嵌入 LLM 对话与工具调用
- 让 agent 调用 MATLAB 数值计算函数（如特征值、多项式拟合）处理数据
- 通过 MCP 服务器为 agent 扩展外部工具
- 对文本数据做分类、信息抽取与图像标注

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: MATLAB® AI Agent SDK lets you build and run AI agents in MATLAB.
> L7: - Create agents based on OpenAI® Chat Completions API, OpenAI Responses API, Ollama™, or OpenAI-compatible APIs.
> L214: |aisdk.LLMClient|Connect to third-party LLM API|

## 星数曲线

```mermaid
xychart-beta
    title "matlab/matlab-ai-agent-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-28 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3e8c6d6e01de` · [字段定义](../../DATASET.md)*
