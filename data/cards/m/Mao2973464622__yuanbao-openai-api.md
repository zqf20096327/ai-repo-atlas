# Mao2973464622/yuanbao-openai-api

⭐ 3 · JavaScript · NOASSERTION · 推送 2026-11-07 · [GitHub](https://github.com/Mao2973464622/yuanbao-openai-api) · 个人维护 · 中文 README

**把腾讯元宝网页版转成本地 OpenAI 兼容 API 的 Node 工具包**

纯 Node 协议实现腾讯元宝网页版，不依赖浏览器常驻：通过搬迁网页 dump 的 2524 个 webpack 模块在 Node 中复现 QIMEI 签名（jsvmp 保护下无法静态逆向），对外提供 OpenAI 兼容服务（/v1/chat/completions 流式/非流式、/v1/models、生图端点、文档对话 /v1/files/chat）。支持扫码登录、78 个官方智能体切换、深度研究搜索模式、工具调用模拟、会话粘性池。声明为研究性质、请勿商用，账号风险自负；需 Node.js ≥ 20，凭据 cookie 存本地需保密。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 零浏览器纯 Node 直连，无需任何 npm 依赖
- OpenAI 兼容端点：chat completions（流式）、images generations/edits、files chat
- 通过 /v1/agents 端点拉取并以 agent_id 切换约 78 个官方智能体
- 工具调用以提示词注入模拟并转译为 OpenAI tool_calls 格式

## 适用场景

- 让只支持 OpenAI API 的客户端接入腾讯元宝模型
- 本地流式调用元宝文本对话与生图能力
- 通过 agent_id 调用 PPT 生成、数据分析等官方智能体
- 上传 txt/pdf/doc 等文件做文档对话

## 场景标签

`模型网关` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L7: 腾讯元宝网页版（yuanbao.tencent.com）的纯协议实现：**零浏览器、纯 Node 直连**，支持文本对话（流式）、AI 生图（文生图 + 图生图）、扫码自动登录。
> L32: |`yuanbao-server.js`|OpenAI 兼容服务：`/v1/chat/completions`（流式/非流式）、`/v1/models`、`/v1/images/generations`、`/v1/images/e
> L93: - **工具调用是提示词注入式模拟**：元宝协议不透传 `tools`，服务把工具定义注入 prompt 并解析模型输出的 `<<TOOL_CALL>>` 标记转换为 OpenAI `tool_calls` 格式（流式请求带 to

## 星数曲线

```mermaid
xychart-beta
    title "Mao2973464622/yuanbao-openai-api 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-18 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `4ffb0a8e917a` · [字段定义](../../DATASET.md)*
