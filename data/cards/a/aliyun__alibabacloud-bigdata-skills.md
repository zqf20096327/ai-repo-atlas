# aliyun/alibabacloud-bigdata-skills

⭐ 19 · Python · Apache-2.0 · 推送 2026-06-16 · [GitHub](https://github.com/aliyun/alibabacloud-bigdata-skills) · [官网](https://www.aliyun.com/product/dide) · 组织维护 · 中文 README

**教 AI agent 使用阿里云大数据服务 Open API 的技能包集合**

阿里云维护的 AI agent 技能仓库：每个技能是自包含包，通过 SKILL.md、官方 SDK 与 API 发现脚本，教 AI agent 与特定云服务交互。当前提供 DataWorks open-api 技能，覆盖数据开发、任务运维、数据集成、数据质量、元数据血缘等，支持 Node.js/Python/Java SDK。使用方式为将技能放入 agent 技能目录，配置阿里云凭证环境变量后运行发现脚本。与 DataWorks Agent、DataWorks MCP Server 互为补充。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SKILL.md 自包含技能包，教 agent 调用 DataWorks Open API
- 动态 API 发现脚本（fetch_api_overview / list_openapi_meta_apis）
- 官方 SDK 支持 Node.js / Python / Java

## 适用场景

- 让自己的 AI agent 按 DataWorks 最佳实践操作云上数据开发
- 在 IDE 或自建 agent 工作流中接入 DataWorks 能力
- 探索 DataWorks Open API 的可用接口

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L19: A collection of AI agent skills for Alibaba Cloud big data services. Each skill is a self-contained package that te
> L39: 2. Read the `SKILL.md` inside — it contains all instructions an AI agent needs.

## 星数曲线

```mermaid
xychart-beta
    title "aliyun/alibabacloud-bigdata-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3b0d92542f6c` · [字段定义](../../DATASET.md)*
