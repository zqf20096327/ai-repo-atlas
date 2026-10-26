# kiliman/codemesh

⭐ 26 · TypeScript · MIT · 推送 2025-11-03 · [GitHub](https://github.com/kiliman/codemesh) · [官网](https://codemeshmcp.com) · 个人维护

**让 agent 写 TypeScript 代码编排多个 MCP 服务器的 MCP 服务器**

CodeMesh 是一个 MCP 服务器，向 AI agent 只暴露 3 个工具（discover-tools、get-tool-apis、execute-code），由 agent 编写 TypeScript 代码在一次执行中调用多个 MCP 服务器（支持 stdio/http/websocket）。代码在 VM2 沙箱中运行（30 秒超时）。其 auto-augmentation 机制：当 agent 遇到不明确的工具输出时进入探索模式并被强制先写 markdown 文档（保存到 .codemesh/），后续 agent 通过 JSDoc 获得解析示例。通过 claude mcp add / npx 安装，配置 .codemesh/config.json 指定目标服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 3 个工具替代数十个独立 MCP 工具，agent 用 TypeScript 编排多服务器
- VM2 沙箱执行（30s 超时），类型安全的 API 生成
- auto-augmentation：强制为不明确输出写文档，后续 agent 复用
- 环境变量替换（${VAR}）与 markdown 文件日志

## 适用场景

- 让 Claude 等客户端通过一段代码协调多个 MCP 服务器完成任务
- 减少多工具调用对 agent 上下文的占用
- 积累工具输出的解析文档，避免重复试错

## 场景标签

`Agent 框架` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L21: CodeMesh lets AI agents write **TypeScript code** to orchestrate **ANY MCP server**. One prompt. One code block. Mu
> L23: Instead of exposing dozens of individual tools, CodeMesh provides just **3 tools**:

## 星数曲线

```mermaid
xychart-beta
    title "kiliman/codemesh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5fe2a09a085f` · [字段定义](../../DATASET.md)*
