# Nuclear-Marmalade/dataforge

⭐ 58 · Python · MIT · 推送 2026-04-07 · [GitHub](https://github.com/Nuclear-Marmalade/dataforge) · [官网](https://nuclearmarmalade.com) · 个人维护

**开源企业数据富化引擎：用免费数据源和本地 AI 补全企业信息**

面向 PostgreSQL 企业数据库的富化工具：读取企业表后补全邮箱、技术栈、SSL 状态、站点速度、行业分类、健康分与痛点。实现方式包括网站抓取、政府数据导入（FCC ULS/NPI Registry/SAM.gov）、SMTP 邮箱验证，以及可选的本地 AI 富化（Ollama 运行 Gemma 生成摘要），无 LLM 也可完成抓取轨道。提供 pip 安装、CLI、CSV 输入输出与 MCP 集成（5 个工具），COALESCE 写入不覆盖已有数据，支持断点续跑。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 层邮箱提取与 SMTP RCPT TO 验证（不实际发信）
- 政府数据导入器：FCC ULS 约 300 万条、NPI 约 700 万条、SAM.gov 约 90 万条
- 本地 AI 富化（Ollama 运行 Gemma）生成摘要/行业分类/健康分，无 API 费用
- MCP 集成提供 forge_discover、forge_enrich_record 等 5 个工具

## 适用场景

- 给 PostgreSQL 里的企业名单批量补全邮箱和技术栈
- 销售线索挖掘时用免费数据源替代付费数据服务
- 在 Claude 等 MCP 客户端中按 ZIP 查找并富化企业记录

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L21: Point FORGE at a PostgreSQL table of businesses and it fills in the blanks: emails, tech stacks, SSL status, site s
> L57: 1. **Web scraping track** -- emails, tech stack, SSL, CMS, site speed. No LLM needed. ~16K records/hr with 4 worker

## 星数曲线

```mermaid
xychart-beta
    title "Nuclear-Marmalade/dataforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-26 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dda746dd9c2f` · [字段定义](../../DATASET.md)*
