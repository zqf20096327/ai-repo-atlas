# inevolin/agentic-ai-safety-and-security-program

⭐ 14 · TypeScript · 推送 2026-05-21 · [GitHub](https://github.com/inevolin/agentic-ai-safety-and-security-program) · [官网](https://ai.nevolin.be/) · 个人维护

**AI agent 安全研究项目：攻击复现、防御手册与认证培训平台**

针对生产级 Claude（Haiku/Sonnet/Opus）的间接提示注入攻击研究仓库：包含红队 CTF 测试架与 26 个可复现企业攻击演示（单脚本运行）、1,054 行防御手册（10 个防御原语、17 张攻击解剖卡）、1,205 条索引来源（论文/博客/漏洞库条目，10 类攻击分类），以及部署在 ai.nevolin.be 的 Next.js 14 培训平台（6 模块课程、监考考试、签名 PDF 证书与公开验证页）。攻击中涉及厂商域名与 URL 均为占位符，仅用于防御测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 24 个间接提示注入攻击针对 Claude API 端到端测试，单脚本可复现
- 1,054 行防御手册：高管风险登记表 + 10 个防御原语 + 17 张攻击解剖卡
- 1,205 条索引来源（274 论文/博客 + 931 条 Promptfoo 漏洞库条目）
- 生产级培训平台：6 个 MDX 课程模块、40 题监考考试、签名证书与公开验证

## 适用场景

- 安全团队复现 agent 提示注入攻击并验证自身防御
- CISO 或平台团队按防御原语加固企业 agent 部署
- 为部署 agent 的领导者/IT 管理员/开发者提供认证培训
- 研究 prompt injection 与 agent 攻击的文献语料

## 场景标签

`网络安全` `科研工具` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L34: The corpus underneath all of it: **1,205 indexed sources** across ten attack taxonomies — every major paper, blog, 
> L125: |**`sources/`**|**1,205 items** across 10 taxonomy buckets — 274 papers / blogs / reports (each paired with a verb

## 星数曲线

```mermaid
xychart-beta
    title "inevolin/agentic-ai-safety-and-security-program 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `25d14be65718` · [字段定义](../../DATASET.md)*
