# FlowEngine-cloud/flowengine

⭐ 16 · TypeScript · NOASSERTION · 推送 2026-09-10 · [GitHub](https://github.com/FlowEngine-cloud/flowengine) · [官网](https://flowengine.cloud) · 组织维护

**面向自动化代理机构的白标客户门户：管理 n8n 实例与客户计费**

面向使用 n8n 的自动化代理机构的白标客户门户。机构自托管后可邀约客户登录，控制其可见内容，管理 n8n、OpenClaw 与 Docker 实例的部署与状态，提供跨实例执行与工作流总览、聊天机器人/表单 UI 嵌入、工作流模板分发、客户凭据直传 n8n、WhatsApp API 接入、Stripe 订阅计费与品牌定制。凭据以 AES-256 加密存储，数据库启用行级安全。技术栈为 Next.js 15 + Supabase + Docker。许可含 Commons Clause，禁止商业嵌入与竞争性托管服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 白标客户门户：按客户端控制实例可见性与访问权限
- 跨实例执行与工作流总览，支持按工作流/状态/客户过滤
- 可嵌入聊天机器人/表单一键关联 n8n 工作流 webhook
- 凭据 AES-256 加密存储，Supabase RLS 行级安全

## 适用场景

- 自动化代理机构向客户交付白标门户管理 n8n 实例
- 通过 Stripe 对客户的实例使用与订阅计费
- 向客户分发工作流模板并统一推送更新

## 场景标签

 · 领域:自动化服务/客户门户

## 证据(README 行号)

> L3: White-label client portal for automation agencies (mainly using n8n). Manage instances, invite clients, control what
> L56: - **n8n** - connect your own self-hosted instance or deploy via FlowEngine managed hosting

## 星数曲线

```mermaid
xychart-beta
    title "FlowEngine-cloud/flowengine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ed456bfcbe93` · [字段定义](../../DATASET.md)*
