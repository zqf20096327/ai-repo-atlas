# HorseSword/joplin-plugin-notellm

⭐ 46 · TypeScript · AGPL-3.0 · 推送 2026-07-12 · [GitHub](https://github.com/HorseSword/joplin-plugin-notellm) · 个人维护 · 中文 README

**Joplin 笔记的 AI 插件：聊天、摘要、改写、问答与 MCP 工具**

面向 Joplin 用户的 AI 笔记插件，通过 OpenAI 兼容 API 接入 LLM（可配置 3 个模型切换），提供基于光标上文或选中文本的聊天、摘要、改写、问答功能。支持 streamableHTTP 模式的 MCP 工具调用（最多 42 个服务器，要求 LLM 支持 tool call，暂不支持 STDIO/SSE）。限制：仅支持 markdown 编辑器；Android 端目前仅支持聊天，且受 CORS 限制部分本地服务需配代理。通过 Joplin 插件市场或 .jpl 文件安装，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天/摘要/改写/问答，按光标位置或选区确定发送内容
- 可配置 3 个 LLM 并切换，支持 OpenAI 兼容 API 与本地服务器
- streamableHTTP MCP 工具调用（最多 42 个 MCP 服务器）
- 不收集日志与个人信息，开源 AGPL-3.0

## 适用场景

- 在 Joplin 笔记内与 AI 对话、摘要长文
- 让 LLM 按我的指示改写选中段落
- 在笔记中调用 MCP 工具扩展 LLM 能力

## 场景标签

`知识库管理` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L18: - **Chat**:
> L30: - **MCP Supported**:
> L15: - **Customizable LLM Service Source**:

## 星数曲线

```mermaid
xychart-beta
    title "HorseSword/joplin-plugin-notellm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4cb1e21f7be4` · [字段定义](../../DATASET.md)*
