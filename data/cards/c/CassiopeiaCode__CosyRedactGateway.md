# CassiopeiaCode/CosyRedactGateway

⭐ 105 · JavaScript · Apache-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/CassiopeiaCode/CosyRedactGateway) · 个人维护 · 中文 README

**给程序员的 LLM API 凭据脱敏网关：出网前替换敏感值并可逆还原**

面向程序员的本地优先、无状态 LLM 隐私网关：在请求转发到 OpenAI/Anthropic 等上游前，用已知格式规则与高熵凭据检测命中敏感文本并替换为占位符；模型原样返回占位符时，在 JSON 响应、受支持的 SSE 流和工具调用参数中为应用还原原值，请求级映射不持久化。单文件 worker.js 可运行于 Cloudflare Workers、Deno 或 Node.js 20+ 本地适配器，通过 URL 开关组合 7 类检测器（高熵/电话/sk- 密钥/身份证/银行卡/邮箱/Gitleaks 规则）。限制：认证头仍转发，不做协议转换，流式兼容仅覆盖受支持字段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 高熵凭据检测：无厂商前缀也可识别随机形态凭据候选
- 占位符在 JSON、受支持 SSE 流与工具调用参数中可逆还原，跨 chunk 缓冲
- 单文件 worker.js 部署到 Cloudflare Workers / Deno / Node 20+，无运行时依赖
- URL 字母开关 HPSIBEG 组合 7 类检测器，未知字母返回 400

## 适用场景

- 把代码/日志发给 LLM 前拦截凭据与敏感个人信息
- 现有 OpenAI/Anthropic SDK 工作流改 Base URL 即接入，不换模型和请求结构
- IDE 助手、命令行工具经自定义 API Base URL 走本地网关脱敏

## 场景标签

`模型网关` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L23: **Cosy 是面向程序员的 LLM 凭据脱敏网关，核心是高熵凭据检测（High-entropy credential detection）。** 它不仅匹配已知密钥格式，还对符合条件的文本块进行统计评分，寻找随机形态的凭据候选，
> L172: |**协议透传**|保留上游请求结构，而不是在不同 API 家族之间转换。|
> L200: |API 家族|请求处理|响应处理|

## 星数曲线

```mermaid
xychart-beta
    title "CassiopeiaCode/CosyRedactGateway 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 103 --> 106
    line [104, 105, 105]
```

2026-10-18 104 → 2026-10-30 105（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `768cef35aaf9` · [字段定义](../../DATASET.md)*
