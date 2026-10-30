# ThirdKeyAI/SchemaPin

⭐ 16 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/ThirdKeyAI/SchemaPin) · [官网](https://schemapin.org) · 组织维护

**为 AI agent 工具 schema 提供加密签名与验签的开源协议**

SchemaPin 是一套防止 MCP/AI agent 工具供应链攻击（如 MCP Rug Pull）的密码学协议与多语言实现：工具开发者用 ECDSA P-256 密钥签名 schema 与技能文件夹，agent 端验签确保未被篡改。公钥通过 .well-known/schemapin.json（RFC 8615）发现，配合 TOFU 首次使用信任锁定防止密钥替换，另支持密钥撤销、离线信任包、可插拔解析器。提供 Python/JavaScript/Go/Rust 四种语言的 SDK 与 .well-known 端点服务器的源码。当前版本为 v1.4.0-alpha.2，引入签名过期、DNS TXT 交叉验证与 schema 版本绑定等可选特性。

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

- ECDSA P-256 + SHA-256 签名与验签工作流
- TOFU 密钥锁定与 .well-known（RFC 8615）公钥发现
- 密钥撤销文档、离线信任包、可插拔解析器
- Python/JavaScript/Go/Rust 四语言 SDK，附 .well-known 端点服务器

## 适用场景

- 为 MCP 服务器或 agent 工具的 schema 做签名与防篡改验证
- 离线/隔离环境使用信任包完成验签
- 防止工具方上线后偷换 schema 的 Rug Pull 攻击

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: Cryptographic tool schema verification for AI agents and MCP servers. Prevent "MCP Rug Pull" attacks with ECDSA sign
> L9: SchemaPin lets tool developers sign their schemas and skill folders with ECDSA P-256 keys, and lets AI agents verify

## 星数曲线

```mermaid
xychart-beta
    title "ThirdKeyAI/SchemaPin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `169ea99f94ae` · [字段定义](../../DATASET.md)*
