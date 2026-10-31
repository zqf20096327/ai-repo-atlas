# Automations-Project/n8n-nodes-cloudflare

⭐ 15 · TypeScript · MIT · 推送 2026-06-10 · [GitHub](https://github.com/Automations-Project/n8n-nodes-cloudflare) · [官网](http://npmjs.com/package/n8n-nodes-cloudflare) · 组织维护

**n8n 的 Cloudflare 集成节点包：在 n8n 中管理 100+ Cloudflare 服务**

面向 n8n 用户的社区节点包，封装 100+ Cloudflare API 操作，覆盖 DNS、Workers、R2、D1、KV、Zero Trust、WAF 等服务，按 6 类主节点与 50+ 附加节点组织。节点内置动态下拉菜单，从用户 Cloudflare 账号加载账户、域名、Workers、R2 存储桶等资源。Vectorize 节点内置 RAG（Embed + Store）资源，一步完成文本嵌入与向量存储及相似度检索。需 n8n >= 1.0.0、Node.js >= 18.17.0 与 Cloudflare API 凭证；同包内节点名与其他社区节点冲突时安装会报错。

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

- 100+ Cloudflare API 操作，覆盖 DNS/Workers/R2/D1/KV/Zero Trust 等
- 动态下拉从 Cloudflare 账号加载账户/域名/Workers/R2 存储桶等资源
- Vectorize 节点内置 RAG（Embed + Store）资源，支持插入与相似度搜索文档
- 支持 API Token 与 API Key + Email 两种凭证方式

## 适用场景

- 在 n8n 工作流中自动化管理 Cloudflare DNS、证书与防火墙规则
- 通过工作流部署 Workers、操作 R2 存储与 D1 数据库
- 在 n8n 内搭建基于 Workers AI 嵌入 + Vectorize 的文档检索流程

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L22: Comprehensive n8n community nodes for **Cloudflare** - manage your entire Cloudflare infrastructure from n8n workfl
> L111: The **Cloudflare Vectorize** node includes a built-in **RAG (Embed + Store)** resource that combines Workers AI em
> L122: - **n8n** >= 1.0.0

## 星数曲线

```mermaid
xychart-beta
    title "Automations-Project/n8n-nodes-cloudflare 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9e4d31b4962d` · [字段定义](../../DATASET.md)*
