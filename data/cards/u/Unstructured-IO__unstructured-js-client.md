# Unstructured-IO/unstructured-js-client

⭐ 63 · TypeScript · MIT · 推送 2026-10-07 · [GitHub](https://github.com/Unstructured-IO/unstructured-js-client) · 组织维护

**调用 Unstructured 文档处理平台 API 的 TypeScript SDK**

Unstructured Platform API 的 JavaScript/TypeScript HTTP 客户端，覆盖 Partition 端点（文档分区解析），Workflow 端点尚未支持。通过 npm/yarn 安装，也可作为 MCP Server 安装，将 SDK 方法暴露为可被 AI 应用调用的工具（需 Node.js v20+，附 Claude Desktop 与 Cursor 配置步骤）。支持自托管时更改 base URL、自定义 Fetch 封装的 HTTPClient、按请求或全局覆盖重试策略、大 PDF 按页拆分并发上传（默认并发 5，上限 15）、流式文件上传与独立函数（tree-shaking）。SDK 处于 beta，由 Speakeasy 程序化生成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Partition 端点的 TypeScript 客户端，支持自托管 base URL 与自定义 HTTPClient
- 可作为 MCP Server 安装，SDK 方法以工具形式供 AI 应用调用
- 大 PDF 按页拆分并发上传（默认并发 5、上限 15）后重组结果
- 支持重试策略覆盖、流式文件上传与独立函数以减小打包体积

## 适用场景

- 在 JS/TS 项目中接入 Unstructured API 做文档解析
- 通过 Claude Desktop 或 Cursor 以 MCP 工具方式调用文档处理能力
- 自托管 Unstructured API 时以本地 URL 接入

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L6:  TypeScript SDK for the Unstructured API
> L28: This SDK is also an installable MCP server where the various SDK methods are

## 星数曲线

```mermaid
xychart-beta
    title "Unstructured-IO/unstructured-js-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-31 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f62491e35b42` · [字段定义](../../DATASET.md)*
