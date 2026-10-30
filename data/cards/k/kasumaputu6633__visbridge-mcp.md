# kasumaputu6633/visbridge-mcp

⭐ 44 · TypeScript · Apache-2.0 · 推送 2026-09-18 · [GitHub](https://github.com/kasumaputu6633/visbridge-mcp) · 个人维护

**给无视觉能力模型加看图功能的 MCP 服务器**

一个 MCP 服务器（stdio + Streamable HTTP 两种传输），暴露单一 analyze_image 工具，让无原生视觉能力的推理模型或希望省 token 的客户端理解图片：客户端仅发送图片引用和模式，服务器解析图片（本地路径/URL/base64/resource 四种来源），调用 OpenAI 兼容的视觉模型，返回紧凑纯文本。提供 describe/ocr/inspect 三种模式，内置 SSRF 防护、本地图片降采样、10 类结构化错误与 token/费用日志。设计为本地运行，HTTP 传输无内置鉴权，不支持公开托管。需 Node.js>=20 与一个视觉模型 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 analyze_image 工具，describe/ocr/inspect 三种模式
- 支持任意 OpenAI 兼容视觉端点，provider 无关
- SSRF 防护（DNS 预解析、私网/环回地址阻断、重定向逐跳校验）
- 本地图片降采样（默认最长边 2048）与无凭证的 mock 离线模式

## 适用场景

- 给 Claude Code、Cursor 等编程客户端中的纯文本模型补上读图能力
- 通过 OCR 模式从截图提取文字并去代码围栏
- 用 inspect 模式对图片提特定问题并控制输出 token 预算

## 场景标签

`多模态` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L11: Token-efficient vision for MCP clients. An MCP server
> L15: It exists for one reason: to give a **model without native vision** (or any client that wants to
> L16: spend fewer tokens) the ability to understand images. The client sends only an image *reference*

## 星数曲线

```mermaid
xychart-beta
    title "kasumaputu6633/visbridge-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6f2c6be9de04` · [字段定义](../../DATASET.md)*
