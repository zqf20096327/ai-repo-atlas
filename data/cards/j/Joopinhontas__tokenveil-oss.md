# Joopinhontas/tokenveil-oss

⭐ 29 · HTML · NOASSERTION · 推送 2026-08-14 · [GitHub](https://github.com/Joopinhontas/tokenveil-oss) · [官网](https://tokenveil.eu/) · 个人维护 · 中文 README

**自托管匿名化 LLM 聊天代理：敏感数据先脱敏再出网**

基于 FastAPI 的自托管聊天界面与代理：用户消息在服务端进程内先被正则引擎匿名化（邮箱、IP、MAC、IBAN、卡号、电话、API 密钥/令牌等确定性类别），再发给 Claude、Gemini、Vertex AI、Bedrock、OpenAI、Mistral，返回后在进程内还原真实值；真实数据不出本地基础设施。支持本地账号或 LDAP/AD 认证、每用户 OAuth 绑定 Claude 订阅、密文存储映射、实时查看实际外发内容。Community 版用无依赖正则引擎（ELv2），Enterprise 商业版提供 Presidio+spaCy NER 检测，两者仅检测引擎不同。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 出站前进程内正则匿名化，响应后透明还原
- 支持 Claude/Gemini/Vertex AI/Bedrock/OpenAI/Mistral 多供应商
- 每用户经 OAuth 绑定自有 Claude Pro/Max 订阅计费，令牌 Fernet 加密存储
- 仅存储匿名化消息，token↔值映射按会话加密，UI 实时展示实际外发内容

## 适用场景

- 企业内部安全地使用云端 LLM 处理含敏感信息的日志与对话
- 团队按自有订阅共享访问 LLM 且不共用计费 API key
- 合规要求下审计实际发送给模型的内容

## 场景标签

`网络安全` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L23: A self-hosted chat interface for Claude, Gemini, Vertex AI, Bedrock, OpenAI, and Mistral that automatically **anony

## 星数曲线

```mermaid
xychart-beta
    title "Joopinhontas/tokenveil-oss 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 27 --> 30
    line [28, 29, 29]
```

2026-10-18 28 → 2026-10-29 29（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `f9014367e36d` · [字段定义](../../DATASET.md)*
